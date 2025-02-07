import os
import matplotlib.pyplot as plt
import numpy as np

# Define tasks
tasks = [
    "Define Research Objectives",
    "Literature Review",
    "Data Collection",
    "Data Analysis",
    "Model Development",
    "Experiments",
    "Writing",
    "Proofreading",
    "Submission",
    "Defense Preparation",
]

# Define the schedule (1 = active, 0 = not active)
schedule = [
    [1, 0, 0, 0, 0],  # Define Research Objectives
    [1, 0, 0, 0, 0],  # Literature Review
    [0, 1, 0, 0, 0],  # Data Collection
    [0, 1, 0, 0, 0],  # Data Analysis
    [0, 0, 1, 0, 0],  # Model Development
    [0, 0, 1, 0, 0],  # Experiments
    [0, 0, 0, 1, 0],  # Writing
    [0, 0, 0, 1, 1],  # Proofreading
    [0, 0, 0, 0, 1],  # Submission
    [0, 0, 0, 0, 1],  # Defense Preparation
]

# Find start month and duration for each task
start_months = [next(j for j, val in enumerate(row) if val == 1) for row in schedule]
durations = [sum(row) for row in schedule]

# Reverse lists for better visualization
tasks.reverse()
start_months.reverse()
durations.reverse()

# Define months for plotting
month_labels = ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5"]
month_ticks = np.arange(len(month_labels))

# Create figure
fig, ax = plt.subplots(figsize=(10, 5))

# Plot tasks as horizontal bars
ax.barh(tasks, durations, left=start_months, color="skyblue", edgecolor="black")

# Formatting
ax.set_xlabel("Months")
ax.set_title("Resource-Efficient Embedded Neural Networks")
ax.set_xticks(month_ticks)
ax.set_xticklabels(month_labels)
ax.grid(axis="x", linestyle="--", alpha=0.7)

pictures_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Pictures')

if not os.path.exists(pictures_folder):
    os.makedirs(pictures_folder)
file_path = os.path.join(pictures_folder, "Thesis_Gantt_Chart.png")

plt.savefig(file_path, bbox_inches="tight")