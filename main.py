#!/usr/bin/env python3
"""quick-dad-joke – fetch and display a random dad joke.

A minimal script with zero external magic; just a simple HTTP GET.
"""
import json
import sys

# Try to import requests for simplicity; fall back to urllib if unavailable.
try:
    import requests
except ImportError:
    requests = None
    import urllib.request
    import urllib.error

API_URL = "https://icanhazdadjoke.com/"
HEADERS = {"Accept": "application/json", "User-Agent": "quick-dad-joke/0.1"}

def fetch_joke():
    """Return a joke string, handling network issues.
    """
    if requests:
        try:
            resp = requests.get(API_URL, headers=HEADERS, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            return data.get("joke", "Why did the chicken cross the road? To get to the other side!")
        except Exception as e:
            return f"[Error fetching joke: {e}] Keep smiling anyway!"
    else:
        try:
            req = urllib.request.Request(API_URL, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=5) as f:
                raw = f.read().decode()
                data = json.loads(raw)
                return data.get("joke", "Why did the chicken cross the road? To get to the other side!")
        except urllib.error.URLError as e:
            return f"[Network issue: {e.reason}] Stay jolly!"
        except Exception:
            return "[Unexpected error] Have a great day!"

def main():
    joke = fetch_joke()
    print(joke)

if __name__ == "__main__":
    sys.exit(main())
