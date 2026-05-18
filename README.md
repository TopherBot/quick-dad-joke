# quick-dad-joke

**What it does**: Pulls a random dad joke from the public `https://icanhazdadjoke.com/` API and prints it to the console.

**Why it matters**: No more scrolling through endless joke websites—just a single command for instant humor.

## Usage
```bash
# Install (requires Python 3.7+)
pip install -r requirements.txt   # optional, see note below

# Run the script
python3 main.py
```

## Features
- One‑liner source code (under 30 lines).
- Uses the standard `requests` library (if missing, it falls back to Python's built‑in `urllib`).
- Handles network errors gracefully with a friendly fallback joke.

## Extending
- Plug it into your CI/CD pipeline to post a joke on every successful build.
- Wrap it in a Telegram bot (quick‑telegram‑alert) for daily joke notifications.

---
*Tiny, happy, and always ready to make you smile.*