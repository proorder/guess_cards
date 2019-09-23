import os

def Reformat_Image(ImageFile):
    from PIL import Image
    image = Image.open('./Pl/' + ImageFile, 'r')
    image_size = image.size
    width = image_size[0]
    height = image_size[1]

    background = Image.new('RGBA', (width, height+24), (255, 255, 255, 0))

    offset = (0, 12)
    background.paste(image, offset)
    background.save('./PZ/' + ImageFile)

files = os.listdir('Pl')
for file in files:
    if file != '.DS_Store':
        Reformat_Image(file)
