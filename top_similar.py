import pandas as pd
from tqdm import tqdm
import pickle
import os

def top10(sim_matrix, model):
    
    print("Extracting and saving top 10 image names and similarity values")
    similar_names = pd.DataFrame(index = sim_matrix.index, columns = range(11))
    similar_values = pd.DataFrame(index = sim_matrix.index, columns = range(11))

    for i in tqdm(range(sim_matrix.shape[0])):
        similar = sim_matrix.iloc[i, :].sort_values(ascending = False).head(11)
        similar_names.iloc[i, :] = list(similar.index)
        similar_values.iloc[i, :] = similar.values

    similar_names.to_pickle(os.path.join("pickles", model, "similar_names.pkl"))
    similar_values.to_pickle(os.path.join("pickles", model, "similar_values.pkl"))