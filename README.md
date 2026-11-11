# Bakery Sales Forecast
## Introduction
This notebook analyzes the bakery sales dataset. I cleaned the data by checking every column for NaN values, renaming columns, and verifying the data type of each column. I then divided the products into four tiers: High, Medium, Bottom, and Rare. The Medium tier was split into Upper-Medium, Mid-Medium, and Lower-Medium. The Bottom tier was split into Upper-Bottom, Mid-Bottom, and Lower-Bottom. The Rare tier was split into Upper-Rare, Mid-Rare, and Lower-Rare. Finally, I dropped the Medium, Bottom, and Rare tiers because they generate far less revenue: there is a gap of about $5K between the lowest-earning product in the High tier and the highest-earning product in the Upper-Medium tier.

## Workflows  
1.**EDA** : Clean the messy data, rename columns to fit the dataset, and build a chart for each product and tier.

2.**Filtering** : Keep only the top-selling producets, create a monthly series from them, and save it as a new dataset file. 

3.**Import** : Load the new dataset file into a seperate notebook for the forecasting task.

4.**Pattern check** : Plot the sales as a time series to identify the pattern and decide which type of forecast model fits it. 

5.**Model selection**: Compare the candidate models by thier error on a holdout set, training on the earlier months and testing on July to September 2022. 

5.1 **Seasonal Naive + Growth**

5.2 **Fourier Regression**

6.**Model Result**: 
```
|                          | MAE      | MAPE    |
| :----------------------- | :------: | :-----: |
| Seasonal Naive + Growth  | 2952.473 | 0.086 % |
| Fourier Regression       | 7565.411 | 0.252 % |
```

7. **Final Model** : Use Seasonal Naive + Growth, since it has the lowest error.

8. **Forecast results** : 
```
| Date     | Result    |
| :------: | :-------: |
| Oct-2022 | 21558.355 |
| Nov-2022 | 16683.891 |
| Dec-2022 | 16391.031 |
```


