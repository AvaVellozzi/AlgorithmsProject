# Stable Matching Algorithm

## Overview

This program implements the Gale-Shapley algorithm for stable matching between hospitals and residents using a Priority Queue, as seen in Chapter 2.5 of the textbook. It uses the **priority queue** (implemented using a heap) to manage the list of free hospitals while iterating through the matching process. The input and output files are text-based, where hospitals and residents have preferences, and the goal is to produce stable matches based on these preferences.

The program can handle different sizes of input data to evaluate the performance of the algorithm on varying scales.

## Algorithm

The program uses the **Gale-Shapley algorithm** for stable matching, which involves the following steps:

1. Hospitals propose to residents based on their preferences.
2. Residents either accept or reject the proposals based on their own preferences, potentially switching partners if a more preferred hospital proposes.
3. The process continues until all hospitals are matched with residents.

A **priority queue** is used to manage the free hospitals efficiently by always processing the one with the smallest index, ensuring that the hospital with the highest priority is processed first.

## Data Structures Used

- **Priority Queue (Heap)**: This data structure is used to manage the free hospitals during the matching process, ensuring that hospitals with the smallest indices are processed first.
- **Resident Pairing**: A list where the index represents the resident, and the value represents the hospital they are matched with.
- **Hospital Next Proposal**: A list that tracks which resident a hospital will propose to next.
- **Resident Ranking**: A list of dictionaries where each dictionary maps a hospital to its ranking for that resident. Used to compare which hospital is more preferred by a resident.

## Input and Output Files

### Input File Format (`input.txt`)

The input file contains:

1. The number of hospitals and residents `n`.
2. The hospital preferences list: `n` lines, each containing a space-separated list of integers representing the hospital’s preference order of the residents.
3. The resident preferences list: `n` lines, each containing a space-separated list of integers representing the resident’s preference order of the hospitals.

**Example Input:**
4
1 3 0 2
3 2 0 1
0 1 3 2
2 3 1 0
0 3 1 2
1 2 0 3
2 0 3 1
3 2 1 0

This represents 4 hospitals and 4 residents with their preference lists.

### Output File Format (`output.txt`)

The output file contains the stable matches as pairs of hospital and resident indices. Each line in the output represents a pair in the format `hospital resident`.

**Example Output:**
0 2
1 0
2 3
3 1

This means:

- Hospital 0 is matched with Resident 2.
- Hospital 1 is matched with Resident 0.
- Hospital 2 is matched with Resident 3.
- Hospital 3 is matched with Resident 1.

## How to Run

1. **Extract the ZIP Folder**:
   After extracting the ZIP folder, you will have the following files:
   - `algorithm.py`: The main Python script implementing the algorithm.
   - `README.md`: This README file.

2. **Running the Program**:
   To run the program, follow these steps:

   - Open a terminal or command prompt in the directory where the extracted files are located.
   - Run the Python script by executing the following command: python algorithm.py

   The script will:
   - Generate random input files for different sizes (10, 50, 100, 500, 1000).
   - Run the stable matching algorithm on each input and produce output files (e.g., `output_10.txt`, `output_50.txt`).
   - Print the execution time for each test size.

3. **Input/Output Files**:
   - The input files are generated dynamically for different test sizes and saved in the same directory as the script.
   - The output files will be saved with names like `output_10.txt`, `output_50.txt`, etc., corresponding to the input sizes.

## Example Output in Terminal

Processed size: 10, Time taken: 0.00015 seconds
Processed size: 50, Time taken: 0.00123 seconds
Processed size: 100, Time taken: 0.00456 seconds
Processed size: 500, Time taken: 0.02345 seconds
Processed size: 1000, Time taken: 0.15678 seconds

Summary of Execution Times:
n = 10: 0.00015 sec
n = 50: 0.00123 sec
n = 100: 0.00456 sec
n = 500: 0.02345 sec
n = 1000: 0.15678 sec

## Conclusion

This program demonstrates the Gale-Shapley algorithm for stable matching with hospitals and residents using a Priority Queue, as seen in Chapter 2.5 of the textbook. It is designed to evaluate performance across various input sizes, making it useful for understanding the scalability of the algorithm.
