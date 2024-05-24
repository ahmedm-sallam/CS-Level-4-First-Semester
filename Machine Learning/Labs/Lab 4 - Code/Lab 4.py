import pandas
import numpy
import matplotlib.pyplot as plot
from sklearn import linear_model
from sklearn.model_selection import train_test_split

data = pandas.read_csv('acceptance_data.txt', names = ['exam1','exam2','decision'])

# Step 1 (skip)

# Step 2
X = data.drop(columns=['decision'])

# Task 1: Perform feature scaling
# Why is it needed? # Can it be done after splitting?

X = X.to_numpy().reshape((-1,2))
y = data['decision'].to_numpy() # What if the decision was "Yes" and "No"?

# Step 3
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) # shuffle, random_state

# Step 4
model = linear_model.LogisticRegression(solver='sag')
model.fit(X_train, y_train)

print('Coefficients: \n', model.coef_, " ", model.intercept_)

# Step 5
y_pred = model.predict(X_test)
print('Correct predicitions ratio: %.2f'% model.score(X_test, y_test))

# Step 6
model.predict([[75, 82]])

# Task 2: Complete this function
def calc_acc(X, y):
    #####
    return acc