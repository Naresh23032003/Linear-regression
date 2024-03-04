import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
import seaborn as sns

# Load the California Housing dataset
housing = fetch_california_housing()

# Limit the data to the first 500 data points
X = np.array(housing.data[:500, 0])  # Median income in block group (feature)
y = np.array(housing.target[:500])   # Median house value for California districts,expressed in $100,000 (target)

# Calculate the means
mean_x = np.mean(X)
mean_y = np.mean(y)

# Calculate the terms needed for the numerator and denominator of beta
numerator = np.sum((X - mean_x) * (y - mean_y))
denominator = np.sum((X - mean_x) ** 2)

# Calculate beta
beta = numerator / denominator

# Calculate alpha
alpha = mean_y - (beta * mean_x)

# Making predictions
y_pred = alpha + beta * X

# Plotting
plt.figure(figsize=(12, 6))

# Scatter plot
plt.subplot(2, 2, 1)
plt.scatter(X, y, color='blue', label='Original data')
plt.plot(X, y_pred, color='red', label='Linear regression')
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.title('Linear Regression: Median Income vs Median House Value')
plt.legend()

# Residual plot
residuals = y - y_pred
plt.subplot(2, 2, 2)
plt.scatter(y_pred, residuals, color='green')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.axhline(y=0, color='red', linestyle='--')

# Distribution plot - Median Income
plt.subplot(2, 2, 3)
sns.histplot(X, kde=True, color='skyblue')
plt.xlabel('Median Income')
plt.ylabel('Frequency')
plt.title('Distribution of Median Income')

# Distribution plot - Median House Value
plt.subplot(2, 2, 4)
sns.histplot(y, kde=True, color='salmon')
plt.xlabel('Median House Value')
plt.ylabel('Frequency')
plt.title('Distribution of Median House Value')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()

# Calculating mean squared error
mse = np.mean((y - y_pred) ** 2)

# Print the results
print("Results:")
print("Mean Squared Error:", mse)
print("Intercept (alpha):", alpha)
print("Coefficient (beta):", beta)
