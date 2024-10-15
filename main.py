import matplotlib.pyplot as plt
import numpy as np
from Transform import T
import sys


def Transform(X):
        xx,yy=T(X)
        xx= xx.squeeze()
        yy = yy.squeeze()
        return xx,yy
def main(lim,**kwargs):
    """
    The arguments are 
    Xlim,
    Ylim,    
    """
    try:
        assert lim[0]<lim[1]
    except :
        print("First argument should be larger than second one")
    
    minval = lim[0]
    maxval = lim[1]
    plt.axis('equal')
    plt.xlim(lim)
    plt.ylim(lim)
    
    x = np.linspace(lim[0],lim[1],)
    
    
    for i in range(minval,maxval):
        plt.hlines(i,xmin=minval,xmax=maxval,linewidth=0.3)
        plt.vlines(i,ymin=minval,ymax=maxval,linewidth=0.3)
        # for horizontal lines
        y = np.full_like(x,i)
        X = np.stack([x,y],axis=0)
        xx,yy=T(X)
        xx= xx.squeeze()
        yy = yy.squeeze()
        
        plt.plot(xx,yy,color=(1.0,0.5,0.5),linewidth=0.5)
        # for vertical lines
        y = np.full_like(x,i)
        X = np.stack([y,x],axis=0)
        xx,yy=T(X)
        xx= xx.squeeze()
        yy = yy.squeeze()
        
        plt.plot(xx,yy,color=(1.0,0.5,0.5),linewidth=0.5)

    
    
    
    if kwargs['unitarrow']==True:
        plt.arrow(0,0,1.0,1.0,label='before',color='black')
        finalarrow=Transform(np.array([[1.0],[1.0]]))
        plt.arrow(0,0,finalarrow[0],finalarrow[1],color='r' , label="Unit after transform")
        

if __name__=="__main__":
    lim=(minv,maxv)= int(sys.argv[1]),int(sys.argv[2])
    
    main(lim,unitarrow=True)

        
    plt.show()

