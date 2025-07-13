
from PIL import Image

def from_images(input_paths, output_path):
    images = []
    for path in input_paths:
        img = Image.open(path)
        img = img.convert('RGB')
        images.append(img)

    if images:
        images[0].save(output_path, save_all=True, append_images=images[1:])
