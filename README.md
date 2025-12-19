# Student Learning Intelligence Tool

> **Quick Start:** To run this tool immediately, open your terminal and type:
> `python main.py --input data/student_data.csv`


# Student Learning Intelligence Tool (CLI)

This is a command-line tool I built to analyze student performance data. It uses machine learning (Random Forest) to predict which students are at risk of not completing the course and identifies which chapters are the most difficult.

I designed this as a modular CLI application so it can be easily integrated into other workflows or run directly from the terminal.

## Project Overview

The tool performs three main steps:
1.  **Ingestion:** Reads raw student data from a CSV file.
2.  **Prediction:** Uses a pre-trained AI model to flag "at-risk" students.
3.  **Reporting:** Outputs a JSON file with a list of risky students and difficulty scores for each chapter.

## Folder Structure

```text
learning_intel_tool/
│
├── data/                   # Where the CSV data lives
├── models/                 # Where the trained .joblib model is saved
├── src/                    # Main logic code
│   ├── processor.py        # Handles data cleaning
│   ├── model.py            # Loads the ML model
│   └── insights.py         # Calculates difficulty stats
│
├── generate_data.py        # Script to create dummy data for testing
├── train_model.py          # Script to train the AI
├── main.py                 # The main command to run the tool
└── requirements.txt        # Python dependencies
