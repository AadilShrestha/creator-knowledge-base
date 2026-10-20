# Start here: your Mac setup

Your job is to turn two Evolve course folders into detailed, linked course knowledge in our shared wiki. Claude Code does the file work. You do browser logins, approve the tools you want installed, and spot-check the notes. You need a Claude account with Claude Code access; local Whisper transcription does not require a paid transcription API.

## 1. Get access

Create/sign in to your own GitHub account at https://github.com. Send your username to the repository owner so they can invite you to the **private** repository. Accept the invitation before cloning. A 404 from the link usually means you are signed into the wrong account or have not accepted access.

The repo is: https://github.com/AadilShrestha/creator-knowledge-base

`main` is the shared baseline. `contrib/friend-creators` is your work branch. A branch is your version of the files; a pull request lets the owner review and merge that version later.

## 2. Install the basics once

Open **Terminal** with Spotlight (`Command + Space`, type Terminal). Paste commands one block at a time. Let each finish; if a command fails, stop that block and show the error to Claude after Claude is installed.

If Homebrew is not installed, use the installer shown at https://brew.sh. Follow its final **Next steps** to add Homebrew to your shell. macOS may request Command Line Tools or your computer password; type the password into Terminal, not into a chat.

```bash
brew --version
brew install git gh ffmpeg python@3.11 pipx
brew install --cask claude-code
claude --version
ffmpeg -version
```

Sign in to GitHub using your own account:

```bash
gh auth login
gh auth setup-git
```

Choose GitHub.com, HTTPS, and browser login when prompted. Configure the name and email you want on your commits, replacing both quoted examples. GitHub Settings → Emails shows your private `noreply` email if you prefer that.

```bash
git config --global user.name "Your Name"
git config --global user.email "YOUR_GITHUB_COMMIT_EMAIL"
```

## 3. Clone and open your branch

```bash
mkdir -p ~/Projects
cd ~/Projects
gh repo clone AadilShrestha/creator-knowledge-base
cd creator-knowledge-base
git switch --track origin/contrib/friend-creators
git status --short --branch
claude
```

If the branch already exists locally, run `git switch contrib/friend-creators` instead of creating it again. On Claude's first launch, complete the browser login. Use ordinary permission prompts; give Claude access to this project folder. Now paste the contents of `handoff/FRIEND-PROMPT.md` into Claude Code. The prompt is for Claude, not a shell command.

## 4. Download the two source folders

Install the official MEGA desktop app from https://mega.io/desktop, or use the browser's download option if it works. Open the two links in `handoff/FRIEND-PROMPT.md` and download their complete contents. Preserve filenames and subfolders.

Claude should prepare these destinations and help you place each download in the right one:

```text
knowledge-base/raw/evolve/copywriting/originals/
knowledge-base/raw/evolve/start-here/originals/
```

They contain about **9.2 GB in total**, before extraction, images, model downloads, and temporary files. Start with at least **25 GB free**, then have Claude check actual space. MEGA transfer quotas can pause downloads; let the app report the wait and record the blocker. Do not repeatedly restart a whole download. Confirm file counts against the manifests; a completed-looking folder is not enough.

## 5. Local transcription on your Mac

Claude can perform these project-local setup commands after you paste the prompt. They are shown here so you know what it is doing. Use the Homebrew Python rather than installing packages into Apple's system Python:

```bash
"$(brew --prefix python@3.11)/bin/python3.11" -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pymupdf python-docx beautifulsoup4 lxml openpyxl python-pptx
uname -m
```

- **M1/M2/M3/M4 or newer Apple Silicon:** `uname -m` should say `arm64`. Run `python -m pip install mlx-whisper`. Claude uses `--backend mlx` and initially tests a short clip. The default MLX model is large; on a low-memory Mac, use `--model mlx-community/whisper-small-mlx` for a pilot and review quality. Run a native Terminal if you accidentally see `x86_64` through Rosetta.
- **Intel Mac:** `uname -m` says `x86_64`. Run `python -m pip install faster-whisper`. Claude uses `--backend cpu --model small`. CPU transcription can be slow; process one recording at a time and review accuracy before accepting the smaller model.

The portable command is:

```bash
python tools/kb/transcribe.py --help
```

For one video, Claude should extract mono 16 kHz audio with FFmpeg, then call the helper with the input path and an output prefix under that course's `_transcripts/`. It creates timestamped `.txt`, `.srt`, and `.json` files. It skips a complete existing output set; use `--overwrite` only when deliberately regenerating it. The first run downloads model weights. Originals stay intact. The old Windows `_tools/transcribe.py` uses NVIDIA CUDA and is not the Mac workflow.

Keep the Mac plugged in. `caffeinate -i` in a second Terminal can prevent idle sleep while a batch runs; stop it with `Control + C` when finished. Closing Claude or hitting its usage limit stops agent progress; resume with the saved progress files.

## 6. Agent Reach

Agent Reach is for reading websites and documentation; MEGA download and local transcription use other tools. Install the CLI in its own environment:

```bash
pipx ensurepath
pipx install https://github.com/Panniantong/agent-reach/archive/main.zip
```

Open a new Terminal after `ensurepath` if the command is not found, return to the repo, then run:

```bash
agent-reach install --env=auto
agent-reach doctor
```

The first command checks available tools. Ask Claude to read the [current installation guide](https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md) and configure its Claude skill if not already installed. Keep Agent Reach tools/config under `~/.agent-reach/`. Install optional channels only when a source needs them; the course job does not require setting up every social network.

## 7. Work, resume, and send it back

Claude should show a small sample lesson before processing the remaining batches. Ask for adjustments in normal language. Its course `PROGRESS.md` files show exact progress and blockers.

To resume later:

```bash
cd ~/Projects/creator-knowledge-base
git switch contrib/friend-creators
source .venv/bin/activate
claude
```

Then paste:

> Read CLAUDE.md, AGENTS.md, and handoff/FRIEND-PROMPT.md. Resume the Evolve assignment from both course PROGRESS.md files and manifests. Verify the previous checkpoint, then process the next pending batch. Save and commit progress before stopping.

When ready, tell Claude:

> Validate my Evolve contribution, show me the coverage and any blockers, commit only my course notes/evidence/images, push contrib/friend-creators, and open a pull request against main. Leave merging to the owner. Read handoff/OWNER-GITHUB.md for the handoff requirements.

Raw video/audio and original documents remain local. Git shares derived text evidence and selected screenshots, so the owner can review the notes. For an original needed during review, send its original MEGA relative path; avoid uploading gigabytes to GitHub or Discord.

Checked against official [Claude setup](https://code.claude.com/docs/en/setup), [MLX Whisper](https://github.com/ml-explore/mlx-examples/tree/main/whisper), [faster-whisper](https://github.com/SYSTRAN/faster-whisper), and Agent Reach documentation on 2026-10-20. Commands may change; inspect errors rather than guessing replacements.
