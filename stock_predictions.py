#predicts stock price drops / gains through regression lines between data sets

import math
import os
import random
import re
import sys
import matplotlib.pyplot as plt
import numpy as np


def calculate_coefficient_of_correlation(x, y):
    numerator = float(0.0)
    x_avg = sum(x) / len(x)
    y_avg = sum(y) / len(y)
    for i in range(len(x)):
        numerator += (x[i] - x_avg) * (y[i] - y_avg)

    denominator_a = float(0.0)
    denominator_b = float(0.0)
    for j in range(len(x)):
        denominator_a += (x[j] - x_avg) ** 2.0
        denominator_b += (y[j] - y_avg) ** 2.0

    r = numerator / ((denominator_a ** 0.5) * (denominator_b ** 0.5))
    return r

def find_top_correlation(stock_dict):
    correlation_list = []
    for keyA in stock_dict:
        for keyB in stock_dict:
            if keyA != keyB:
                r = calculate_coefficient_of_correlation(stock_dict[keyA], stock_dict[keyB])
                if r > -0.5 and r < -1.0 or r > 0.5 and r < 1:
                    already_in_list = False
                    for i in range(len(correlation_list)):
                        if keyA in correlation_list[i] and keyB in correlation_list[i]:
                            already_in_list = True
                            break
                    if not already_in_list:
                        correlation_list.append([keyA, keyB])
                    
    return correlation_list 

def calculate_slope_of_regression_line(x, y):
    x_avg = sum(x) / len(x)
    y_avg = sum(y) / len(y)
    numerator = 0
    denominator = 0
    #treating x as independent, y as dependent
    for i in range(len(x)):
        numerator += (x[i] - x_avg) * (y[i] - y_avg)
        denominator += (x[i] - x_avg) ** 2

    slope = numerator / denominator
    return slope

def calculate_intercept(x, y, slope):
    # calculate intercept of y dependent on x
    intercept = sum(y) / len(y) - slope * sum(x) / len(x)
    return intercept

def read_trainingdata():
    filename = "stock_training.txt"
    f =  open(filename, "r")
    stock_dict = {}
    stocks = f.readlines()
    f.close()
    for stock in stocks:
        values = stock.split(' ')
        values[len(values) - 1].replace("\n", "")
        stock_dict[values[0]] = [float(i) for i in values[1:-1]]
    
    return stock_dict


if __name__ == '__main__':
    stock_dict = read_trainingdata()
    correlation_list = []

    correlation_list = find_top_correlation(stock_dict)
    print(correlation_list)

    for key in stock_dict:
        vals = range(len(stock_dict[key]))
        #y_pos = np.arange(len(vals))
        y_pos = vals
        plt.bar(y_pos, stock_dict[key])

        # Create names on the x-axis
        plt.xticks(y_pos, stock_dict[key])
        plt.title(key)
 
        # Show graphic
        plt.show()

#High Growth : RIT
#High Flux: UCLA UCSC