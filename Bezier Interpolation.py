def Bezier(x_vec, y_vec, x_guide, y_guide):
    n = len(x_vec)
    print('n = ', n)
    
    a0 = []
    b0 = []
    a1 = []
    b1 = []
    a2 = []
    b2 = []
    a3 = []
    b3 = []
    
    for i in range(0,n-1):
        a0.append(None)
        b0.append(None)
        a1.append(None)
        b1.append(None)
        a2.append(None)
        b2.append(None)
        a3.append(None)
        b3.append(None)
    
    for i in range(0, n-1):
        a0[i] = x_vec[i]
        b0[i] = y_vec[i]
        
        k = i
        if(i >= 1 & n>3):
            k = i+1
        
        alpha0 = x_guide[i] - x_vec[i]
        alpha1 = x_vec[i+1] - x_guide[k+2]
        
        beta0 = y_guide[k] - y_vec[i]
        beta1 = y_vec[i+1] - y_guide[k+2]
        
        print('alpha0 = ', alpha0, 'alpha1 = ', alpha1)
        print('beta0 = ', beta0, 'beta1 = ', beta1)
        
        
        a1[i] = 3*alpha0
        b1[i] = 3*beta0
        
        
        a2[i] = ((3)*(x_vec[i+1]-x_vec[i])) - ((3)*((alpha1)+((2)*(alpha0))))
        b2[i] = ((3)*(y_vec[i+1]-y_vec[i])) - ((3)*((beta1)+((2)*(beta0))))
        
        
        a3[i] = ((2)*(x_vec[i]-x_vec[i+1])) + ((3)*(alpha0+alpha1))
        b3[i] = ((2)*(y_vec[i]-y_vec[i+1])) + ((3)*(beta0+beta1))
    
    
    
    return 'a0 = ', a0, 'a1 = ', a1, 'a2 = ', a2, 'a3 = ', a3, 'b0 = ', b0, 'b1 = ', b1, 'b2 = ', b2, 'b3 = ', b3 

