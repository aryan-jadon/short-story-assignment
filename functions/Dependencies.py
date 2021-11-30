import numpy as np
import ray

@ray.remote
def create_matrix(size):
    return np.random.normal(size=size)

@ray.remote
def multiply_matrices(x, y):
    return np.dot(x, y)

x_id = create_matrix.remote([1000, 1000])
y_id = create_matrix.remote([1000, 1000])
z_id = multiply_matrices.remote(x_id, y_id)

# Get the results.
z = ray.get(z_id)
print(z)
'''
[[-62.30022241 -83.0611604    5.72010034 ... -61.02951196  15.04974551
   43.99595037]
 [ -6.23070769  32.80734975 -33.64986191 ... -38.4687297   14.88310789
   50.84077935]
 [-49.06475522 -16.83841587  36.72203119 ...  38.82781677  41.80612796
  -42.99423584]
 ...
 [ 18.90957542 -34.29446846  49.95619848 ...  13.25161149  16.69423933
    1.66444909]
 [ -4.07011657 -55.90377254 -40.73841092 ... -16.06169279  36.48743567
  -14.49553321]
 [ -1.77445099  20.69593156  24.09842907 ...  19.03980352 114.95532402
   41.73977812]]
'''
