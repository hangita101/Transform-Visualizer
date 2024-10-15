import numpy as np
def T(X):
    x = X[0]
    y = X[1]
    return np.asarray([
       [x],
       [2*y] 
    ])
    