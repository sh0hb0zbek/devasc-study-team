from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error
from sys import argv
from time import time


def persistence_model_main(arg):
    """
        Implementation of Persistence Model, following command line arguments
        :param Name_Input:  input data file in .csv format
        This function reads a .csv file containing features, processes it
        to evaluate time-steps and forecasts the future predictions by
        implementing Persistence Model and store the results
    """
    Name_Input = argv[1]
    start_time = time()

    # load dataset
    dataset = read_csv(Name_Input, header=0, index_col=0, parse_dates=True, squeeze=True)

    # create lagged dataset
    values = DataFrame(dataset.values)
    dataframe = concat([values.shift(1), values], axis=1)

    # split into train and test sets
    X = dataframe.values
    train_size = int(len(X) * 0.66)
    train, test = X[1:train_size], X[train_size:]
    train_X, train_y = train[:, 0], train[:, 1]
    test_X, test_y = test[:, 0], test[:, 1]

    # walk-forward validation
    predictions = list()
    for x in test_X:
        yhat = model_persistence(x)
        predictions.append(yhat)

    # store predictions
    dataframe = DataFrame(predictions)
    dataframe.to_csv('persistence_model_predictions.csv', header=0)

    test_score = mean_squared_error(test_y, predictions)
    exec_time = time() - start_time
    print('Test MSE: %.3f\nExecution time: %.3f' % (test_score, exec_time))

    # # plot predictions and expected results
    # pyplot.plot(train_y)
    # pyplot.plot([None for i in train_y] + [x for x in test_y])
    # pyplot.plot([None for i in train_y] + [x for x in predictions])
    # pyplot.show()


# persistence model
def model_persistence(x):
    return x


if __name__ == '__main__':
    persistence_model_main(argv)
