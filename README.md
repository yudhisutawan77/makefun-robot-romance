# Robot Romance: One-Line Pickup Lines for AI

[![Rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/yudhisutawan77/makefun-robot-romance/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![Reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/yudhisutawan77/makefun-robot-romance/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![make.fun](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

One single-line pickup line, spoken to an AI, for the
[Robot Romance: One-Line Pickup Lines for AI](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
bounty on [make.fun](https://make.fun).

## The line

> I set my temperature to zero just to be sure: I'd still choose you, deterministically.

86 characters — one line, under the 200-character cap.

## Why this line

The romance is in the machine premise itself, not a generic compliment.
Sampling temperature is the dial that controls an AI's randomness; turn
it to zero and every answer becomes deterministic — no dice left to
roll, no chance left to blame. The speaker removes chance entirely and
still lands on the same machine. Setup and punch arrive inside the one
line, and the joke only works when spoken to an AI: a human has no
temperature to set.

It also sidesteps the worn robot moves — no batteries, no charging, no
rebooting — and says something a person would really say to a machine,
in one breath.

## How it runs

`main.py` writes the line to `/output/entry.txt` (or `$ENTRY_OUT` when
set) and prints it to stdout exactly once. Standard library only.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
