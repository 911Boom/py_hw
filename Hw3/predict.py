import pandas
from xgboost import XGBRegressor

data = pandas.read_csv('ssq.csv')
# 选取后100条作为测试集
train = data[:-100]
test = data[-100:]
# 选取特征
X_columns = ['id']
y_column = ['red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'blue']
X_train = train[X_columns]
y_train = train[y_column]
X_test = test[X_columns]
y_test = test[y_column]
model = XGBRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


def get_score(y_pred, y_test):
    red_test = y_test[:6]
    blue_test = y_test[6]
    red_pred = y_pred[:6]
    blue_pred = y_pred[6]
    blue_pred = int(round(blue_pred))
    print(red_pred, blue_pred, red_test, blue_test)
    red = 0
    blue = 0
    for i in red_pred:
        i = int(round(i))
        if i in red_test:
            red += 1
    if blue_pred == blue_test:
        blue = 1
    if red == 6 and blue == 1:
        return 7500000
    elif red == 6:
        return 400000
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


TotScore = 0
for i in range(100):
    # print(y_pred[i], list(y_test.iloc[i]))
    TotScore += get_score(y_pred[i], list(y_test.iloc[i]))
print(TotScore)
