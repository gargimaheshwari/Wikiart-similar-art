from PIL import Image
import os
from torchvision import transforms

def resizer():
    resize = transforms.Compose([transforms.Resize((224,224))])

    directory = "images"
    os.makedirs("resized", exist_ok = True)

    print("Resizing images to (224, 224) and saving")
    for file in os.listdir(directory):
        img = Image.open(os.path.join(directory, file))
        new_img = resize(img)
        new_img.save(os.path.join("resized", file))
        new_img.close()
        img.close()