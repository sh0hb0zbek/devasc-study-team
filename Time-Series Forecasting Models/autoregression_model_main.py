from pandas import read_csv
from pandas import DataFrame
from matplotlib import pyplot
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
from math import sqrt
from sys import argv
from time import time


def autoregression_model_main(arg):
    """
        Implementation of AutoRegression Model, following command line arguments
        :param Name_Input:          input data file in .csv format
        :param Steps_to_Predict:    number of time-steps to be predicted
        This function reads a .csv file containing features, processes it
        to evaluate time-steps and forecasts the future predictions by
        implementing AutoRegression Model and store the results
    """
    Name_Input = arg[1]
    Steps_to_Predict = int(arg[2])
    start_time = time()

    # load dataset
    dataset = read_csv(Name_Input, header=0, index_col=0, parse_dates=True, squeeze=True)

    # split into train and test sets
    X = dataset.values
    train, test = X[1: len(X)-Steps_to_Predict], X[len(X)-Steps_to_Predict:]

    # train autoregression
    window = 29
    model = AutoReg(train, old_names=False, lags=29)
    model_fit = model.fit()
    coef = model_fit.params

    # walk-forward over time steps in test
    history = train[len(train)-window:]
    history = [history[i] for i in range(len(history))]
    predictions = list()
    for t in range(len(test)):
        length = len(history)
        lag = [history[i] for i in range(length-window, length)]
        yhat = coef[0]
        for d in range(window):
            yhat += coef[d+1] * lag[window-d-1]
        obs = test[t]
        predictions.append(yhat)
        history.append(obs)

    # store predictions
    dataframe = DataFrame(predictions)
    dataframe.to_csv('autoregression_model_predictions.csv', header=0)

    rmse = sqrt(mean_squared_error(test, predictions))
    exec_time = time() - start_time
    print('Test RMSE: %.3f\nExecution time: %.3f' % (rmse, exec_time))

    # # plot predictions and expected results
    # pyplot.plot(test)
    # pyplot.plot(predictions, color='red')
    # pyplot.show()


if __name__ == '__main__':
    autoregression_model_main(argv)
