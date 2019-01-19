# Loopover Challenge

1. What the heck is the Loopover Challenge?

Given a loopover board, find a (relatively) short sequence of moves needed to solve the board. Considering that it's probably NP-Complete, so the aim of this challenge is optimisation.

2. How do I participate? 

Submit your solutions to spdskatr#1657 (when the challenge actually starts) as a text file, describing a sequence of moves with Programmer Notation.

3. What's this repository? 

Scripts and utilities used either for judging or solving. It currently includes:

```md
- evaluator.py
A Python module that implements Programmer Notation on a Loopover board

- evaluator-oo.py
Like evaluator.py, but exposes the loopover board as a Python class
```

## Programmer Notation Cheatsheet:

```md
# Programmer Notation
0-indexed
  1R0 - Move the top row (row 0) to the right one square
  -1R0 - Move the top row (row 0) to the left one square
  2R0 - Move the top row to the right twice
  -1C2 - Move column 2 (third from the left) downwards one square
  1R1' Move row 1 from the bottom (second from the bottom) to the right one square
```

*Credits for original puzzle go to carykh* <3
