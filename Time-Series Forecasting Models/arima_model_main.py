from pandas import read_csv
from pandas import DataFrame
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
from sys import argv
from time import time


def arima_model_main(arg):
    """
        Implementation of Persistence Model, following command line arguments
        :param Name_Input:  input data file in .csv format
        This function reads a .csv file containing features, processes it
        to evaluate time-steps and forecasts the future predictions by
        implementing Rolling Forecast ARIMA Model and store the results
    """
    Name_Input = arg[1]
    start_time = time()

    # load dataset
    dataset = read_csv(Name_Input, header=0, index_col=0, parse_dates=True, squeeze=True)
    dataset.index = dataset.index.to_period('M')

    # split into train and test sets
    X = dataset.values
    train_size = int(len(X) * 0.66)
    train, test = X[:train_size], X[train_size:]
    history = [x for x in train]
    predictions = list()

    # walk-forward validation
    for t in range(len(test)):
        model = ARIMA(history, order=(5, 1, 0))
        model_fit = model.fit()
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)

    # store predictions
    dataframe = DataFrame(predictions)
    dataframe.to_csv('arima_model_predictions.csv', header=0)

    # evaluate forecasts
    rmse = sqrt(mean_squared_error(test, predictions))
    exec_time = time() - start_time
    print('Test RMSE: %.3f\nExecution time: %.3f' % (rmse, exec_time))

    # # plot predictions and expected results
    # pyplot.plot(test)
    # pyplot.plot(predictions, color='red')
    # pyplot.show()


if __name__ == '__main__':
    arima_model_main(argv)
