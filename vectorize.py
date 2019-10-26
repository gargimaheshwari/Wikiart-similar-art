import sys
from PIL import Image
import os
from tqdm import tqdm
import pickle
from img2vec import Img2Vec

def img2vec_converter(model, cuda):
    img2vec = Img2Vec(cuda = cuda, model = model) #change to false if no gpu

    #with gpu this takes about an hour. Without, around four or five
    vectors = {}
    print("Converting images to vectors:")
    for image in tqdm(os.listdir("resized")):
        img = Image.open(os.path.join("resized", image))
        try:
            vec = img2vec.get_vec(img)
            #certain images are in rgba format and raise a runtime error here
            #converting them to rgb solves this issue
        except RuntimeError:
            vec = img2vec.get_vec(img.convert('RGB'))
        assert len(vec) == img2vec.layer_output_size
        vectors[image] = vec
        img.close() 
    
    assert len(vectors) == len(os.listdir("resized"))
    
    print("Saving image vectors")
    os.makedirs(os.path.join("pickles", model), exist_ok = True)
    file = open(os.path.join('pickles', model, 'vectors.pkl'), 'wb')
    pickle.dump(vectors, file)
    file.close()
    
    return vectors