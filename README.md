# Art Recommendation system

This is the repository of a portfolio project at [DSR](https://datascienceretreat.com/). This project aims to identify similar images using pre-trained computer vision networks. For an explanation of the technology see the [technology section](#tech).

## <a name="contributors"></a>Contributors
* [Catarina Ferreira](https://github.com/Naycat)
* [Gargi Maheshwari](https://github.com/gargimaheshwari)

## <a name="setup"></a>Setup

We recommend to set up a virtual environment using a tool like [Virtualenv](https://virtualenv.pypa.io/en/latest/).

Clone this repo
```
git clone https://github.com/gargimaheshwari/art-recommendation
```
and install dependencies.
```
pip install -r requirements.txt
```
## <a name="data"></a>Generate Data

Before running the model, you will need to generate the data. Clone the repo at `https://github.com/lucasdavid/wikiart` and run the json downloader.

```
git clone https://github.com/lucasdavid/wikiart
python wikiart/wikiart.py
```
The directory structure should look as follows:

```
art-recommendation
├── wikiart
└── wikiart-saved
    ├── images
    └── meta
```

While the repo at wikiart is supposed to download the images along with the data, it didn't work for us. The images folder remains empty, but we did get all the json files in the folder named meta.

Download the images:
```
python download.py
# Or
python download.py -n [NUMBER] # this downloads only the first n images
# use -h for help
```
This will save the metadata as a pickle file in a folder called pickles, the images in an images folder, and all images resized to 224x224 in a folder called resized.

```
art-recommendation
├── images
├── pickles
├── resized
├── wikiart
└── wikiart-saved
    ├── images
    └── meta
```
You are now ready to run the model.

## <a name="run"></a>Run model

The beauty of this model is that it requires no training. Once the data has been downloaded we can convert the images to vectors and make calculations right away. To do this, run:

```
python similarity_matrix.py -c [CUDA] -m [MODEL]
# use -h for help with available models
```
The app runs on both CPU and GPU, however the use of a GPU with CUDA is higly recommended. If you have a GPU with CUDA make sure to have the proper card drivers and CUDA installed.

The images have now been converted to vectors\*, which have been used to calculate similarity matrices\*. The top ten similar images for each image have been extracted and their names and similarity values stored\*.

\* saved as .pkl files in `pickles` folder.

## <a name="plot"></a>Plot similar images

You can now plot similar images for any image using the command
```
python plot_similar.py -i [IMAGE NAME] -m [MODEL]
# for image name format and available models use -h
```
The plots for similar images are stored in `similar_images` folder.
```
art-recommendation
├── images
├── pickles
├── resized
├── similar_images
├── wikiart
└── wikiart-saved
    ├── images
    └── meta
```
Sample saved image:
![Eugene Boudin](https://i.imgur.com/gbvltc2.jpg)



## <a name="tech"></a>Technology Used

to-do
