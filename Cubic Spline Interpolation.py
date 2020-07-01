def cubicSpline(x_vec, a_vec):
    n = len(x_vec)
    print('n = ', n)
    h = [] #length n
    alpha = []
    l = []
    mu = []
    z = []
    c = []
    d = []
    b = []
    a = []
    
    for i in range(0, n):
        h.append(None)
        alpha.append(None)
        l.append(None)
        mu.append(None)
        z.append(None)
        c.append(None)
        d.append(None)
        b.append(None)
        
    for i in range(0, n-1):
        h[i] = x_vec[i+1] - x_vec[i]
    
    for i in range(1, n-1):
        alpha[i] = ((3/h[i])*(a_vec[i+1] - a_vec[i])) - ((3/h[i-1])*(a_vec[i] - a_vec[i-1]))
    
    l[0] = 1
    mu[0] = 0
    z[0] = 0
    
    for i in range(1, n-1):
        l[i] = (2*(x_vec[i+1] - x_vec[i-1])) - (h[i-1]*mu[i-1])
        mu[i] = h[i]/l[i]
        z[i] = (alpha[i] - (h[i-1]*z[i-1]))/l[i]   
   
    l[n-1] = 1
    z[n-1] = 0
    c[n-1] = 0
    
    for j in range(n-2, -1, -1):
        c[j] = (z[j]) - (mu[j]*c[j+1])
        b[j] = ((a_vec[j+1]-a_vec[j])/(h[j])) - (((h[j])*(c[j+1] + (2*c[j])))/(3))
        d[j] = (c[j+1] - c[j])/(3*h[j])
    
    return 'a = ', a_vec, 'b = ', b, 'c = ', c, 'd = ', d
