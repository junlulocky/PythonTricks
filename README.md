# PythonTricks

See also my original [webpage](http://www.junlulocky/blog/pythontricks)

## Useful codes

#### logger

Use the logger utility in your Python code to track your running easily

| Code | Example | 
|:-------:| ----------- |
| [logger](/logger/logger.py) | [example](/logger/examples/logger_demo.py) |


## Cannot load module
If you installed a module by pip, you may cannot load it. 

To be sure you install the package using the correct pip instance for your python interpreter you need to run something like:

```
/bin/env python -m pip install --upgrade mymodule
```

or for OSX

```
/usr/bin/env python -m pip install --upgrade mymodule
```

[source in stack overflow](http://stackoverflow.com/questions/15052206/python-pip-install-module-is-not-found-how-to-link-python-to-pip-location)


## Python change font size

try the following ones

```python
plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)
plt.tick_params(axis='both', which='major', labelsize=15)
cbar = plt.colorbar(im, cax=cax)
cbar.ax.tick_params(axis='both', which='major', labelsize=15)
plt.rcParams.update({'font.size': 15})
```

## Python add xlabel

try the following two ways

```python
plt.xlabel('a', fontsize=15)
plt.ylabel('b', fontsize=15)
```

or

```python
ax = plt.subplot(111)
ax.set_xlabel('x', fontsize=15)
ax.set_ylabel('y', fontsize=15)
```

## Python change xtick rotation

```
plt.xticks(rotation = 90)
```

## Numpy tricks

#### Remove a row with 'NaN'

```python
>>> a = np.array([[1,2,3], [4,5,np.nan], [7,8,9]])
array([[  1.,   2.,   3.],
       [  4.,   5.,  nan],
       [  7.,   8.,   9.]])

>>> a[~np.isnan(a).any(axis=1)]
array([[ 1.,  2.,  3.],
       [ 7.,  8.,  9.]])
```

#### Set seed

```python
import numpy as np
import random

seed = 12345
np.random.seed(seed)
random.seed(seed)

````



## Installation
Anaconda is a very good python package including all useful scientific computing tools. It can be downloaded from: [link](http://continuum.io/downloads#all)

run the following command:

```
 >bash Anaconda-2.x.x-Linux-x86[_64].sh 
```

### Autocompletion in the terminal
In order to have autocompletion using TAB in the terminal, we have to load two commands:

```
import rlcompleter, readline
readline.parse_and_bind('tab:complete')
```

Those two lines can be automatically loaded by creating a .pythonrc in your home directory with those two files and by adding

```
export PYTHONSTARTUP=~/.pythonrc
```

to your .profile

## Command line debugger

### Debugger

```
 >python -m pdb <your_code.py> 
```

At start you are at the begining of your code. Then you can create breakpoints.

- Breakpoint at line 100 in the main file: 

```
 (Pdb) b 100
```

- Breakpoint at line 50 in another file: 

```
 (Pdb) b myclass.py:50 
```

You can go though your code until first breakpoint by typing 'c' (continue)

You can go though your code step by step:

- n: execute current statement
- s: execute and step into 

Enable/Disable/Clear breakpoint:

- disable number
- enable number
- clear number 

```
 (Pdb) b myclass.py:50 
```

- Breaking on error: 

```
 >python -Werror -mpdb <your_code> 
```

### Profiler

```
 >python -m cProfile <your_code.py> 
```

### Matlab vs Python

|Matlab | Python/Numpy |
|---|---|
|X[1] (indexing starts at 1)  |   X[0] (indexing starts at 0) |



