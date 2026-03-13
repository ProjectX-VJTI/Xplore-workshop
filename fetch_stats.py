import urllib.request
import urllib.error
import json
import os
import time
from datetime import datetime, timezone, timedelta

OWNER = "ProjectX-VJTI"
REPO = "Xplore-workshop"
TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Bearer {TOKEN}" if TOKEN else "",
    "X-GitHub-Api-Version": "2022-11-28"
}

def fetch_api(endpoint):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/{endpoint}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 202:
            print("GitHub is compiling stats. Waiting 5 seconds...")
            time.sleep(5)
            return fetch_api(endpoint)
        print(f"Error fetching {url}: {e}")
        return []
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

def main():
    print(f"Fetching data for {OWNER}/{REPO}...")
    
    # Dates for timeframe filtering
    now = datetime.now(timezone.utc)
    date_3m = now - timedelta(days=90)
    date_6m = now - timedelta(days=180)

    users_data = {}

    # 1. Fetch Commit & Changes Stats using /stats/contributors
    # This natively provides additions, deletions, and commits mapped by week
    commit_stats = fetch_api("stats/contributors")
    for stat in commit_stats:
        author = stat.get("author")
        if not author: continue
        login = author.get("login")
        
        users_data[login] = {
            "login": login,
            "avatar_url": author.get("avatar_url"),
            "role": "contributor", # Default, overridden later if needed
            "stats": {
                "all": {"commits": 0, "changes": 0, "prsOpened": 0, "prsMerged": 0},
                "6m": {"commits": 0, "changes": 0, "prsOpened": 0, "prsMerged": 0},
                "3m": {"commits": 0, "changes": 0, "prsOpened": 0, "prsMerged": 0}
            }
        }
        
        for week in stat.get("weeks", []):
            week_date = datetime.fromtimestamp(week["w"], tz=timezone.utc)
            commits = week["c"]
            changes = week["a"] + week["d"]
            
            users_data[login]["stats"]["all"]["commits"] += commits
            users_data[login]["stats"]["all"]["changes"] += changes
            
            if week_date >= date_6m:
                users_data[login]["stats"]["6m"]["commits"] += commits
                users_data[login]["stats"]["6m"]["changes"] += changes
            if week_date >= date_3m:
                users_data[login]["stats"]["3m"]["commits"] += commits
                users_data[login]["stats"]["3m"]["changes"] += changes

    # 2. Fetch PRs (Pagination up to 100 to keep it lightweight, adjust per_page if huge repo)
    prs = fetch_api("pulls?state=all&per_page=100")
    for pr in prs:
        user = pr.get("user")
        if not user: continue
        login = user.get("login")
        
        # Ensure user exists in our dict
        if login not in users_data:
            continue

        # Check Roles (if they are repo owner/collaborator)
        association = pr.get("author_association", "")
        if association == "OWNER" or login == OWNER:
            users_data[login]["role"] = "admin"
        elif association in ["MEMBER", "COLLABORATOR"] and users_data[login]["role"] != "admin":
            users_data[login]["role"] = "collaborator"

        # Calculate PR stats based on dates
        created_at = datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        merged_at = datetime.strptime(pr["merged_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc) if pr.get("merged_at") else None

        users_data[login]["stats"]["all"]["prsOpened"] += 1
        if created_at >= date_6m: users_data[login]["stats"]["6m"]["prsOpened"] += 1
        if created_at >= date_3m: users_data[login]["stats"]["3m"]["prsOpened"] += 1

        if merged_at:
            users_data[login]["stats"]["all"]["prsMerged"] += 1
            if merged_at >= date_6m: users_data[login]["stats"]["6m"]["prsMerged"] += 1
            if merged_at >= date_3m: users_data[login]["stats"]["3m"]["prsMerged"] += 1

    # Convert dictionary to list
    final_data = list(users_data.values())

    # Save to JSON
    with open("data.json", "w") as f:
        json.dump(final_data, f, indent=4)
    print("Successfully generated data.json!")

if __name__ == "__main__":
    main()