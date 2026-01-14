# Textoggle – Grid-Based Word Game Engine (Python)

## Overview
This project implements the core game logic for a grid-based word game inspired by Boggle and Textris.
Words are formed by selecting adjacent letters on an n × n board, with support for scoring, board updates,
and an optional AI agent that plays optimally.

## Features
- Grid-based board representation using 2D lists
- Scrabble-style letter scoring
- Word existence checking (with and without adjacency constraints)
- Board update mechanics with gravity and spare letters
- Optional AI agent for optimal gameplay

## Concepts Demonstrated
- 2D data structures and traversal
- Constraint-based logic
- State transitions without mutating input
- Greedy search and scoring strategies
- Clean functional decomposition

## How to Run
```bash
python main.py
