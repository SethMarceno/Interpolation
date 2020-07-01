def CubicPara(x_vec, y_vec, Lx_guide, Ly_guide, Rx_guide, Ry_guide):
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
        
        a1[i] = Lx_guide[i] - x_vec[i]
        b1[i] = Ly_guide[i] - y_vec[i]
        
        a2[i] = ((3)*(x_vec[i+1]-x_vec[i])) - ((x_vec[i+1]-Rx_guide[i]) + ((2)*(Lx_guide[i] - x_vec[i])))
        b2[i] = ((3)*(y_vec[i+1]-y_vec[i])) - ((y_vec[i+1]-Ry_guide[i]) + ((2)*(Ly_guide[i] - y_vec[i])))
        
        a3[i] = (((2)*(x_vec[i]-x_vec[i+1])) + ((Lx_guide[i] - x_vec[i])+(x_vec[i+1]-Rx_guide[i])))
        b3[i] = (((2)*(y_vec[i]-y_vec[i+1])) + ((Ly_guide[i] - y_vec[i])+(y_vec[i+1]-Ry_guide[i])))
    
    
    
    return 'a0 = ', a0, 'a1 = ', a1, 'a2 = ', a2, 'a3 = ', a3, 'b0 = ', b0, 'b1 = ', b1, 'b2 = ', b2, 'b3 = ', b3 



