import numpy as np
import pandas as pd
from plotnine import *

import matplotlib.pyplot as plt

plt.xkcd()

# Generate data points that match the curve pattern
np.random.seed(42)  # for reproducibility

# Create base x values
x_base = np.linspace(0, 10, 100)

# Create a smooth declining curve with some bumps
y_smooth = 10 * np.exp(-0.3 * x_base)  # exponential decay base

# Add some characteristic bumps and variations
bumps = (
    0.8 * np.exp(-((x_base - 1.5) ** 2) / 0.2)  # early bump
    + 0.4 * np.exp(-((x_base - 3.2) ** 2) / 0.3)  # middle bump
    + 0.2 * np.exp(-((x_base - 6.5) ** 2) / 0.4)  # later smaller bump
)

# Combine smooth curve with bumps and add some noise
y_values = y_smooth + bumps + 0.1 * np.random.normal(0, 1, len(x_base))

# Ensure the curve starts high and ends low
y_values = np.maximum(y_values, 0.5)  # minimum value
y_values[0] = 9.5  # ensure high start
y_values[-1] = 0.8  # ensure low end

# Create DataFrame
df = pd.DataFrame({"difficulty": x_base, "performance": y_values})

# Create the plot
plot = (
    ggplot(df, aes(x="difficulty", y="performance"))
    + geom_line(size=2, color="black")
    + labs(
        title="Smooth Capability Curve",
        x="Perceived Difficulty",
        y="Model Performance",
    )
    + scale_x_continuous(
        breaks=[],  # Remove tick marks
        labels=lambda x: [
            "Easy" if i == 0 else "Hard" if i == len(x) - 1 else ""
            for i in range(len(x))
        ],
    )
    + scale_y_continuous(breaks=[])  # Remove y-axis tick marks
    + theme_xkcd()
    + theme(
        plot_title=element_text(size=16, ha="center", margin={"b": 20}),
        axis_title_x=element_text(size=12, margin={"t": 10}),
        axis_title_y=element_text(size=12, angle=90, margin={"r": 10}),
        figure_size=(10, 6),
    )
    # Add custom x-axis labels at the ends
    + annotate("text", x=0.5, y=-0.8, label="Easy", size=12)
    + annotate("text", x=9.5, y=-0.8, label="Hard", size=12)
)

plot
