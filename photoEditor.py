from PIL import Image, ImageEnhance, ImageFilter
import os

# Your code here


path = './PhotosBefore'
pathOut = './Editedphotos'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # Apply the sharpen filter
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    # Extract the clean name without the file extension
    clean_name = os.path.splitext(filename)[0]

    # Save the edited image without the dot before pathOut
    edit.save(f'{pathOut}/{clean_name}_edited.jpg')
