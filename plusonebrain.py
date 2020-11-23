import pandas as pd
import numpy as np
import sklearn as sk
import sklearn.model_selection
import sklearn.linear_model

data = pd.read_csv('plusonedata.csv', sep=';')
predict = 'goingout'

x = np.array(data.drop(['goingout'], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sk.model_selection.train_test_split(x, y, test_size=0.1)

line = sk.linear_model.LinearRegression()
line.fit(x_train, y_train)
acc = line.score(x_test, y_test)

print(acc)
print(f'Line slope is {line.coef_}\nLine intercept is {line.intercept_}')

predictions = line.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])