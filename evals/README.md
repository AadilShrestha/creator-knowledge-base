# Evals: does the knowledge base make agents write better?

Fixed test briefs, run before and after every structural change and every new course, so improvements are measured instead of guessed.

## Layout
- `briefs/`: test briefs. Product facts and reviews in them are **fictional test fixtures**; never cite them as evidence in the wiki.
- `runs/<run-name>/NN.md`: an agent's output for brief NN. `baseline` = the knowledge base before the skills existed (snapshot of commit 329e517).
- `runs/<run-name>/review.md`: the blind comparison and checklist scoring for that run.

## How to run
1. Start a fresh agent with no other context. Point it at the repo and give it one brief file: "Do the request in `evals/briefs/NN-....md` using this knowledge base. Write the deliverable to `evals/runs/<run>/NN.md`."
2. Run every brief. Use the same model for each run you compare.
3. Review blind. Label the two outputs A and B (random order), then:
   - score both on `.claude/skills/write-ugc-script/references/checklist.md` (yes/no per item, quoting lines);
   - judge which one you'd actually film, and why.
4. A human makes the final call. AI judges prefer AI-sounding text.

## Add your own briefs
Real products beat fictional ones. Add `briefs/NN-<product>.md` with: the request as you'd normally type it, product facts, offer, audience, what must not be claimed, and 5–20 real customer lines (reviews, comments). Keep at least one deliberately thin brief, since real requests are often one line.
