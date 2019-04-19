import ee
import pandas as pd
from ee import batch
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import skimage
import matplotlib.pyplot as plt

rocks = skimage.io.imread('out55.tif')
rocks_greyscale = skimage.color.rgb2gray(rocks)

edge_sobel = skimage.filters.sobel(rocks)


fig, ax = plt.subplots(ncols=1, sharex=True, sharey=True,
                       figsize=(8, 4))

ax.imshow(edge_sobel, cmap=plt.cm.gray)
ax.axis('off')

plt.tight_layout()
plt.show()



ee.Initialize()

# get image
# path: 21 # row: 31 # date: jan262019 # doy:26
image = ee.Image('LANDSAT/LC08/C01/T1/LC08_021031_20190126').select('B8')
# print(image.getInfo())

# run an ee data analysis function
canny = ee.Algorithms.CannyEdgeDetector(image, 10, 1)

# define bbox
# bbox = ee.Geometry.Rectangle([-85.4664, 42.3693, -85.3717, 42.4645])
out1 = batch.Export.image.toDrive(canny, description = 'out55', 
                                  scale = 30, region=([-85.4664, 42.36926], [-85.37169, 42.36926], [-85.37169, 42.46446], [-85.4664, 42.46446], [-85.4664, 42.36926]))
process = batch.Task.start(out1)

# pull file from GDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

(file_list = drive.ListFile({'q': "'root' in parents and trashed=false"})
    .GetList())
file_position = np.min(np.where(
    [file1['title'] == "out55.tif" for file1 in file_list]))
file_id = file_list[file_position]['id']

file1 = drive.CreateFile({'id':file_id})
file1.GetContentFile('out55.tif')
