import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import zlib
img = Image.open('4202252.jpg')
data = np.array(img)

#plt.pcolor(data[...,3])
#plt.colorbar()
#plt.show()
alpha = data[...,2]
secret = alpha[alpha != 255]
stream = ''.join(map(chr, secret))
print("stream is :: " + stream)
print("decoded Message is  :: "+zlib.decompress(stream[::-1].decode('base64'), 16+zlib.MAX_WBITS))
