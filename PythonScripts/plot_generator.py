import matplotlib.pyplot as plt
import numpy as np
import os

# Create figures directory if it doesn't exist
os.makedirs("Pictures", exist_ok=True)

# Generate and save multiple figures
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# First plot
plt.figure(figsize=(6, 4))
plt.plot(x, y1, label="Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sine Function")
plt.legend()
plt.savefig("Pictures/sine_plot.png", dpi=300)
plt.close()

# Second plot
plt.figure(figsize=(6, 4))
plt.plot(x, y2, label="Cosine Wave", color="red")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Cosine Function")
plt.legend()
plt.savefig("Pictures/cosine_plot.png", dpi=300)
plt.close()

print("Plots generated successfully!")
