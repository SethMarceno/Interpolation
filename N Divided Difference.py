import numpy as np

def Ndivdiff(x_vec, f_vec, F = None):
    '''
    vec_x: vector of x values to interpolate over
    vec_f: vector of function values solved at x value in vec_x
    '''
    
    n = np.size(x_vec)
    print('n = ', n)
    
    if (F == None):
        F = np.zeros((n , n))
        
    for i in range(0, n):
        F[i][0] = f_vec[i]
        
    for i in range(1, n):
        for j in range(i, n):
    
            F[j][i] = ((F[j][i-1] - F[j-1][i-1])/(x_vec[j] - x_vec[j-i]))
        
    return F
