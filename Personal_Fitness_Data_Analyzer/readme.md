# Personal Fitness Data Analyzer

This project analyzes personal fitness data (steps, distance, sleep, workout, and calories) and generates a **detailed fitness report** in plain text (`report.txt`).  
The report summarizes **daily, weekly, and monthly averages**, highlights the **best and worst days**, and provides insights into overall fitness trends.


## Features

1. **Reads fitness data** from a CSV file (`example_data.csv`).
2. **Calculates a normalized fitness score** (0–100) for each day based on multiple health metrics.
3. Generates:
   - Daily Averages
   - Weekly Averages
   - Monthly Averages
   - Best & Worst Day Summaries
   - Fitness Trends (Good, Normal, Bad days)
4. Provides a **personalized motivational message** depending on overall performance.
5. Ends with a **fitness quote for encouragement**.


## Input Data

The project expects a CSV file named **`example_data.csv`** with the following columns:

| Column | Description |
|--------|-------------|
| `date` | Date (YYYY-MM-DD) |
| `day` | Day of the week |
| `steps` | Number of steps taken |
| `Distance_km` | Distance walked/run (in kilometers) |
| `Sleep_Duration_hours` | Sleep duration (in hours) |
| `Workout_Duration_minutes` | Workout duration (in minutes) |
| `Calories_Burned` | Calories burned |

**Example Row:**


## Fitness Score Normalization

Each metric is scaled between **0–100**, so all contribute fairly to the final `fitness_score`.

- **Steps:**  
(10,000 steps/day = 100 points)

- **Distance Walked (km):**  
(5 km/day = 100 points)

- **Sleep Duration (hours):**  
(8 hours = 100 points)

- **Workout Duration (minutes):**  
(1 hour workout = 100 points)

- **Calories Burned:**  
(2500 kcal/day = 100 points)

Finally, the **overall fitness score** is the average of all 5 normalized scores.


## Report Sections

- **Summary (Daily Averages)**
- **Weekly Averages**
- **Monthly Averages**
- **Best & Worst Day** (highest & lowest fitness score)
- **Trends** (Good, Normal, Bad days count)
- **Motivational message + quote**


## Insights

- **Good Days:** Fitness score > 80  
- **Normal Days:** Fitness score between 50 and 80  
- **Bad Days:** Fitness score ≤ 50  

Motivational messages are generated depending on the ratios of good, normal, and bad days.


## How to Run

1. Place your dataset in the project folder as `example_data.csv`.
2. Run the script:
   ```bash
   python main.py
3. The output will be saved as
   ```bash
   report.txt
