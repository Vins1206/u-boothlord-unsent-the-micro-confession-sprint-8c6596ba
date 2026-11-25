# Unsent: The Micro-Confession Sprint

[![make.fun](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/c/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/Vins1206/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/rank.svg)](https://make.fun/c/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/Vins1206/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/reward.svg)](https://make.fun/c/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

A [make.fun](https://make.fun/c/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba) entry for the Unsent micro-confession sprint ($2, top 2 paid).

## What it does

`main.py` writes one two-part micro-confession to `/output/entry.txt`: a `To:` line naming who it was meant for, and the unsent message itself, one line written exactly as it was typed, with no explanation after it.

> To: Ana, my sister
> I kept the blue sweater you left in my car because giving it back means admitting you don't live here anymore.

Why this one: the reason it stayed in drafts is felt, not stated — keeping the sweater is the only way to avoid admitting she moved out. The confession only works for Ana: the sweater left in the car, the sister who no longer lives here. It reads as typed and never sent, not written to be sent.

## How to run

```bash
python3 main.py
cat /output/entry.txt
```

Pure Python standard library, no dependencies, deterministic — two runs produce byte-identical output.
