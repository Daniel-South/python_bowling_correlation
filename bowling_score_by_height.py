"""
bowling_score_by_height.py
Daniel South
2026-02-26

A math professor intuits that there is a positive correlation between the height
of bowlers in his bowling league and their high scores, i.e. he believes that
taller bowlers tend to have higher scores. He wants to test the hypothesis
because he has noticed that tallest bowlers in the league typically do not
bowl the highest scores.

At a league event, the professor notes the height and the high score of each
participant and calculates the correlation and covariance between these
two metrics.

Correlation is scaled on a range from -1 to 1. A positive correlation
will confirm the professor's intuition that taller bowlers have higher scores.

A negative correlation will confirm the opposite, i.e. that the professor
is wrong, and taller bowlers actually have lower scores.

A correlation near zero would indicate that there is no correlation between
height and bowling score.

Is the professor correct?
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


height_inches   = [60,  61, 62,  63,  64,  65,  65,  66,  67,  70,  68,  71,  73,  72,  72,  69,  76,  74,  75,  70]
high_bowl_score = [79, 116, 75, 171, 199, 111, 165, 242, 148, 217, 199, 240, 236, 270, 175, 292, 191, 288, 220, 183]

d = {"height_inches": height_inches, "high_bowling_score" : high_bowl_score}
df = pd.DataFrame(d)

print("The Bowling League")
print(df)

print("\nScatter Plot")

# Visualize the data with a scatter plot
plt.scatter(height_inches, high_bowl_score)
plt.xlabel("Height In Inches")
plt.ylabel("Bowling Score")
plt.show()


print("--\n")

# Calculation the correlation and covariance
correlation_matrix = df.corr()
correlation_matrix
correlation = correlation_matrix.loc['height_inches', 'high_bowling_score']
print("Correlation of Height to Bowling Score:", round(correlation, 4))

cov_matrix = np.cov(height_inches, high_bowl_score)
print("Covariance:", round(cov_matrix[0][1], 2))

print("\nAdditional Statistics")
df.describe()
