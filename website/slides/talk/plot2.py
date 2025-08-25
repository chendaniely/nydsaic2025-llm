import numpy as np
import pandas as pd
from plotnine import *
import matplotlib.pyplot as plt

# Generate data points for jagged pattern
np.random.seed(123)  # for reproducibility

# Create x values
x_values = np.linspace(0, 10, 60)

# Create jagged pattern with sharp peaks and valleys, flat overall trend
y_values = []
base_level = 5  # Constant base level - no trend

for i, x in enumerate(x_values):
    # Add sharp spikes at various intervals around the flat base
    if i % 8 == 0 or i % 8 == 1:  # Sharp peaks
        spike = np.random.uniform(2, 4)
        y_values.append(base_level + spike)
    elif i % 8 == 2 or i % 8 == 3:  # Sharp drops
        drop = np.random.uniform(-2, -1)
        y_values.append(max(0.5, base_level + drop))
    elif i % 8 == 4 or i % 8 == 5:  # Medium values
        med = np.random.uniform(-1, 1)
        y_values.append(max(0.5, base_level + med))
    else:  # Low values
        low = np.random.uniform(-1.5, -0.5)
        y_values.append(max(0.5, base_level + low))

# Add some additional randomness for more jagged look
for i in range(len(y_values)):
    if i > 0 and i < len(y_values) - 1:
        # Occasionally create dramatic jumps
        if np.random.random() < 0.2:
            y_values[i] = max(0.5, y_values[i] + np.random.uniform(-2, 3))

# Create some specific tall spikes like in the image, distributed across difficulty levels
spike_positions = [8, 15, 28, 42, 52]
for pos in spike_positions:
    if pos < len(y_values):
        y_values[pos] = np.random.uniform(7, 9)

# Keep both ends at similar levels to maintain flat trend
y_values[0] = np.random.uniform(4, 6)
y_values[-1] = np.random.uniform(1, 3)

# Create DataFrame
df = pd.DataFrame({"difficulty": x_values, "performance": y_values})

# Create the plot
plot = (
    ggplot(df, aes(x="difficulty", y="performance"))
    + geom_line(size=2, color="black")
    + labs(
        title="Jagged Capability Curve",
        x="Perceived Difficulty",
        y="Model Performance",
    )
    + scale_x_continuous(breaks=[])
    + scale_y_continuous(breaks=[])
    + theme_xkcd()
    + theme(
        plot_title=element_text(size=16, ha="center", margin={"b": 20}),
        axis_title_x=element_text(size=12, margin={"t": 10}),
        axis_title_y=element_text(size=12, angle=90, margin={"r": 10}),
        figure_size=(10, 6),
    )
    + annotate("text", x=0.5, y=-0.5, label="Easy", size=12)
    + annotate("text", x=9.5, y=-0.5, label="Hard", size=12)
)

plot
