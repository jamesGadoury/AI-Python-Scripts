#!/bin/python3
import matplotlib.pyplot as plt
import math
import os
import random
import re
import sys

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

def predict_battery_life_with_trainingdata(timeCharged):
    filename = "trainingdata.txt"
    f =  open(filename, "r")
    lines = f.readlines()
    f.close()
    charge_times = []
    battery_life_times = []
    for line in lines:
        values = line.split(',')
        #plot show that correlation degrades as charge_times exceed 4, so that data is not used in training
        if float(values[0]) <= 4.00:
            charge_times.append(float(values[0]))
            battery_life_times.append(float(values[1].replace("\n", "")))
    
    #treating battery_life_times as dependent on charge_times
    slope = calculate_slope_of_regression_line(charge_times, battery_life_times)

    intercept = calculate_intercept(charge_times, battery_life_times, slope)

    #predicted battery life time for charge time of X => Y' = bX + A where b = slope and A = intercept where y is dependent on x
    predicted_battery_life = slope * timeCharged + intercept

    #plot show that correlation degrades as charge_times exceed 4, so that data is not used in training
    plt.scatter(charge_times, battery_life_times)
    plt.show()
    
    return predicted_battery_life

if __name__ == '__main__':
    timeCharged = float(input())
    if timeCharged > 4.00:
        print(8.00)
    else:
        print(round(predict_battery_life_with_trainingdata(timeCharged), 2))
    