import urllib.request
import json
import os
from datetime import datetime, timezone, timedelta

# --- CONFIGURATION ---
OWNER = "ProjectX-VJTI"  # Update this!
REPO = "Xplore-workshop"  # Update this!
TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Bearer {TOKEN}" if TOKEN else "",
    "X-GitHub-Api-Version": "2022-11-28"
}

def fetch_paginated(endpoint):
    """Fetches all pages of a GitHub API endpoint."""
    data = []
    page = 1
    while True:
        # Determine if we need to append with ? or &
        separator = "&" if "?" in endpoint else "?"
        url = f"https://api.github.com/repos/{OWNER}/{REPO}/{endpoint}{separator}per_page=100&page={page}"
        
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as response:
                page_data = json.loads(response.read().decode())
                if not page_data: # If the page is empty, we've hit the end
                    break
                data.extend(page_data)
                page += 1
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            break
    return data

def main():
    print(f"Fetching complete commit and PR history for {OWNER}/{REPO}...")
    
    # Set up timeframes
    now = datetime.now(timezone.utc)
    date_3m = now - timedelta(days=90)
    date_6m = now - timedelta(days=180)

    users_data = {}

    def get_or_create_user(login, avatar_url):
        if login not in users_data:
            users_data[login] = {
                "login": login,
                "avatar_url": avatar_url,
                "role": "contributor",
                "stats": {
                    "all": {"commits": 0, "prsOpened": 0, "prsMerged": 0},
                    "6m": {"commits": 0, "prsOpened": 0, "prsMerged": 0},
                    "3m": {"commits": 0, "prsOpened": 0, "prsMerged": 0}
                }
            }
        return users_data[login]

    # 1. Fetch Commits manually to get exact dates
    print("Processing commits...")
    commits = fetch_paginated("commits")
    for c in commits:
        author = c.get("author")
        if not author: continue  # Skip commits without linked GitHub accounts
        
        login = author.get("login")
        avatar_url = author.get("avatar_url")
        
        commit_date_str = c["commit"]["author"]["date"]
        commit_date = datetime.strptime(commit_date_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        
        user = get_or_create_user(login, avatar_url)
        
        user["stats"]["all"]["commits"] += 1
        if commit_date >= date_6m: user["stats"]["6m"]["commits"] += 1
        if commit_date >= date_3m: user["stats"]["3m"]["commits"] += 1

    # 2. Fetch all Pull Requests
    print("Processing pull requests...")
    prs = fetch_paginated("pulls?state=all")
    for pr in prs:
        user_info = pr.get("user")
        if not user_info: continue
        
        login = user_info.get("login")
        avatar_url = user_info.get("avatar_url")
        
        user = get_or_create_user(login, avatar_url)
        
        # Check roles natively via the PR association
        association = pr.get("author_association", "")
        if association == "OWNER" or login == OWNER:
            user["role"] = "admin"
        elif association in ["MEMBER", "COLLABORATOR"] and user["role"] != "admin":
            user["role"] = "collaborator"

        # Tally PRs by date
        created_at = datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        merged_at_str = pr.get("merged_at")
        
        user["stats"]["all"]["prsOpened"] += 1
        if created_at >= date_6m: user["stats"]["6m"]["prsOpened"] += 1
        if created_at >= date_3m: user["stats"]["3m"]["prsOpened"] += 1
        
        if merged_at_str: # If merged_at exists, the PR was merged
            merged_at = datetime.strptime(merged_at_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            user["stats"]["all"]["prsMerged"] += 1
            if merged_at >= date_6m: user["stats"]["6m"]["prsMerged"] += 1
            if merged_at >= date_3m: user["stats"]["3m"]["prsMerged"] += 1

    # Convert dictionary to list
    final_data = list(users_data.values())

    # Save to JSON
    with open("data.json", "w") as f:
        json.dump(final_data, f, indent=4)
    print(f"Successfully generated data.json with {len(final_data)} contributors!")

if __name__ == "__main__":
    main()