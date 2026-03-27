# importing modules
import urllib.request
from PIL import Image, ImageStat

urllib.request.urlretrieve(
  'https://static.wikia.nocookie.net/blinks/images/0/02/Ruby_Teaser_Jennie_%282%29.jpg/revision/latest?cb=20250228112123',
   "jenie.jpg")

img_jenie = Image.open("jenie.jpg")
#img_jenie.show()

#------
# grayscale

# Convert the image to grayscale. The `"L"` argument in Pillow represents grayscale mode.
grayscale_image = img_jenie.convert("L")

# Save the grayscale image
grayscale_image.save("grayscale_image_jenie.jpg")
#grayscale_image.show()

#----------------------
# brightness mean
from PIL import ImageStat

def brightness( im_file ):
   im = Image.open(im_file)
   stat = ImageStat.Stat(im)
   return stat.mean[0]


Average_brigh = brightness("grayscale_image_jenie.jpg")
print(Average_brigh)
