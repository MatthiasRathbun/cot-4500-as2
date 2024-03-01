import numpy as np
def nevilles_interpolation(x_values, y_values, x):
    n = len(x_values)
    p = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        p[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n-j):
            p[i][j] = ((x - x_values[i+j])*p[i][j-1] - (x - x_values[i])*p[i+1][j-1]) / (x_values[i] - x_values[i+j])

    return p[0][n-1]


def newton_coef(x, y):
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])

    for j in range(1, n):

        for i in range(n-1, j-1, -1):
            a[i] = float(a[i]-a[i-1])/float(x[i]-x[i-j])

    return np.array(a)

def newton_forward(a, x, r):
    n = len( a ) - 1
    temp = a[n] + (r - x[n])
    for i in range( n - 1, -1, -1 ):
        temp = temp * ( r - x[i] ) + a[i]
    return temp

def hermite_polynomial(x_values, y_values, y_prime_values):

    n = len(x_values) * 2
    Q = [[0 for _ in range(n + 1)] for _ in range(n)]
    
    for i in range(0, n, 2):
        Q[i][0] = x_values[i // 2]
        Q[i + 1][0] = x_values[i // 2]
        Q[i][1] = y_values[i // 2]
        Q[i + 1][1] = y_values[i // 2]
        
    for i in range(0, n, 2):
        Q[i + 1][2] = y_prime_values[i // 2]
        if i != 0:
            Q[i][2] = (Q[i][1] - Q[i - 1][1]) / (Q[i][0] - Q[i - 1][0])
    
    for i in range(2, n):
        for j in range(2, i + 1):
            Q[i][j + 1] = (Q[i][j] - Q[i - 1][j]) / (Q[i][0] - Q[i - j][0])
    
    for row in Q:
        print(row)

def cubic_spline_interpolation(x_values, y_values):
    n = len(x_values) - 1  
    h = [x_values[i+1] - x_values[i] for i in range(n)] 
    
    A = np.zeros((n+1, n+1))
    A[0,0] = 1
    A[n,n] = 1
    for i in range(1, n):
        A[i, i-1] = h[i-1]
        A[i, i] = 2 * (h[i-1] + h[i])
        A[i, i+1] = h[i]
    
    b = np.zeros(n+1)
    for i in range(1, n):
        b[i] = 3 * ((y_values[i+1] - y_values[i]) / h[i] - (y_values[i] - y_values[i-1]) / h[i-1])
    
    x = np.linalg.solve(A, b)
    
    
    return A, b, x