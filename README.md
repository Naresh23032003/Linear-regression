# Linear-regression
## Linear Regression Analysis: Median Income vs Median House Value

This project aims to analyze the relationship between median income and median house value using linear regression. It utilizes the California Housing dataset, focusing on the first 500 data points for better visualization.

## Dataset
The dataset used in this project is the California Housing dataset, which contains housing-related information such as median income, median house value, etc.

## Project Structure
- `linear_regression.py`: Python script for performing linear regression analysis.
- `README.md`: Markdown file providing information about the project.

## Requirements
- Python 3.x
- NumPy
- Matplotlib
- SKlearn
- Seaborn

## Usage
1. Clone the repository or download the files.
2. Install the required dependencies using `pip install numpy matplotlib sklearn seaborn`.
3. Run the `linear_regression.py` script using Python.
4. The script will generate a scatter plot showing the relationship between median income and median house value, along with the linear regression line also other plots for better visualization.
5. Mean squared error and coefficients (intercept and coefficient) will be printed in the console.

## Results

![download](https://github.com/Naresh23032003/Linear-regression/assets/72620370/036c68a1-d73c-425c-a5b2-1f4363bb3f71)

Mean Squared Error: 0.4379935254847339

Intercept (alpha): 0.6019438492294418

Coefficient (beta): 0.39888938971145643

## Conclusion

The linear regression analysis conducted on the California Housing dataset revealed several key insights:

- **Positive Correlation**: There exists a positive correlation between median income and median house value in California. As median income increases, median house value tends to increase as well, indicating that higher-income areas generally have higher property values.

- **Model Performance**: The linear regression model demonstrated reasonable performance in predicting median house values based on median income, as indicated by the mean squared error (MSE) of 0.4379. While the model captures the overall trend, there may be inherent complexities or additional factors influencing house prices that are not accounted for in this analysis.

- **Intercept and Coefficient**: The intercept (alpha) value of 0.6019 suggests that even in areas with zero median income, there is a base level of median house value. The coefficient (beta) value of 0.3989 indicates that for every unit increase in median income, the median house value is expected to increase by approximately $0.40 thousand.

In summary, this analysis provides valuable insights into the relationship between median income and median house value in California. However, it's important to consider additional factors and conduct further analysis for a comprehensive understanding of housing market dynamics.
