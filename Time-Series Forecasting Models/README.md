# Time-Series Forecasting
- Persistence Model
- AutoRegression Model
- ARIMA Model

## Requirements

- [Scikit-learn](http://scikit-learn.org/stable/)
- [Pandas](https://pandas.pydata.org/)
- [Statsmodels](https://www.statsmodels.org/)
- [Matplotlib](https://matplotlib.org/)
- [Python 3](https://www.python.org/)

## Persistence Model
1. Clone this repository
2. Run
    ```bash
    python <persistence_model_main|...|arima_model_main>.py <monthly-car-sales|...>.csv
    ```
   For example
    ```bash
        python persistence_model_main.py monthly-car-sales.csv
    ```

- Input CSV file name
    - monthly-car-sales.csv
- Output CSV file name
    - persistence_model_predictions.csv

## AutoRegression Model
1. Clone this repository
2. Run
    ```bash
    python <autoregression_model_main|...|arim_model_main>.py <monthly-car-sales|...>.csv
    ```
   For example
    ```bash
        python autoregression_model_main.py monthly-car-sales.csv 6
    ```

- Input CSV file name
    - monthly-car-sales.csv
- Output CSV file name
    - autoregression_model_predictions.csv

## Rolling Forecast ARIMA model
1. Clone this repository
2. Run
    ```bash
    python <arima_model_main|...|persistence_model_main>.py <monthly-car-sales|...>.csv
    ```
   For example
    ```bash
        python arima_model_main.py monthly-car-sales.csv
    ```

- Input CSV file name
    - monthly-car-sales.csv
- Output CSV files name
    - arima_model_predictions.csv