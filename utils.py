import numpy as np
from PIL import Image
from os import walk
from model import generator_model
from utils import load_image, deprocess_image, preprocess_image
import glob
path = './images/test/'
def depth(image_path):
    data = {
        'A_paths': [path + image_path],
        'A': np.array([preprocess_image(load_image(path + image_path))])
    }
    x_test = data['A']
    g = generator_model()
    g.load_weights('generator.h5')
    generated_images = g.predict(x=rgb2gray(x_test))
    generated = np.array([deprocess_image(img) for img in generated_images])
    x_test = deprocess_image(x_test)
    
    for i in range(generated_images.shape[0]):
        x = x_test[i, :, :, :]
        img = generated[i, :, :, :]
        #img=rgb2gray(img)
        output = img
        im = Image.fromarray(output.astype(np.uint8))
        im.save('./images/out/'+image_path)
def rgb2gray(rgb):
    print(rgb.shape)
    r, g, b = rgb[:,:,:,0], rgb[:,:,:,1], rgb[:,:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    gray=np.stack((gray,)*3, -1)
    return gray

def deblur_command(image_path):
    
    return deblur(image_path)


if __name__ == "__main__":
    fs = []
    for (dirpath, dirnames, filenames) in walk(path):
        fs = (filenames)
    for f in fs:
        depth(f)