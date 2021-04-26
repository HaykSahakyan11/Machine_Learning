import numpy as np


def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.07

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1 / n) * sum([val ** 2 for val in (y - y_predicted)])
        RMSE = np.sqrt(cost)
        #print(y_predicted, "pred")

        md = -(2 / n) * sum(x * (y - y_predicted))
        bd = -(2 / n) * sum(y - y_predicted)

        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd

        print('m {}, b {}, iterations {}, cost {}, RMSE {}'.format(
            m_curr, b_curr, i, cost, RMSE))
        #print("-------------------")
        #print(y-y_predicted,"----------")


x = np.array([1, 2, 3, 4, 5])
#y = np.array([3, 5, 7, 9, 11])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)
