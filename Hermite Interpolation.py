import numpy as np

def Hermite(x_vec, f_vec, fp_vec, Q = None):
    '''
    vec_x: vector of x values to interpolate over
    vec_f: vector of function values solved at x value in vec_x
    fp_vec: vector of derivative valyes at each x value in vec_x 
    '''
    n = np.size(x_vec)
    print('n = ', n)
    
    z_vec = []
    for i in range(0, (2*n)):
        z_vec.append(None) 
    
    if (Q == None):
        Q = np.zeros((n*2 , n*2))

    for i in range(0, n):
        z_vec[(2*i)] = x_vec[i]
        z_vec[(2*i) + 1] = x_vec[i]
        Q[2*i][0] = f_vec[i]
        Q[(2*i) + 1][0] = f_vec[i]
        Q[(2*i) + 1][1] = fp_vec[i]

        if i != 0:
            Q[2*i][1] = (Q[2*i][0] - Q[(2*i) - 1][0])/(z_vec[2*i] - z_vec[(2*i) - 1])
    
    for i in range(2, (2*n)):
        for j in range(2, i+1):
            Q[i][j]  = (Q[i][j-1] - Q[i-1][j-1])/(z_vec[i] - z_vec[i-j])
            
    return Q
