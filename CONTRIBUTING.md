🤝 CONTRIBUTING.md
# Contributing Guidelines

This guide explains how students should solve exercises and submit their solutions properly.

## 🛠️ Steps to Submit Your Solutions

### 1️⃣ Fork the Repository

Fork this repository to your own GitHub account.

### 2️⃣ Clone Your Fork
```
git clone https://github.com/<your-username>/Xplore-workshop.git
cd CoC-git-python-workshop
```
### 3️⃣ Create Your Solutions Folder

**Note: You can also run the `my_dir_setup.py` in main directory, to automate making your directory,but it only works within your fork.**

Inside the repository, create a folder inside top-level directory `SOLUTIONS` named:
```
<githubid>_solutions
```
📌 Example:

`aswadekarb24-code_solutions/`

### 4️⃣ Copy the Playground

Copy the entire `test_playground` directory into your solutions folder:
```
SOLUTIONS
└── <githubid>_solutions/
      └── test_playground/
```

⚠️ Do not modify the original test_playground directory or any file/directory outside your solutions directory.

### 5️⃣ Set Up Virtual Environment

Create a virtual environment using Python 3.12.0 or 3.14.2 (important to avoid conflicts):
```
# Windows
py -3.12 -m venv venv
venv\Scripts\Activate
```

```
# Linux/Mac
python3.12 -m venv venv
source venv/bin/activate  
```
Install dependencies:
```
pip install -r requirements.txt
# or pip install -r requirements-3.14.2.txt in case of 3.14.2
# 3.14.x should also work, but do contact on group if conflicts faced
```

### 6️⃣ Implement Your Fixes & Enhancements

- Make all changes only inside your `<githubid>_solutions` folder

- Fix bugs in the copied files

- You may also:

  - Add your own Python scripts

  - Showcase something new you learned

  - Implement alternative or improved solutions

7️⃣ Commit & Open a Pull Request

```
git add .
git commit -m "Fix: completed basics and intermediate exercises"
git push origin main
```

- Open a Pull Request (PR) to the upstream repository

- Follow the PR format provided in the repository

## ✅ Important Rules

- ❌ Do NOT edit original tutorial or top level files ro ANY files outside your solutions folder

- Make sure to sync your fork before making any PR, either via github website or by
```
git remote add upstream https://github.com/ProjectX-VJTI/Xplore-workshop
git fetch upstream
git merge upstream/main # or git rebase
git push origin main
```

- ✅ Work only inside your solutions folder

- ✅ Keep code clean and readable

- ✅ Use meaningful commit messages

## 🎉 Final Note

This repository is meant to help you:

- Learn Python deeply

- Improve debugging skills

- Gain confidence with real code

- 💡 Experiment, break things, fix them, and enjoy the process!

**Happy coding! 🐍✨**


## Note for Maintainers

1. Be civil with FYs.
2. Ensure the repository is in working condition.
3. You have the ability to push to main, Use it wisely and only after discussion with other maintainers.
