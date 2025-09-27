# Personal Fitness Report Generator

This Python script generates a **personal fitness report** based on daily activity data, including steps, distance walked, sleep duration, workouts, and calories burned. The report provides daily, weekly, and monthly averages, highlights the best and worst days, and evaluates overall fitness trends.

---

## Features

- **Data Processing**
  - Reads a CSV dataset from Google Drive.
  - Standardizes column names to lowercase.
  - Converts `date` column to datetime.
  
- **Fitness Metrics Calculation**
  - `step_score`: Based on daily steps (max 100).
  - `kms_walked_score`: Based on daily distance walked (max 100).
  - `sleep_score`: Based on daily sleep duration (max 100).
  - `workout_score`: Based on daily workout duration (max 100).
  - `calorie_score`: Based on daily calories burned (max 100).
  - `fitness_score`: Average of all individual scores (0–100 scale).

- **Additional Features**
  - Extracts `month` and `week` from the date.
  - Computes weekly and monthly averages.
  - Identifies best and worst fitness days.
  - Counts good, normal, and bad fitness days.
  - Generates motivational suggestions based on overall trends.

- **Output**
  - Saves a **detailed report** in `report.txt` including:
    - Daily averages
    - Weekly averages
    - Monthly averages
    - Best and worst day summaries
    - Fitness trends and motivational message

---

## Requirements

- Python 3.x
- `pandas` library

### 1. Install dependencies using pip:

```bash
pip install pandas
```

### 2. Run The Script

```python
python fitness_report.py
```
