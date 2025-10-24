from rembg import remove
from PIL import Image


input = Image.open('leo.png')

output = remove(input)

output.save('out.png')