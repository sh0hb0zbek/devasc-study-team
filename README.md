# generalAI
- Add testing and validation percentage arguments
- Split validation
- fit model for testing and validatio# WearableSensorData
This repository provides the codes and data used in our paper "Human Activity Recognition Based on Wearable Sensor Data: A Standardization of the State-of-the-Art", where we implement and evaluate several state-of-the-art approaches, ranging from handcrafted-based methods to convolutional neural networks. Also, we standardize a large number of datasets, which vary in terms of sampling rate, number of sensors, activities, and subjects.

## Requirements

- [Scikit-learn](http://scikit-learn.org/stable/)
- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Python 3](https://www.python.org/)

## Linear Regression function
1. Clone this repository
2. Run
    ```bash
    python <simple_linear_regression_main|...|logistic_regression_main>.py <MHEALTH|USCHAD|UTD-MHAD1_1s|UTD-MHAD2_1s|WHARF|WISDM>.csv
    ```
        For example
    ```bash
        python simple_linear_regression_main.py student_scores.csv 4 0 100
    ```

- Input CSV file name
    - studentscores.csv
- Output CSV files name
    - Y_test_pred.csv
    - Y_train_pred.csv

## Multiple Linear Regression function
1. Clone this repository
2. Run
    ```bash
    python <multiple_linear_regression_main|...|simple_linear_regression_main>.py data/<SNOW|FNOW|LOTO|LOSO>/<MHEALTH|USCHAD|UTD-MHAD1_1s|UTD-MHAD2_1s|WHARF|WISDM>.npz
    ```
        For example
    ```bash
        python multiple_linear_regression_main.py 50_Startups.csv -1 0 -1
    ```

- Input CSV file name
    - 50_Startups.csv
- Output CSV files name
    - Y_test_pred.csv
    - Y_train_pred.csv

## Logistic Regression function
1. Clone this repository
2. Run
    ```bash
    python <logistic_regression_main|...|simple_linear_regression_main>.py data/<SNOW|FNOW|LOTO|LOSO>/<MHEALTH|USCHAD|UTD-MHAD1_1s|UTD-MHAD2_1s|WHARF|WISDM>.npz
    ```
        For example
    ```bash
        python logistic_regression_main.py Social_Network_Ads.csv 4 2 3 0 -1
    ```

- Input CSV file name
    - Social_Network_Ads.csv
- Output CSV files name
    - Y_test_pred.csv
    - Y_train_pred.csv

## Logistic Regression function
1. Clone this repository
2. Run
    ```bash
    python <logistic_regression_main|...|simple_linear_regression_main>.py data/<SNOW|FNOW|LOTO|LOSO>/<MHEALTH|USCHAD|UTD-MHAD1_1s|UTD-MHAD2_1s|WHARF|WISDM>.npz
    ```
        For example
    ```bash
        python logistic_regression_main.py Social_Network_Ads.csv 4 2 3 0 -1
    ```

- Input CSV file name
    - Social_Network_Ads.csv
- Output CSV files name
    - Y_test_pred.csv
    - Y_train_pred.csv
