import pandas as pd
df = pd.read_csv("example_data.csv")
df['date']=pd.to_datetime(df['date'])
df['step_score'] = (df['steps']/10000).clip(upper=1)*100
df['kms_walked_score'] = (df['Distance_km']/5).clip(upper=1)*100
df['sleep_score'] = (df['Sleep_Duration_hours']/8).clip(upper=1)*100
df['workout_score'] = (df['Workout_Duration_minutes']/60).clip(upper=1)*100
df['calorie_score'] = (df['Calories_Burned']/2500).clip(upper=1)*100
df['fitness_score'] = (df['step_score']+df['kms_walked_score']+df['sleep_score']+df['workout_score']+df['calorie_score'])/5
df["month"] = df["date"].dt.month_name()
df["week"] = df["date"].dt.isocalendar().week
monthly_avg = df.groupby("month").mean(numeric_only=True)
weekly_avg = df.groupby("week").mean(numeric_only=True)
best = df.loc[df['fitness_score'].idxmax()]
worst = df.loc[df['fitness_score'].idxmin()]
bad = df.loc[df['fitness_score']<=50].shape[0]
good = df.loc[df['fitness_score']>80].shape[0]
normal = df.loc[(df['fitness_score'] > 50) & (df['fitness_score'] <= 80)].shape[0]
report_period = f"{df['date'].min().date()} - {df['date'].max().date()}"
with open("report.txt", "w", encoding="utf-8") as f:
    f.write(
        f"PERSONAL FITNESS REPORT\n\n"
        f"Report Period -> {report_period}\n\n"
        f"Summary:-> \nDaily Averages\n"
        f"Average Steps/day: {df['steps'].mean():.0f}\n"
        f"Average Distance/day: {df['Distance_km'].mean():.2f} km\n"
        f"Average Sleep Duration/day: {df['Sleep_Duration_hours'].mean():.2f} hrs\n"
        f"Average Workout Duration/day: {(df['Workout_Duration_minutes']/60).mean():.2f} hrs\n"
        f"Average Calories Burned/day: {df['Calories_Burned'].mean():.0f} kcal\n"
        f"Overall Fitness Score/day: {df['fitness_score'].mean():.2f} / 100\n\n"
    )
    f.write(f"Weekly Averages\n")
    for week, row in weekly_avg.iterrows():
        f.write(
            f"Week {week} -> Steps: {row['steps']:.0f}, "
            f"Distance: {row['Distance_km']:.2f} km, "
            f"Sleep: {row['Sleep_Duration_hours']:.2f} hrs, "
            f"Workout: {(row['Workout_Duration_minutes']/60):.2f} hrs, "
            f"Calories: {row['Calories_Burned']:.0f}, "
            f"Fitness Score: {row['fitness_score']:.2f}\n\n"
        )
    f.write(f"Monthly Averages\n")
    for month, row in monthly_avg.iterrows():
        f.write(
            f"Month {month} -> Steps: {row['steps']:.0f}, "
            f"Distance: {row['Distance_km']:.2f} km, "
            f"Sleep: {row['Sleep_Duration_hours']:.2f} hrs, "
            f"Workout: {(row['Workout_Duration_minutes']/60):.2f} hrs, "
            f"Calories: {row['Calories_Burned']:.0f}, "
            f"Fitness Score: {row['fitness_score']:.2f}\n\n"
        )
    f.write(
        f"Best Day :-\n"
        f"Date {best['date'].date()} -> Steps: {best['steps']}, "
        f"Distance: {best['Distance_km']:.2f} km, "
        f"Sleep: {best['Sleep_Duration_hours']:.2f} hrs, "
        f"Workout: {(best['Workout_Duration_minutes']/60):.2f} hrs, "
        f"Calories: {best['Calories_Burned']}, "
        f"Fitness Score: {best['fitness_score']:.2f}\n\n"
    )

    f.write(
        f"Worst Day :-\n"
        f"Date {worst['date'].date()} -> Steps: {worst['steps']}, "
        f"Distance: {worst['Distance_km']:.2f} km, "
        f"Sleep: {worst['Sleep_Duration_hours']:.2f} hrs, "
        f"Workout: {(worst['Workout_Duration_minutes']/60):.2f} hrs, "
        f"Calories: {worst['Calories_Burned']}, "
        f"Fitness Score: {worst['fitness_score']:.2f}\n\n"
    )
    f.write(
            f"Trends :-\n"
            f"The Total Number Of Good Days where Fitness Score Is Above 80 -> {good}\n"
            f"The Total Number Of Normal Days where Fitness Score Is Above 50 But Less Than or eqaul to 80 -> {normal}\n"
            f"The Total Number Of Bad Days where Fitness Score Is below or equal to 50 -> {bad}\n\n"
    )
    total_days=good+bad+normal
    if ((good/total_days)*100>=65 and (normal/total_days)*100>=20):
        f.write("Excellent work! 🎉 You’re maintaining a strong fitness routine. Keep pushing your limits and stay consistent!")
    elif (((good/total_days)*100>=25 and (normal/total_days)*100>=50)):
        f.write("Good job! 👍 You’re on the right track, but there’s room for improvement. Try adding a bit more activity or better sleep to boost your fitness.")
    else:
        f.write("Your fitness levels are quite low ⚠️. Don’t worry — start with small daily steps like walking more, regular workouts, and proper rest. Progress will follow!")
    
    f.write('\n\n\n"Take care of your body. It’s the only place you have to live." – Jim Rohn')
