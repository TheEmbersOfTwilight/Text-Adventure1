# Warden's Sanctum

A short text-adventure about escape, discovery, and a mysterious sanctum.

Overview
--------
Warden's Sanctum is a compact Python text adventure in which you awaken in a grimy cell, discover a mysterious wand, and are swept into the sanctum of a powerful and suspicious figure. The game focuses on exploration, simple inventory flags, atmosphere created by a typed-text effect, and branching choices that change the outcome.

This repository contains the game code (Python) and the story/prose currently embedded in the code.

Quick facts
-----------
- Project name: Warden's Sanctum
- Language: Python
- Status: Prototype / early demo
- Intended distribution: Free to play and edit; non-commercial restriction on assets and prose

Requirements
------------
- Python 3.8+ (standard library only)
- No external packages required

How to play
-----------
1. Download the latest release of the game
2. Run the .py file:  
     -You can either run it locally through terminal (Python 3.8+ Required) using the prompt `Python file-name.py`, or use an online IDE such as https://trinket.io/ or https://www.online-python.com/

Controls
--------
- When you are presented with options, type the number of your choice and press Enter.

Project structure
-----------------
- TextAdventure.py — main Python game file 
- (future) assets/ — images, audio, or other resources (if/when added)
- README.md — this file
- LICENSE-AGPLv3 — AGPLv3 text for code
- LICENSE-CC-BY-NC-SA-4.0 — CC BY-NC-SA 4.0 text for assets/prose
- LICENSES.md — mapping file explaining which parts of the repo are under which license

Contributing
------------
- Contributions welcome! If you plan a small change (bugfix, typo, small refactor), open a pull request.
- For larger changes (new chapters, design changes), please open an issue first to discuss scope and compatibility.
- By contributing code you agree to license your contributions under AGPL-3.0 for code and CC BY-NC-SA 4.0 for creative content included in your contributions (this should be formalized in CONTRIBUTING.md).

Support / Contact
-----------------
Author / maintainer: TheEmbersOfTwilight  
Repo: https://github.com/TheEmbersOfTwilight/Text-Adventure1

Acknowledgements
----------------
- This project started as a small Python prototype with an emphasis on atmosphere and branching choices.

Changelog / Roadmap
-------------------
- v0.1.0 — Prototype: single-file Python demo with simple item flags and branching.
- Planned:
  - Add save/load
  - Add accessibility flags (skip typing effects)
