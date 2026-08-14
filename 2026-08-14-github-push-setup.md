# Push 100-days-of-code to github.com/yigitisik/CUNY-Python

Prepared 2026-08-14. You'll run these yourself in VSCode / a terminal where
you're logged into GitHub. The commits will use YOUR local git identity, not
anyone else's.

## Already done for you
- `.gitignore` added — excludes all `.env`/`keys.env`, `.idea/`, venvs,
  `.DS_Store`, `*.exe`.
- Hardcoded API keys scrubbed to `os.environ.get(...)` in:
  - `day-36-stock-tickers/main.py` (Alpha Vantage, News API, Twilio)
  - `day-37-post-requests-tracker/main.py` and `gui.py` (Pixela token)
  - `day-35-api-auth-sms/main.py` (Twilio Account SID — a dead commented-out
    second SID on the same line was also removed)
  - `day-38-google-sheets-api/main.py` (Nutritionix app ID/key — these were
    unused dead literals; the file already read the env vars correctly
    elsewhere)

## ⚠️ Do these two things
1. **Revoke the token you pasted into chat** (`cuny-python-token`) at
   GitHub → Settings → Developer settings → Personal access tokens. It was
   exposed in the conversation. You don't need it for VSCode's built-in auth.
2. **Rotate the exposed keys** in each provider dashboard (Amadeus, Twilio,
   Sheety, Spotify, Alpha Vantage, News API, Pixela) — they sat in plaintext
   on disk. To run the projects later, put the values in each folder's `.env`
   (already gitignored).

## Confirm your git identity (so the author is you, not a default)
```bash
git config user.name  "yigitisik"
git config user.email "86640635+yigitisik@users.noreply.github.com"
```

## Verify nothing sensitive will be committed
```bash
cd "100-days-of-code"
git init
git add -A
git status
git ls-files | grep -iE '\.env|keys\.env|\.idea' || echo "clean — no secrets staged"
```

## Option A — add alongside the existing repo files (non-destructive)
Keeps the old folders (Coffee Machine, hangman, etc.) already on `main`.
```bash
cd "100-days-of-code"
git init
git remote add origin https://github.com/yigitisik/CUNY-Python.git
git fetch origin
git checkout -b main origin/main
git add -A
git commit -m "Add structured 100 Days of Code projects (day-01..day-79)"
git push origin main
```

## Option B — replace remote contents with this clean structure
Overwrites `main`. Only if you want the repo to contain just day-01..day-79.
```bash
cd "100-days-of-code"
git init
git add -A
git commit -m "Restructure repo: 100 Days of Code (day-01..day-79)"
git branch -M main
git remote add origin https://github.com/yigitisik/CUNY-Python.git
git push -u --force origin main
```
