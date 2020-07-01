import numpy as np

def neville(x, vec_x, vec_f, Q_table = None, i0 = -1, j0 = -1):
    '''
    x: point to approximate interpolation at
    vec_x: vector of x values to interpolate over
    vec_f: vector of function values solved at x value in vec_x
    '''

  n = np.size(vec_x) - 1;  # x0, x1, ..., xn.

  if (Q_table == None):
    Q_table = np.zeros((n + 1, n + 1));

  for i in np.arange(0, n + 1):
    Q_table[i][0] = vec_f[i];
  
  for j in np.arange(1, n + 1):
    for i in np.arange(j, n + 1):
      # compute Q_{i,j}
      Q_table[i][j]  = 0.0;
      Q_table[i][j] += (x - vec_x[i - j])*Q_table[i][j - 1];
      Q_table[i][j] -= (x - vec_x[i])*Q_table[i - 1][j - 1];
      Q_table[i][j] /= (vec_x[i] - vec_x[i - j]);
                   
  return Q_table[n][n], Q_table;
