Textoggle – Grid-Based Word Game Engine (Python):

Textoggle is a grid-based word game engine inspired by games such as Boggle and Scrabble.
The project focuses on implementing the full game logic behind word discovery, scoring, board updates, and an optional AI agent that plays optimally.

This repository contains a clean, modular Python implementation designed to demonstrate algorithmic thinking, data structures, and careful state management.


Project Overview:

In Textoggle, players form words by selecting letters from a 2D grid. Words must obey specific rules depending on the game mode:

Letters may need to be adjacent (horizontal or vertical)

Each letter can be used at most once per word

Blank tiles can substitute for missing letters

Words are scored using Scrabble-style letter values

Playing a word modifies the board using gravity and spare letters

The project progressively builds from simple scoring to a fully playable engine with an AI agent.


Key Features
1. Scrabble-Style Letter Scoring

Implements the official Scrabble point system

Supports blank tiles with zero value

Can score entire boards or individual words

2. Word Validation (Two Modes)

Simplified mode: checks if a word can be formed from available letters and blanks

Adjacency mode: enforces horizontal/vertical adjacency rules

Prevents letter reuse within a single word

3. Pathfinding on a Grid

Maps letters to board coordinates

Verifies valid adjacency paths for words

Returns exact index sequences for valid words

4. Board Update Mechanics

Removes letters after a word is played

Applies gravity so remaining letters fall downward

Refills columns using a finite list of spare letters

Uses # to represent empty cells when spares run out

Ensures the original board is never mutated

5. AI Agent (Bonus Task)

Searches for the highest-scoring valid word each turn

Uses Scrabble scoring multiplied by word length

Resolves ties alphabetically

Continues playing until no valid words remain

Designed for boards up to 4×4 with limited spares

