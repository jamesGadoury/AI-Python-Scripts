#https://www.hackerrank.com/challenges/stockprediction/problem
# 

import ast
def write_memory(stock_prices):
    filename = "stock_memory.txt"
    f = open(filename, "w")
    for i in range(0, len(stock_prices)):
        s = str(stock_prices[i]) + "\n"
        f.write(s)
    f.close()

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
    filename = "stock_memory.txt"
    f =  open(filename, "r")
    prev_prices = []
    stocks = f.readlines()
    f.close()
    for stock in stocks:
        prev_prices.append(ast.literal_eval(stock))
    return prev_prices

# Complete the function printTransactions that takes a float m money left, 
# an integer k number of stocks, an integer d days left, 
# a string array name of stock names, 
# an integer array owned of stocks owned, 
# and an 2d integer array prices of stock prices containing k arrays of length 5
#  and print your output.

#All indexes correspond properly (For index i, the name of the stock is name[i], 
# the number of shares of it you hold is owned[i] and the data about it is prices[i].

def printTransactions(m, k, d, name, owned, prices):
    write_memory(prices)
    prev_prices = read_trainingdata()
    for i in range(0, len(prev_prices)):
        prices[i].extend(prev_prices[i])
    slope_list = []
    prev_slope_list = []
    print(prev_prices[1])
    for j in range(len(prices)):
        slope_list.append(calculate_slope_of_regression_line(range(len(prices[j])), prices[j]))
        prev_slope_list.append(calculate_slope_of_regression_line(range(len(prev_prices[j])), prev_prices[j]))
    trans = []
    for k in range(len(slope_list)):
        if slope_list[k] < 0 and m > prices[k][4] and (name[k] == 'UCLA' or name[k] == 'UCSC'):
            trans.append(str(names[k]) + " BUY " + str(int(m / prices[k][4])))
            m = m - prices[k][4] * int(m / prices[k][4])
    for l in range(len(name)):
        if slope_list[l] > 10 and owned[l] > 0:
            trans.append(str(names[l]) + " SELL " + str(owned[l]))
    print(len(trans))
    for n in range(len(trans)):
        print(trans[n])

    
    

if __name__ == '__main__':
    m, k, d = [float(i) for i in input().strip().split()]
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for data in range(k):
        temp = input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])

    printTransactions(m, k, d, names, owned, prices)

    # need to predict when stocks are cheap, but about to rise
    # predict when growth is going to come in 4 turns when item is cheap
    # predict when item is going to devalue in 4 turns so it can be sold