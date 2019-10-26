import pandas as pd
import numpy as np
import os
from numpy.linalg import norm

def matrix_calculator(vectors):
    print("Computing cosine similarity matrix")
    test = np.array(list(vectors.values())).T
    sim = np.inner(test.T, test.T) / ((norm(test, axis=0).reshape(-1,1)) * ((norm(test, axis=0).reshape(-1,1)).T))
    
    assert sim.shape[0] == sim.shape[1] == len(os.listdir("resized"))
    
    col = list(vectors.keys())
    row = col
    matrix = pd.DataFrame(sim, columns = col, index = row)
    
    return matrix