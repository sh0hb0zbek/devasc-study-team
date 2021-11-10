# generalAI
- Add testing and validation percentage arguments
- Split validation
- fit model for testing and validation

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
    python <simple_linear_regression_main|...|logistic_regression_main>.py <studentscores|50_Startups|...|Social_Network_Ads>.csv
    ```
        For example
    ```bash
        python simple_linear_regression_main.py student_scores.csv 1 0 -1
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
    python <multiple_linear_regression_main|...|simple_linear_regression_main>.py <50_Startups|studentscores|...|Social_Network_Ads>.csv
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
    python <logistic_regression_main|...|simple_linear_regression_main>.py <Social_Network_Ads|50_Startups|...|studentscores>.csv
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

## Implementation of SVM
1. Clone this repository
2. Run
    ```bash
    python <svm_implementation_main|...|simple_linear_regression_main>.py <Social_Network_Ads|50_Startups|...|studentscores>.csv
    ```
        For example
    ```bash
        python svm_implementation_main.py Social_Network_Ads.csv 2 2 3 4 0 -1
    ```

- Input CSV file name
    - Social_Network_Ads.csv
- Output CSV files name
    - Y_test_pred.csv
    - Y_train_pred.csv
