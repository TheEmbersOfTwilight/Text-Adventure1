# Contributing to Warden's Sanctum

Thank you for your interest in contributing to Warden's Sanctum — your help makes the game better. This document explains how to report issues, propose changes, and what to expect when contributing.

## Quick Start

- Fork the repository and create a feature branch from `main` named `feat/short-description` or `fix/short-description`.
- Make your changes locally, run tests (if present), and ensure code follows the style guidelines below.
- Commit changes with clear messages, push your branch to your fork, and open a pull request (PR) against `TheEmbersOfTwilight/Text-Adventure1:main`.

## Reporting Bugs and Requesting Features

- Use the repository Issues tab to report bugs or request features.
- When opening an issue, include:
  - A descriptive title
  - Steps to reproduce the problem (or a clear description of the feature you want)
  - The Python version you used
  - Any error messages or tracebacks

## Pull Request Guidelines

- For small fixes (typos, minor bug fixes), a single commit PR is fine.
- For larger changes (new chapters, refactors, added systems), open an issue first to discuss the design.
- Keep PRs focused: each PR should address one logical change.
- Add tests if you introduce or change behavior that can be automated.
- Be responsive to review comments and update the PR as requested.

## Branching and Commit Messages

- Branch naming examples:
  - `feat/add-save-system`
  - `fix/input-validation`
  - `chore/update-deps`
- Commit message style: short summary on the first line (50 chars or less), followed by a blank line and an optional detailed description.

## Code Style and Testing

- Code should target Python 3.8+.
- Follow PEP 8 where practical. Keep the code readable and well-documented.
- If adding significant Python code, consider adding tests under a `tests/` directory.
- If you add external dependencies, include them in a requirements.txt and explain why they are necessary.

## Licensing of Contributions

By submitting a pull request you agree that your contributions will be licensed under the same licenses used in this repository:

- Code contributions (Python files, scripts): AGPL-3.0
- Creative content (story text, prose, images, audio, other assets): CC BY-NC-SA 4.0

If you cannot license your contribution under these terms, please contact the maintainer before submitting.

## Contributor Conduct

Please follow a professional and respectful tone in all conversations. This project recommends adding a `CODE_OF_CONDUCT.md` at the repository root; if one is present, contributors must follow it.

## Small Tasks and Good First Issues

- Label beginner-friendly issues with `good first issue`.
- If you're looking for something to work on, check the issues list and filter by `good first issue`.

## Local Development Tips

- Running the game locally: `python TextAdventure.py` from the repo root.
- If you prefer a faster run for testing, temporarily set delays inside `type_text` to a smaller value or add a flag to skip delays.

## Requesting Commercial Permission

- The project's assets and prose are licensed CC BY-NC-SA 4.0 and are not available for commercial use without permission. To request a commercial license or permission to use the content commercially, contact the repository owner: https://github.com/TheEmbersOfTwilight

## Thank You

Thanks for taking the time to improve Warden's Sanctum — your contributions are appreciated.