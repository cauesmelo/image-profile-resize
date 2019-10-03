from PIL import Image, ImageCms
import glob
import os
import numpy

images = glob.glob('RGB/*.jpg')

try:
    print("Criando diretório...")
    os.mkdir('CMYK/ECOM')
except:
    print("Diretorio já existente.\n\n")

SIZE_LIMIT = 1

LIMIT = True

for image in images:
    quality = 100
    os.system("clear")
    print("CONVERTENDO IMAGENS DE RGB PARA CMYK")
    print("Total de imagens na pasta -> " + str(len(images)))
    print("Total de imagens convertidas -> " + str(images.index(image)) + '(' + '{:.2f}'.format((100*images.index(image))/len(images)) + '%)')
    print("Convertendo - " + image[4:])
    img = Image.open(image)
    img = ImageCms.profileToProfile(img, 'icc/sRGB.icc', 'icc/CMYK.icc', renderingIntent=0, outputMode='CMYK')
    new_img = 'CMYK/' + image[4:]
    img.save(new_img, quality=quality)
    size = round(os.stat(new_img).st_size / 1000000, 2)
    if(LIMIT):
        while size > SIZE_LIMIT:
            img = img.resize(tuple(numpy.subtract(img.size, (200, 200))), Image.ANTIALIAS)
            quality = quality - 5
            img.save(new_img, quality=quality)
            size = round(os.stat(new_img).st_size / 1000000, 2)
            print('Imagem convertida -> ' + image[4:] + (' ' * (8 - len(image[4:]))) + ' ||  Tamanho: ' + '{:.2f}'.format(size) + 'mb  ||  Dimensão: ' + str(img.size) + '   ||   Qualidade: ' + str(quality))
    else:
        img.save(new_img, quality=quality)
        size = round(os.stat(new_img).st_size / 1000000, 2)
        print('Imagem convertida -> ' + image[4:] + (' ' * (8 - len(image[4:]))) + ' ||  Tamanho: ' + '{:.2f}'.format(size) + 'mb  ||  Dimensão: ' + str(img.size) + '   ||   Qualidade: ' + str(quality))

print("=====FINALIZADO=====")