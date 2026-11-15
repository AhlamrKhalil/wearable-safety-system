from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# paths are based on the script location, so it runs from any folder
repo_folder = Path(__file__).resolve().parents[2]
csv_file = repo_folder / "src" / "sense_hat" / "sensor_test_01.csv"
output_file = repo_folder / "docs" / "images" / "sensor_test_01_accel.png"

# same labels as in sensor_data.py
movements = [
    "No movement",
    "Side to side movement",
    "Forward and backward movement"
]

data = pd.read_csv(csv_file, parse_dates=["timestamp"])

fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharey=True)

for ax, movement in zip(axes, movements):
    rows = data[data["movement"] == movement]

    # seconds from the start of each recording
    seconds = (rows["timestamp"] - rows["timestamp"].iloc[0]).dt.total_seconds()

    ax.plot(seconds, rows["accel_x"], label="X")
    ax.plot(seconds, rows["accel_y"], label="Y")
    ax.plot(seconds, rows["accel_z"], label="Z")

    ax.set_title(movement)
    ax.set_xlabel("Time (s)")
    ax.grid(True)

axes[0].set_ylabel("Acceleration (g)")
axes[0].legend()

fig.suptitle("Accelerometer Readings sensor_test1.csv")
fig.tight_layout()

# save before show(), otherwise the saved image can be blank
output_file.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output_file, dpi=150)
print("Graph saved to:", output_file)

plt.show()