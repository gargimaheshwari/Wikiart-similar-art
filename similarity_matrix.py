import sys
import getopt
from vectorize import img2vec_converter
from cos_sim import matrix_calculator
from top_similar import top10
from pathlib import Path
import os
import pickle

cuda= False
model = "resnet18"

try:
    opts, args = getopt.getopt(sys.argv[1:], "c:m:h", ['cuda=', 'model=', 'help'])
except getopt.GetoptError:
    print("Usage: python <filename.py> -c cuda -m model")
    print("cuda = (True, False)\nDefault CUDA status: False")
    print("To see available models use -h or --help")
    sys.exit(2)
if not opts:
    print("Using default options. Model: resnet18, Cuda: False")
else:
    c = True
    m = True
    for opt, arg in opts:
        if opt in ('-c', '--cuda'):
            c = False
            cuda = arg
        elif opt in ('-m', '--model'):
            m = False
            model = arg
        elif opt in ('-h', '--help'):
            print("Usage: python <filename.py> -c cuda -m model")
            print("cuda = (True, False)\nDefault CUDA status: False")
            print("Available models: resnet18, resnet34, resnext, wide_resnet, alexnet\nDefault model: resnet18")
            sys.exit()
        else:
            print("Check your arguments")
            sys.exit(2)
    if c:
        print("CUDA not given. Using CPU")
    if m:
        print("No model given. Using default: resnet18")

matrix = matrix_calculator(img2vec_converter(model, cuda))

print("Saving cosine similarity matrix")
path_output = Path("sim_matrix.pkl")
file = open(os.path.join("pickles", model, path_output), 'wb')
pickle.dump(matrix, file)
file.close()

top10(matrix, model)