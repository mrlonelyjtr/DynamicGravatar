from PIL import Image
from images2gif import writeGif

names = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png',
         '7.png', '8.png', '9.png', '10.png', '11.png']

lists = names[:]
names.pop()
names.reverse()
names.pop()
for name in names:
    lists.append(name)

# read the png files
images = [Image.open(list) for list in lists]

# generate the gif file
writeGif('matianyao.gif', images, duration=0.2)