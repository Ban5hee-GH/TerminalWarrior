# CLI Linux Lab (FileSystem-CTF)
A Dockersized command-line cybersecurity challenge built in Python, simulating a Linux terminal environment where you solve hacking-style puzzles using real Linux commands.

## Overview
CLI Linux lab is an interactive command-line game where players explore a simulated Linux filesystem to uncover hidden flags, passwords, and secrets using common terminal commands. Designed for cybersecurity beginner and ethical hacking enthusiasts, it provides a safe and educational environment to practice Linux fundamentals, command syntax, and problem-solving-skills -- all inside a self-contained Docker container.

## Features
- Linux-Style terminal environment built entirely in Python.
- Multiple levels of increasing difficulty.
- Realistic Linux Commands like ('ls', 'cat', 'cd', 'ssh', 'whoami', 'pwd' etc.)
- Progress tracking and challenge checklist.
- Full self-contained Docker setup (no installs required).
- Cross-platform - works on Windows, macOS, and Linux.

## Levels Overview
- |1| Intro Challenge | Explore directories and find hidden files | Basic Linux commands ('ls', 'cat', 'cd', 'pwd', 'whoami') |
- |2| Permissions & Ownership *(COMING SOON)* | Learn how to view and modify file permissions | 'chmod', 'chown', 'sudo', file modes |
- |3| Searching the system *(CMOING SOON)* | Find hidden files and analyze logs | 'grep', 'find', 'less', 'head', 'tail' |
- |4| Networking Challenge *(COMING SOON)* | Discover hosts and services | 'ping', 'netcat', 'curl', 'ssh' |
- |5| Cryptography & Decoding *(COMING SOON)* | Decode hidden messages and hash files | base64, hashing, simple ciphers |

## Setup & Usage

### Run Locally (No Docker)
---bash
- Step 1: git clone https://github.com/Ban5hee-GH/FileSystem-CTF.git
- Step 2: cd FileSystem-CTF
- Step 3: pip install -r requirements.txt
- step 4: python -m cli_lab.main

### Run With Docker (Recommended)
- Step 1: docker build -t cli-lab -f docker/Dockerfile .
- Step 2: docker run -it cli-lab

## Learning Outcomes
- Practice Linux terminal commands in a safe enviornment.
- Learn basic file systems navigation and command syntax.
- Understand SSH authentication basics.
- Improve problem-solving and cybersecurity investigation workflow.
- Build confidence with ethical hacking CTF-style challenges.
