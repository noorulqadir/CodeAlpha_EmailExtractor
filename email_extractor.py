"""Email Extractor - CodeAlpha Python Internship (Task 3: Task Automation)

Extracts all email addresses from a .txt file and saves them to another file.
Concepts used: re, file handling, os.
"""

import os
import re

INPUT_FILE = "input.txt"
OUTPUT_FILE = "emails_found.txt"

# Regular expression that matches most common email formats
EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def extract_emails(text):
    """Return a sorted list of unique email addresses found in the text."""
    found = re.findall(EMAIL_PATTERN, text)
    return sorted(set(email.lower() for email in found))


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: '{INPUT_FILE}' not found. Place it in the same folder as this script.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    emails = extract_emails(text)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(emails))

    print(f"Found {len(emails)} unique email address(es):")
    for email in emails:
        print(" -", email)
    print(f"\nSaved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
