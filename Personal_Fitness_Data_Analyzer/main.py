import pandas as pd
dataset = "https://drive.google.com/uc?export=download&id=1txZq3x86k7hvF_sXGL_cgW8Fve75cTNv"
df = pd.read_csv(dataset)
df.columns = df.columns.str.strip().str.lower()
df['date']=pd.to_datetime(df['date'])
df['step_score'] = (df['steps']/10000).clip(upper=1)*100
df['kms_walked_score'] = (df['distance_km']/5).clip(upper=1)*100
df['sleep_score'] = (df['sleep_duration_hours']/8).clip(upper=1)*100
df['workout_score'] = (df['workout_duration_minutes']/60).clip(upper=1)*100
df['calorie_score'] = (df['calories_burned']/2500).clip(upper=1)*100
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
with open("report.txt", "w") as f:
    f.write(
        f"PERSONAL FITNESS REPORT\n\n"
        f"Report Period -> {report_period}\n\n"
        f"Summary:-> \nDaily Averages\n"
        f"Average Steps/day: {df['steps'].mean():.0f}\n"
        f"Average Distance/day: {df['distance_km'].mean():.2f} km\n"
        f"Average Sleep Duration/day: {df['sleep_duration_hours'].mean():.2f} hrs\n"
        f"Average Workout Duration/day: {(df['workout_duration_minutes']/60).mean():.2f} hrs\n"
        f"Average Calories Burned/day: {df['calories_burned'].mean():.0f} kcal\n"
        f"Overall Fitness Score/day: {df['fitness_score'].mean():.2f} / 100\n\n"
    )
    f.write(f"Weekly Averages\n")
    for week, row in weekly_avg.iterrows():
        f.write(
            f"Week {week} -> Steps: {row['steps']:.0f}, "
            f"Distance: {row['distance_km']:.2f} km, "
            f"Sleep: {row['sleep_duration_hours']:.2f} hrs, "
            f"Workout: {(row['workout_duration_minutes']/60):.2f} hrs, "
            f"Calories: {row['calories_burned']:.0f}, "
            f"Fitness Score: {row['fitness_score']:.2f}\n\n"
        )
    f.write(f"Monthly Averages\n")
    for month, row in monthly_avg.iterrows():
        f.write(
            f"Month {month} -> Steps: {row['steps']:.0f}, "
            f"Distance: {row['distance_km']:.2f} km, "
            f"Sleep: {row['sleep_duration_hours']:.2f} hrs, "
            f"Workout: {(row['workout_duration_minutes']/60):.2f} hrs, "
            f"Calories: {row['calories_burned']:.0f}, "
            f"Fitness Score: {row['fitness_score']:.2f}\n\n"
        )
    f.write(
        f"Best Day :-\n"
        f"Date {best['date'].date()} -> Steps: {best['steps']}, "
        f"Distance: {best['distance_km']:.2f} km, "
        f"Sleep: {best['sleep_duration_hours']:.2f} hrs, "
        f"Workout: {(best['workout_duration_minutes']/60):.2f} hrs, "
        f"Calories: {best['calories_burned']}, "
        f"Fitness Score: {best['fitness_score']:.2f}\n\n"
    )

    f.write(
        f"Worst Day :-\n"
        f"Date {worst['date'].date()} -> Steps: {worst['steps']}, "
        f"Distance: {worst['distance_km']:.2f} km, "
        f"Sleep: {worst['sleep_duration_hours']:.2f} hrs, "
        f"Workout: {(worst['workout_duration_minutes']/60):.2f} hrs, "
        f"Calories: {worst['calories_burned']}, "
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
print("Your Report Has Been Saved In file report.txt")
