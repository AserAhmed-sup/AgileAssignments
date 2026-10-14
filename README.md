# DevOps Practice App

A minimal Flask app, structured for AWS Elastic Beanstalk, meant for practicing
Git workflows and deployment pipelines.

## Run locally

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python application.py
```

Visit http://localhost:5000

## Git workflow to practice

```bash
git init
git add .
git commit -m "Initial commit: minimal Flask app"

# Practice branching
git checkout -b feature/add-about-page
# ...make a change...
git add .
git commit -m "Add about page"
git checkout main
git merge feature/add-about-page

# Push to a remote (create an empty repo on GitHub first)
git remote add origin <your-repo-url>
git branch -M main
git push -u origin main
```

Good exercises:
- Make a feature branch per change, open a PR, merge it.
- Add a GitHub Actions workflow that runs a lint/test step on push.
- Tag releases (`git tag v0.1.0`) and bump `APP_VERSION` in `.ebextensions/env.config`.

## Deploy to Elastic Beanstalk

Install the EB CLI, then from this directory:

```bash
eb init -p python-3.11 devops-practice-app
eb create devops-practice-env
eb deploy        # run this after each change you want to ship
eb open
eb logs          # troubleshooting
```

Notes:
- `Procfile` tells EB how to start the app with gunicorn.
- `.ebextensions/env.config` sets environment variables on the EB environment.
- `/health` is a lightweight endpoint you can point EB's health check at
  (Configuration → Load balancer → Health check path).

## Suggested next steps for practice

- Add a `/api/items` endpoint backed by an in-memory list, then a database.
- Wire up a CI pipeline (GitHub Actions) that runs tests and deploys with `eb deploy`.
- Practice rolling back a bad deploy with `eb deploy --version <label>`.
