# CO₂ Emissions Data Processing System

Python project for reading, validating, organizing, and filtering real-world CO₂ emissions data using custom linked-list data structures and recursive algorithms.

## Features

- Reads emissions data from CSV files and validates the expected file structure
- Converts raw CSV values into structured Python dataclass objects
- Handles missing emissions data using `None`
- Builds an immutable linked list recursively
- Counts linked-list entries using recursive traversal
- Filters emissions data by country and numeric fields
- Supports equality, less-than, and greater-than comparisons
- Preserves filtered results in a new linked-list structure

## Technologies Used

- Python
- Dataclasses
- CSV Processing
- Recursion
- Linked Lists
- Type Hints
- Unit Testing

## Project Structure

```text
co2-emissions-data-processing/
├── emissions.py
├── test_emissions.py
├── sample.csv
├── README.md
└── .gitignore
