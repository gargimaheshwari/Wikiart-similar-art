import pandas as pd
import os

def jsonloader():
    df = []
    print("Converting json files to dataframe")
    for file in os.listdir(os.path.join("wikiart-saved", "meta")):
        if (file == "artists.json"):
            continue
        df.append(pd.read_json(os.path.join("wikiart-saved", "meta", file), orient = "records", encoding = "utf-8"))

    jsondata = pd.concat(df, ignore_index = True, axis = 0, sort = False)

    print("Number of images, metadata fields of each image: " + str(jsondata.shape))

    import pickle
    print("Saving metadata")
    os.makedirs("pickles", exist_ok = True)
    file = open(os.path.join("pickles", "jsondata.pkl"), 'wb')
    pickle.dump(jsondata, file)
    file.close()
    
    return jsondata

# Download images
from skimage import io
from PIL import Image
from urllib import error
import urllib.parse as up
import numpy as np
from tqdm import tqdm

def httpe(link):
    try:
        img = io.imread(link[:-10], as_gray = False)
    except error.HTTPError:
        try:
            img = io.imread(link[:-11], as_gray = False)
        except error.HTTPError:
            try:
                img = io.imread(link[:-13], as_gray = False)
            except:
                img = np.full((2,2), np.nan)
                print(str(i)+" image not found")
    except:
        img = np.full((2,2), np.nan)
        print(str(i) + ": problem with download")
    return img

os.makedirs("images", exist_ok = True)

def downloader(n, jsondata):
    if n:
        num_images = n
    else:
        num_images = jsondata.shape[0]
    
    print("Downloading images")
    for i in tqdm(range(num_images)):
        link = jsondata.loc[i, "image"]
        name = jsondata.loc[i, "url"]
        artist = jsondata.loc[i, "artistUrl"]

        try:
            img = io.imread(link, as_gray = False)
        except UnicodeEncodeError as err:
            link = up.quote(link, safe="!/:")
            try:
                img = io.imread(link, as_gray = False)
            except error.HTTPError as e:
                img = httpe(link)
        except error.HTTPError as e:
            img = httpe(link)
        except:
            print(str(i) + ": problems with imread")
            continue

        if pd.isna(img).all():
            continue

        out = Image.fromarray(img)
        out.save(os.path.join("images", artist+"_"+name+".png"))
        out.close()
    
    num_downloaded = len(os.listdir("images"))
    assert num_downloaded == num_images
    
    print("\nNumber of images downloaded: " + \
        str(num_downloaded))