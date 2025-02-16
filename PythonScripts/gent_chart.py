import os
import datetime
import matplotlib.pyplot as plt
import numpy as np

# Define tasks
tasks = [
    "Define Research Objectives",
    "Literature Review",
    "Goal Setting"  ,
    "Basic Model Development (Milestone 1)",
    "Basic Experiments",
    "Writing",
    "Advanced Model Development (Milestone 2)",
    "Advanced Experiments",
    "Submission",
    "Defense Preparation",
]


start_date = datetime.date(2025, 1, 27)
end_date = datetime.date(2025, 6, 27)

num_intervals = (end_date - start_date).days // 14 + 2

week_labels = [(start_date + datetime.timedelta(weeks=2 * i)).strftime('%b %d') for i in range(num_intervals)] # 11 (2-weeks)
week_labels[-1] = "Jun 27"

schedule = [
    [1,1] + [0] * (num_intervals - 1),  # Define Research Objectives
    [1,1,1] + [0] * (num_intervals - 1),  # Literature Review
    [1,1] + [0] * (num_intervals - 1),  # Goal Setting
    [0, 0, 1 ,1] + [0] * (num_intervals - 2),  # Model Development
    [0, 0, 0 , 0, 1] + [0] * (num_intervals - 3),  # Experiments
    [0] * (num_intervals - 5) + [1] * 4,  # Writing
    [0] * (num_intervals - 7) + [1] * 2 ,  # Advanced Model Development (Milestone 2)
    [0] * (num_intervals - 5) + [1] * 2, # Advanced Experiments
    [0] * (num_intervals -2) + [1],  # Submission
    [0] * (num_intervals -2) + [1],  # Defense Preparation
]

# Reverse lists for better visualization
tasks.reverse()
schedule.reverse()

# Find start week and duration for each task
start_weeks = [next(j for j, val in enumerate(row) if val == 1) for row in schedule]
durations = [sum(row) for row in schedule]

# Create figure
fig, ax = plt.subplots(figsize=(12, 6))

# Plot tasks as horizontal bars
y_positions = np.arange(len(tasks))
for i, (start, duration) in enumerate(zip(start_weeks, durations)):
    ax.barh(y_positions[i], duration, left=start, color="skyblue", edgecolor="black")

# Formatting
ax.set_yticks(y_positions)
ax.set_yticklabels(tasks)
ax.set_xticks(np.arange(len(week_labels)))
ax.set_xticklabels(week_labels, rotation=45)
ax.set_xlabel("Timeline (2-week intervals)")
ax.set_title("Resource-Efficient Embedded Neural Networks")
ax.grid(axis="x", linestyle="--", alpha=0.7)

# Save chart in the Pictures folder
pictures_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Pictures")
if not os.path.exists(pictures_folder):
    os.makedirs(pictures_folder)

file_path = os.path.join(pictures_folder, "Thesis_Gantt_Chart.png")
plt.savefig(file_path, bbox_inches="tight")
