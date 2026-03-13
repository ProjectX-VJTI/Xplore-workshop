const Config = {
    owner: "ProjectX-VJTI", // Update this
    repo: "Xplore-workshop", // Update this
    apiUrl: "https://api.github.com"
};

const API = {
    async getRepoInfo() {
        const res = await fetch(`${Config.apiUrl}/repos/${Config.owner}/${Config.repo}`);
        return res.ok ? await res.json() : null;
    },
    async getFile(filename) {
        const res = await fetch(`${Config.apiUrl}/repos/${Config.owner}/${Config.repo}/contents/${filename}`);
        if (!res.ok) return "Not available";
        const data = await res.json();
        return atob(data.content); 
    },
    async getLeaderboardData() {
        try {
            const res = await fetch(`data.json?t=${new Date().getTime()}`);
            if (!res.ok) throw new Error("Data file not found");
            return await res.json();
        } catch (error) {
            console.error("Failed to load data.json. Has the GitHub Action run yet?", error);
            return [];
        }
    }
};

const UI = {
    container: document.getElementById('views'),
    loader: document.getElementById('loader'),

    showLoader() {
        this.loader.classList.remove('d-none');
        this.container.innerHTML = '';
        this.container.classList.remove('fade-enter');
    },

    hideLoader() {
        this.loader.classList.add('d-none');
        this.container.classList.add('fade-enter');
    },

    getBadge(role, mergedPrs) {
        let badges = [];
        if (role === 'admin') badges.push('<span class="badge-admin" title="Admin"><i class="fa-solid fa-hashtag"></i>1</span>');
        if (role === 'collaborator') badges.push('<span class="badge-veteran" title="Collaborator"><i class="fa-solid fa-star"></i> Veteran</span>');
        
        if (mergedPrs > 10) badges.push('<i class="fa-solid fa-gem badge-diamond" title=">10 PRs"></i>');
        else if (mergedPrs >= 5) badges.push('<i class="fa-solid fa-medal badge-gold" title="5-9 PRs"></i>');
        else if (mergedPrs >= 3) badges.push('<i class="fa-solid fa-medal badge-silver" title="3-4 PRs"></i>');
        else if (mergedPrs >= 1) badges.push('<i class="fa-solid fa-medal badge-bronze" title="1-2 PRs"></i>');
        
        return badges.join(' ');
    },

    async renderHome(metric = 'commits', timeframe = 'all') {
        this.showLoader();
        const repo = await API.getRepoInfo();
        let users = await API.getLeaderboardData();
        
        users.sort((a, b) => b.stats[timeframe][metric] - a.stats[timeframe][metric]);

        let html = `
            <div class="text-center mb-5">
                <h1 class="display-4">${repo ? repo.name : Config.repo}</h1>
                <p class="lead text-secondary">${repo ? repo.description : 'A GitHub Repository'}</p>
                <a href="${repo ? repo.html_url : '#'}" target="_blank" class="btn btn-outline-light"><i class="fa-brands fa-github"></i> View on GitHub</a>
            </div>

            <div class="card p-4">
                <div class="d-flex justify-content-between align-items-center mb-3 flex-wrap gap-3">
                    <h3>Leaderboard</h3>
                    <div class="d-flex gap-2">
                        <select id="timeFilter" class="form-select bg-dark text-light border-secondary" onchange="UI.filterLeaderboard()">
                            <option value="all" ${timeframe === 'all' ? 'selected' : ''}>All Time</option>
                            <option value="6m" ${timeframe === '6m' ? 'selected' : ''}>Last 6 Months</option>
                            <option value="3m" ${timeframe === '3m' ? 'selected' : ''}>Last 3 Months</option>
                        </select>
                        <select id="metricFilter" class="form-select bg-dark text-light border-secondary" onchange="UI.filterLeaderboard()">
                            <option value="commits" ${metric === 'commits' ? 'selected' : ''}>Commits</option>
                            <option value="prsOpened" ${metric === 'prsOpened' ? 'selected' : ''}>PRs Opened</option>
                            <option value="prsMerged" ${metric === 'prsMerged' ? 'selected' : ''}>PRs Merged</option>
                        </select>
                    </div>
                </div>
                <div class="table-responsive">
                    <table class="table table-dark table-hover align-middle">
                        <thead>
                            <tr>
                                <th>Contributor</th>
                                <th>Badges</th>
                                <th>Score (${metric})</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${users.map(u => `
                                <tr class="contributor-row" onclick="Router.navigate('profile', '${u.login}')">
                                    <td>
                                        <img src="${u.avatar_url}" width="30" class="rounded-circle me-2">
                                        ${u.login}
                                    </td>
                                    <td>${this.getBadge(u.role, u.stats.all.prsMerged)}</td>
                                    <td>${u.stats[timeframe][metric]}</td>
                                </tr>
                            `).join('')}
                        </tbody>
                    </table>
                </div>
            </div>
        `;
        this.container.innerHTML = html;
        this.hideLoader();
    },

    filterLeaderboard() {
        const metric = document.getElementById('metricFilter').value;
        const timeframe = document.getElementById('timeFilter').value;
        this.renderHome(metric, timeframe);
    },

    async renderMarkdownPage(title, file1, file2 = null) {
        this.showLoader();
        let content1 = await API.getFile(file1);
        let content2 = file2 ? await API.getFile(file2) : null;
        
        let html = `<div class="card p-4 markdown-body text-light"><h2>${title}</h2><hr>`;
        html += content1 === "Not available" ? `<p>${file1} is not available.</p>` : marked.parse(content1);
        
        if (file2) {
            html += `<hr><h3 class="mt-5">License</h3>`;
            html += content2 === "Not available" ? `<p>License not available.</p>` : marked.parse(content2);
        }
        
        html += `</div>`;
        this.container.innerHTML = html;
        this.hideLoader();
    },

    async renderProfile(username) {
        this.showLoader();
        const users = await API.getLeaderboardData();
        const user = users.find(u => u.login === username);

        if (!user) {
            this.container.innerHTML = `<p class="text-danger">User not found.</p>`;
            this.hideLoader();
            return;
        }

        let html = `
            <button class="btn btn-outline-secondary mb-4" onclick="Router.navigate('home')">
                <i class="fa-solid fa-arrow-left"></i> Back to Leaderboard
            </button>
            
            <div class="row">
                <div class="col-md-4">
                    <div class="card p-4 text-center">
                        <img src="${user.avatar_url}" class="rounded-circle mx-auto mb-3" width="150">
                        <h3>${user.login}</h3>
                        <div class="mb-3 fs-4">${this.getBadge(user.role, user.stats.all.prsMerged)}</div>
                        <a href="https://github.com/${user.login}" target="_blank" class="btn btn-dark border-secondary">GitHub Profile</a>
                        <a href="https://github.com/${user.login}/${Config.repo}" target="_blank" class="btn btn-dark border-secondary mt-2">View Fork</a>
                    </div>
                </div>
                <div class="col-md-8">
                    <div class="card p-4 mb-4">
                        <h4>Commit History</h4>
                        <img src="https://ghchart.rshah.org/219138/${user.login}" alt="${user.login}'s commit chart" class="img-fluid rounded bg-dark p-2 border border-secondary">
                    </div>
                    <div class="card p-4">
                        <h4>Stats Overview</h4>
                        <ul class="list-group list-group-flush bg-transparent">
                            <li class="list-group-item bg-transparent text-light"><b>Total Commits:</b> ${user.stats.all.commits}</li>
                            <li class="list-group-item bg-transparent text-light"><b>PRs Opened:</b> ${user.stats.all.prsOpened}</li>
                            <li class="list-group-item bg-transparent text-light"><b>PRs Merged:</b> ${user.stats.all.prsMerged}</li>
                        </ul>
                    </div>
                </div>
            </div>
        `;
        this.container.innerHTML = html;
        this.hideLoader();
    }
};

const Router = {
    navigate(view, param = null) {
        window.location.hash = view;
        switch (view) {
            case 'home': UI.renderHome(); break;
            case 'desc': UI.renderMarkdownPage('Project Description', 'README.md', 'LICENSE'); break;
            case 'contrib': UI.renderMarkdownPage('Contributing Guidelines', 'CONTRIBUTING.md'); break;
            case 'profile': param ? UI.renderProfile(param) : this.navigate('home'); break;
            default: UI.renderHome();
        }
    },
    init() {
        const hash = window.location.hash.replace('#', '');
        this.navigate(hash || 'home');
    }
};

document.addEventListener("DOMContentLoaded", () => Router.init());
