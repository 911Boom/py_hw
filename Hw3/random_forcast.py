import random
import pandas


def get_score(y_pred, y_test):
    red_test = y_test[:6]
    blue_test = y_test[6]
    red_pred = y_pred[:6]
    blue_pred = y_pred[6]
    blue_pred = int(round(blue_pred))
    # print(red_pred, blue_pred, red_test, blue_test)
    red = 0
    blue = 0
    for i in red_pred:
        i = int(round(i))
        if i in red_test:
            red += 1
    if blue_pred == blue_test:
        blue = 1
    if red == 6 and blue == 1:
        return 4000000
    elif red == 6:
        return 80000
    elif red == 5 and blue == 1:
        return 3000
    elif red == 5 or (red == 4 and blue == 1):
        return 200
    elif red == 4 or (red == 3 and blue == 1):
        return 10
    elif blue == 1:
        return 5
    else:
        return -2


data = pandas.read_csv('./Hw3/ssq.csv')
y_column = ['red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'blue']
test = data[y_column]


def game():
    tot = 0
    for i in range(1000):
        y_pred = random.sample(range(1, 34), 6)
        y_pred.append(random.randint(1, 16))
        y_test = list(test.iloc[i])
        score = get_score(y_pred, y_test)
        if score > 200:
            print(y_pred, y_test)
            print(score)
        tot += score
    print(tot)
    return tot


t = 0
for i in range(100):
    t += game()

print(t/100)
