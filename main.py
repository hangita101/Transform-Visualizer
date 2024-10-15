import matplotlib.pyplot as plt
import numpy as np
from Transform import T


def main(lim):
    """
    The arguments are 
    Xlim,
    Ylim,    
    """
    try:
        assert lim[0]<lim[1]
    except :
        print("Error")
    
    minval = lim[0]
    maxval = lim[1]
                
    plt.xlim(lim)
    plt.ylim(lim)
    
    x = np.linspace(lim[0],lim[1],)
    
    for i in range(lim):
        plt.hlines(i,xmin=minval,xmax=maxval,linewidth=0.3)
        plt.vlines(i,ymin=minval,ymax=maxval,linewidth=0.3)
        # for horizontal lines
        y = np.full_like(x,i)
        X = np.stack([x,y],axis=0)
        xx,yy=T(X)
        xx= xx.squeeze()
        yy = yy.squeeze()
        
        plt.plot(xx,yy,color=(0.5,0.5,0.5),linewidth=0.5)
        # for vertical lines
        y = np.full_like(x,i)
        X = np.stack([y,x],axis=0)
        xx,yy=T(X)
        xx= xx.squeeze()
        yy = yy.squeeze()
        plt.plot(xx,yy,color=(0.5,0.5,0.5),linewidth=0.5)

    



plt.figure(figsize=(8,8))
plt.xlim(-20,20)
plt.ylim(-20,20)  
plt.scatter(0,0,s=2,c='b')
plt.vlines(0,-100,100)
plt.hlines(0,-100,100)

for i in range(-20,20):
    plt.hlines(i,xmin=minval,xmax=100,linewidth=0.3)
    plt.vlines(i,ymax=100,ymin=-100,linewidth=0.3)
    # for hirizontal lines
    y = jnp.full_like(x,i)
    X = jnp.stack([x,y],axis=0)
    xx,yy=T(X)
    xx= xx.squeeze()
    yy = yy.squeeze()
    plt.plot(xx,yy,color=(0.5,0.5,0.5),linewidth=0.5)

    # for vertical lines
    y = jnp.full_like(x,i)
    X = jnp.stack([y,x],axis=0)
    xx,yy=T(X)
    xx= xx.squeeze()
    yy = yy.squeeze()
    plt.plot(xx,yy,color=(0.5,0.5,0.5),linewidth=0.5)

y1 = x
plt.plot(x,y1,label='before',color=(0.0,0.,0.0))

X1 = jnp.stack([x,y1],axis=0)
xx,yy=T(X1)
xx,yy= xx.squeeze(),yy.squeeze()
plt.plot(xx ,yy,c='r',label='after')

plt.legend()





if __name__=="__main__":
    
    pass

