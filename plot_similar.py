import os
import sys
import getopt
import matplotlib.pyplot as plt
from getsimilar import get_images
from plotfunctions import get_image, add_border, set_axes

models = [m for m in os.listdir("pickles") if os.path.isdir(os.path.join("pickles", m)) & (m != '.ipynb_checkpoints')]
model = models[0]

try:
    opts, args = getopt.getopt(sys.argv[1:], "i:m:h", ['image=', 'model=', 'help'])
except getopt.GetoptError:
    print("Usage: python <filename.py> -i image -m model")
    print("Name of the image should be in the format: artist-name_image-name[.png]")
    print("To see available models use -h or --help")
    sys.exit(2)
if not opts:
    print("Image name is required")
    sys.exit(2)
else:    
    for opt, arg in opts:
        if opt in ('-i', '--image'):
            input_image = arg
        elif opt in ('-m', '--model'):
            model = arg
        elif opt in ('-h', '--help'):
            print("Usage: python <filename.py> -i image -m model")
            print("Name of the image should be in the format: artist-name_image-name[.png]")
            print("Available models: {0}\nDefault model: {1}".format((', '.join(models)), model))
            sys.exit()
        else:
            print("Check your arguments")
            sys.exit(2)

folder = "similar_images"
os.makedirs(folder, exist_ok = True)

input_image, images, values = get_images(input_image, model)

columns = 3
rows = 3

print("Creating figure")
fig = plt.figure(figsize=(20, 15))
img = get_image(input_image)
img = add_border(img, 12)
ax = fig.add_subplot(rows, columns, 1)
set_axes(ax, input_image, query = True, model = model)
plt.imshow(img)
img.close()
    
ax = []
    
for j in range(2, 10):
    link = images[j]
    img = get_image(link)
    ax.append(fig.add_subplot(rows, columns, j))
    set_axes(ax[-1], link, value = values[j])
    plt.imshow(img)
    img.close()

plt.subplots_adjust(hspace = 0.45)

print("Saving figure")
plt.savefig(os.path.join(folder, input_image), dpi = 300, bbox_inches = 'tight')
plt.clf()

print("Figure with top similar images stored in {0} folder as {1}".format(folder, input_image))