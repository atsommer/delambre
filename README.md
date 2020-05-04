## delambre
A pure python package for numbers with units that are compatible with lists and numpy arrays, and behave intuitively.

To use the package, you import Delambre.MKS. The MKS module describes physical quantities using SI units as the underlying representation, but you can work with quantities in other units as well.

Example 1: Convert kilometers to miles:
```python
  >>> from delambre import SI as u
  >>> x = 5*u.km
  >>> x/u.mi
  3.1068559611866697
```  
Example 2: Quantities are stored in SI units:
```python
  >>> u.hour
  3600.0 s
```

Example 3: Quantities can be manipulated with arithemetic operations:
```python
  >>> 5*u.gram/u.s + 2*u.kg/u.min
  0.0383333333333 kg s^-1
```  
Example 4: Dimensionless quantities are converted automatically to unitless numbers, and can be used in numerical functions:
```python
  >>> import numpy as np
  >>> np.sin(3*u.cm/u.inch)
  0.92502536766051635
```
Example 5: Multiplying by a list happenes element-wise:
```python
>>> [1,2]*u.kg
[1.0 kg, 2.0 kg]
>>> [u.m,u.s]*u.m
[1.0 m^2, 1.0 m s]
```
Example 6: Multiplying with a numpy array on the right ascribes units to the array:
```python
  >>> x= u.m*np.array([1,2]); x
  [ 1.  2.] m
  >>> np.sin(x/u.cm)
  array([-0.50636564, -0.8732973 ])
```
Example 7: Multiplying with a numpy array on the left creates an array of objects. However, due to the behavior of numpy functions, these continue to have the dtype of 'object' even after being non-dimensionalized:
```python
>>> np.array([1,2])*u.m
array([1.0 m, 2.0 m], dtype=object)
>>> np.array([1,2])*u.s/u.s
array([1.0, 2.0], dtype=object)
```
For working with numpy arrays, it is best to multiply with the array on the right, as in Example 6, to allow automatic non-dimensionalization.
