import pickle
import os
import sys

def get_names(name, similar_names, similar_values):
    print("Getting similar images")
    images = list(similar_names.loc[name, :])
    values = list(similar_values.loc[name, :])
    if name in images:
        images.remove(name)
        values.remove(max(values))
    return name, images, values


def get_images(input_image, model):
    similar_names = pickle.load(open(os.path.join("pickles", model, "similar_names.pkl"), 'rb'))
    similar_values = pickle.load(open(os.path.join("pickles", model, "similar_values.pkl"), 'rb'))
    
    if input_image in set(similar_names.index):
        return get_names(input_image, similar_names, similar_values)
    elif input_image+".png" in set(similar_names.index):
        input_image = input_image+".png"
        return get_names(input_image, similar_names, similar_values)
    else:
        print("'{}' is not in images.\nMake sure the name of the image is in the format: artist-name_image-name[.png]\nFor example, for The Starry Night by Van Gogh: van-gogh_the-starry-night".format(input_image))
        sys.exit(2)