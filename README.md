# Data-Structure-Unit-4-Case-Study-
 Dictionary Application using Hash Tables, Description: Implement a dictionary where words and meanings are stored and retrieved using hashing with collision resolution

# Dictionary Application Using Hash Tables

A Python case study for Unit 4: Hashing. This program stores word–meaning pairs in a hash table and supports adding, searching, updating, removing, and displaying dictionary entries.

## Collision Resolution

The program uses **separate chaining**. Each hash table bucket contains a list of entries, so multiple words that map to the same bucket can be stored together.

The example uses a table capacity of 5 and a simple hash function based on the sum of the character codes. The words `listen` and `silent` map to the same bucket, demonstrating collision handling.

## Features

- Add a word and its meaning.
- Search for a word.
- Update a word's meaning.
- Remove a word.
- Display all stored entries.
- Handle word matching without regard to capitalization.

## Requirements

- Python 3.7 or newer
- No external packages required

## How to Run

Open a terminal in this folder and run:

```bash
python CaseStudy4.py
```

If your system uses `python3`, run:

```bash
python3 CaseStudy4.py
```

## Sample Output

See [`sample_output.txt`](sample_output.txt) for the output produced by the example program.

## Complexity

Let `n` be the number of stored words and `m` the number of entries in a bucket:

- Hashing a word takes **O(k)**, where `k` is the word length.
- Add, search, and remove take **O(1)** on average when entries are distributed across buckets.
- In the worst case, when many words collide, these operations can take **O(n)**.
- The table uses **O(n + capacity)** space.

## Files

- `CaseStudy4.py` — Hash table dictionary implementation and demonstration.
- `README.md` — Project overview and instructions.
- `sample_output.txt` — Example output from the program.