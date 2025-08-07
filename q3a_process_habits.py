import json
from collections import defaultdict

# Load your habit tracker file (make sure it's in the same folder as this script)
with open(r"C:\Users\prava\Downloads\habit_tracker_simulation_5users_30days.json", "r") as f:
    logs = json.load(f)

# Prepare a nested dictionary to store stats per user per habit
user_data = defaultdict(lambda: defaultdict(lambda: {"days_completed": 0, "days_skipped": 0}))

# Process the data
for entry in logs:
    user = entry["user"]
    for habit_entry in entry["daily_log"]:
        habit = habit_entry["habit"]
        if habit_entry["completed"]:
            user_data[user][habit]["days_completed"] += 1
        else:
            user_data[user][habit]["days_skipped"] += 1

# Calculate success rate and store final result
final_result = {}
for user, habits in user_data.items():
    final_result[user] = {}
    for habit, counts in habits.items():
        total = counts["days_completed"] + counts["days_skipped"]
        success_rate = (counts["days_completed"] / total) * 100 if total > 0 else 0
        final_result[user][habit] = {
            "days_completed": counts["days_completed"],
            "days_skipped": counts["days_skipped"],
            "success_rate": round(success_rate, 2)
        }

output_path = r"C:\Users\prava\Downloads\q3a_habit_summary.json"
with open(output_path, "w") as out_file:
    json.dump(final_result, out_file, indent=2)

print(f"✅ Habit summary saved at: {output_path}")

# Write output to a new JSON file
with open("q3a_habit_summary.json", "w") as out_file:
    json.dump(final_result, out_file, indent=2)

print("✅ Habit summary saved as q3a_habit_summary.json")
