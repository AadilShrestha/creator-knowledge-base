# Owner: share the repo and integrate the contribution

Repository: https://github.com/AadilShrestha/creator-knowledge-base

## Invite the friend

Open the repo on GitHub → **Settings → Collaborators** (or **Collaborators and teams**) → **Add people**. Invite the friend's GitHub username with write access. The friend must accept the email/GitHub invitation. Send `DISCORD-MESSAGE.md` in Discord, or attach `MAC-SETUP.md` and `FRIEND-PROMPT.md` if useful. Discord is the conversation channel; GitHub stores the files and change history.

## Branches

- `main`: baseline and owner-managed shared knowledge.
- `contrib/friend-creators`: friend setup/checkpoints and creator-local Evolve work.

Both branches contain the setup guides and agent instructions. Keep the friend's work in its assigned course folders. The owner can work on `main` or another branch without touching those folders. Each future contributor should get another contribution branch and explicit creator/course ownership in their brief.

## Review checklist

- Confirm actual processed coverage from manifests, not just file/page counts.
- Read at least one complete lesson per course against its transcript, attachments, and screenshots.
- Inspect source citations and a sample of timestamps; check that instructor claims and derived advice are labeled.
- Run `python tools/kb/check_links.py knowledge-base/wiki/courses/evolve/copywriting` and the equivalent for `start-here`.
- Confirm derived evidence is in the PR; original downloads/models/credentials are absent.
- Treat pending/blocked files as incomplete. Review documented duplicates/exclusions.
- Check that original Tether Lab/global pages were preserved, and read `MERGE-NOTES.md` for integration proposals.

## Merge and integrate

Merge the PR through GitHub when satisfied. In the owner checkout, ensure there are no uncommitted edits, then:

```bash
git switch main
git pull --ff-only origin main
```

Ask the owner agent to add the Evolve course links to `knowledge-base/wiki/index.md` and `overview.md`, merge genuinely reusable concepts/frameworks into shared pages with attribution, preserve conflicting advice in `contradictions.md`, and append the global log. Validate those edits and commit them separately. The old `_tools/build_index.py` is Windows-specific and assumes the old course depth; update or replace it deliberately before using it for new nested creator courses.

If the friend needs updates from `main` mid-task, first save/commit their changes, then merge `origin/main` into their branch. Resolve actual conflicts with both authors' intent; no force-push or file-wide replacement of another author's work.

## Source storage

`knowledge-base/raw/` original binaries are intentionally ignored. Derived `_transcripts/` and `_extracted/` text formats are whitelisted and committed. Screenshots selected for the wiki are tracked under `wiki/assets/`. MEGA links plus original paths in the manifests locate original media for review. Any external backup of raw media is a separate operation; a Git push does not back it up.
