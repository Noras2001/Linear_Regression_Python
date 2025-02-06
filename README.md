# Simple Linear Regression in Python

This repository contains a Python script that demonstrates how to perform simple linear regression on a dataset, using `scipy.stats.linregress` to calculate the regression parameters and visualize the results with `matplotlib`.

## Project Overview

The script demonstrates a basic implementation of linear regression to predict final grades (`notas`) based on the number of hours spent studying per week (`horas_estudio`). The regression model is fitted using the `linregress` function from the `scipy.stats` module.

### Dataset

The dataset contains the following values:

- `horas_estudio` (Study hours per week): A list of hours spent studying each week.
- `notas` (Final grades): A list of final grades corresponding to the study hours.

```python
horas_estudio = np.array([1, 2.5, 3.5, 4.2, 4.5, 5.3, 6, 6.3, 7, 8.5], dtype='float16')
notas = np.array([2, 3, 3.5, 3.7, 4, 4.2, 4.5, 4.6, 4.8, 5], dtype='float16')
```

## Key Components

- **Linear Regression**: The `linregress` function calculates the following parameters:
  - **Slope**: The slope of the regression line.
  - **Intercept**: The y-intercept of the regression line.
  - **R-squared (R²)**: The coefficient of determination, indicating the goodness of fit.
  - **p-value**: The p-value indicating the statistical significance of the regression.
  - **Standard error**: The standard error of the estimated slope.

- **Prediction Function**: The `predict(x)` function predicts the final grade (`y`) for a given number of study hours (`x`).

- **Plotting**: The script visualizes the data points and the regression line using `matplotlib`.

## How to Run

1. Install the required dependencies:
   ```bash
   pip install numpy matplotlib scipy
   ```

2. Run the script:
   ```bash
   python linear_regression.py
   ```

The script will output the regression parameters and display a plot showing the data points and the fitted regression line.

## Example Output

```
Slope: 0.2841796875
Intercept: 1.4384375
R^2: 0.9771940911500801
p-value: 4.757367470768822e-05
Standard error: 0.04047702383305126
y=0.28*x+1.44
```


## License

This project is licensed under the MIT License.

