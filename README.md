## Transformation Visualizer

Write you transformation in `Transfrom.py` file
like
```python
def T(X):
    x = X[0]
    y = X[1]
    return np.asarray([
       [x],
       [2*y] 
    ])
    
```
Another Example:


```python
def T(X):
    x = X[0]
    y = X[1]
    return np.asarray([
       [ 5*np.sin(x*y)],
       [2*y] 
    ])
```

The command like arguments are just lower limit and upper limit
meaning it will create an Square canvas
The first part should be lower then second one
`python main.py -10 10 `
