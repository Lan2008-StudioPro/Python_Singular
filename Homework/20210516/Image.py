from PIL import Image
import time

img = Image.open('Photo.jpg')
img.show()
time.sleep(1)
img.close()