from PIL import Image
import time
path = 'Test.png'
img = Image.open(path)
img.show()
time.sleep(1)
img.close()