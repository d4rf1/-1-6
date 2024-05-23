import numpy as np
import matplotlib.pyplot as plt

X = [14, 8, 5, 7, 12, 2, 1, 8, 15, 12, 12, 7, 5, 9, 6, 7, 7, 5]
print('Исходный массив X')
print(X)

N = len(X)

Y = [14, 9, 6, 7, 11, 1, 1, 7, 15, 13, 12, 6.5, 5, 8, 6, 6.5, 8, 4]
print('Исходный массив Y')
print(Y)

Sx = sum(X)
Sy = sum(Y)
Sxx = np.dot(X,X)
Sxy = np.dot(X,Y)

a = (N * Sxy - Sx * Sy) / (N * Sxx - Sx * Sx)
b = (Sy - a * Sx) / N
print('y = ', a, '*x+', b)

YY = []

for x in X:
    YY.append(float(a * x + b))

Z = (np.array(Y) - np.array(YY))**2
SS = sum(Z)
print('SS = ', SS)

plt.title('MHK')
plt.xlabel('X')
plt.ylabel('Y')

plt.scatter(X,Y,c = 'r', marker = '*')

plt.plot(X, YY, 'b')

plt.show()
