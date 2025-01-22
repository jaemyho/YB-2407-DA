
# Activity 1: Simple data cleaning and correlation Python Project


## Overview
This Python script provides an end-to-end demonstration of loading, cleaning, and analyzing datasets related to the Iris flower dataset. It calculates the correlation among numerical features and visualizes these correlations using a heatmap.

The project begins with loading data from two datasets (bezdekIris.csv and irisdata.csv) and assignment header for each columns. Then the project will perform data cleaning, gather sum of missing values and the mean of the missing values in the datasets. And perform a cleaning by removing duplicate values in the datasets.

To explore relationships between numerical features, a correlation matrix is computed. The corr() method calculates the Pearson correlation coefficients, which quantify the linear relationships between features such as sepal_length, sepal_width, petal_length, and petal_width. This correlation matrix serves as a foundation for understanding how features are related.

Lastly, Heatmap is used to visually present the correlation matrix.

## Requirements
This script requires Python libraries such as pandas for data manipulation, matplotlib for basic plotting, and seaborn for advanced visualizations. To run the script, ensure the datasets