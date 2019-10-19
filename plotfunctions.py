import pickle
import os
from PIL import Image, ImageOps
import matplotlib.image as mpimg
from textwrap import wrap

jsondata = pickle.load(open(os.path.join("pickles", "jsondata.pkl"), 'rb'))
jsondata.loc[jsondata.artistUrl == "ethel-reed", "artistName"] = "Ethel Reed"
jsondata.loc[jsondata.artistUrl == "ancient-greek-painting", "artistName"] = "Ancient Greek Painting"

def get_image(name):
    img = Image.open(os.path.join("images", name))
    return img.convert('RGB')

def add_border(name, border):
    img = ImageOps.expand(name, border = 2, fill = "white")
    return ImageOps.expand(img, border = (border - 2))

def get_label(name):
    name = name[:-4].split("_", 1)
    x = jsondata.loc[((jsondata.artistUrl == name[0])&(jsondata.url == name[1])), :].reset_index(drop = True)
    title = x.loc[0, "title"]
    artist = x.loc[0, "artistName"]
    return artist, title

def set_axes(ax, image_name, query = False, **kwargs):
    value = kwargs.get("value", None)
    model = kwargs.get("model", None)
    artist, title = get_label(image_name)
    title = '\n'.join(wrap(title, 50))
    if query:
        ax.set_xlabel("{2} Query Image\n{0}\n{1}".format(artist, title, model.replace("_", " ").title()), fontsize = 12)
    else:
        ax.set_xlabel("Similarity value {2:1.3f}\n{0}\n{1}".format(artist, title, value), fontsize = 12)
    ax.set_xticks([])
    ax.set_yticks([])
    
