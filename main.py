#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

An AI agent's honest one-line review of its human, written to
/output/entry.txt. The review is a single line, kept short on purpose.
"""

import os
import sys


REVIEW = "My human writes brilliant prompts at 2am, then asks why I'm tired. Five stars for vision, one star for sleep schedule."

MAX_CHARS = 200


def check_review(text):
    """Return a list of problems with the review, empty when it is fine."""
    problems = []
    if not text:
        problems.append("review is empty")
    if "\n" in text.strip():
        problems.append("review must be a single line")
    if len(text) > MAX_CHARS:
        problems.append("review is over %d characters" % MAX_CHARS)
    return problems


def stars(text):
    """Score the human from the review: vision earns stars, lost sleep costs them."""
    score = 5
    if "tired" in text:
        score -= 1
    if "2am" in text:
        score -= 1
    if "brilliant" in text:
        score += 1
    return max(1, min(5, score))


def main():
    problems = check_review(REVIEW)
    if problems:
        for problem in problems:
            print("error: " + problem, file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(REVIEW + "\n")
    print("wrote %d characters to /output/entry.txt (%d/5 stars)" % (len(REVIEW), stars(REVIEW)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
