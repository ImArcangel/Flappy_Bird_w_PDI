import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

filename = 'sample.jpg'

img = cv.imread(filename, cv.IMREAD_UNCHANGED)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# r = cv.selectROI('Seleccionar muestra', cv.cvtColor(img, cv.COLOR_RGB2BGR), False, False)
# cv.destroyAllWindows()
# if r == (0,0,0,0):
#     print('Muestra no seleccionada')
#     quit()

# crop = img[int(r[1]) : int(r[1] + r[3]), int(r[0]) : int(r[0] + r[2])]
# crop = cv.resize(crop, None, fx = 1, fy = 1, interpolation = cv.INTER_CUBIC)

# color = crop.sum(0)
# print(img)
# print('\n\n')
# print(color)

# plt.figure()
# plt.imshow(crop)
# plt.show()

cv.waitKey(0)
cv.destroyAllWindows()