import numpy as np

def calculate(num_list):
    if (len(num_list) != 9):
        raise ValueError("List must contain nine numbers.")
    m = np.array(num_list).reshape(3,3)
    keys = ['mean','variance', 'standard deviation', 'max', 'min', 'sum']
    funcs = [np.mean, np.var, np.std, np.max, np.min, np.sum]
    axes = [0,1,None]
    calculations = {}
    for i, key in enumerate(keys):
        val = []
        for axis in axes:
            val.append(funcs[i](m,axis=axis).tolist())
        calculations[key] = val

    return calculations