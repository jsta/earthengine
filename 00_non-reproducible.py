from pathlib import Path
import ee
import numpy as np
from ee import batch
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

if not Path("raw_export.tif").is_file() or not Path("canny.tif").is_file():
    ee.Initialize()
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    # get image # path: 21 # row: 31 # date: jan262019 # doy:26
    image = ee.Image('LANDSAT/LC08/C01/T1/LC08_021031_20190126').select('B8')
    # print(image.getInfo())

    raw_export = batch.Export.image.toDrive(image, description = 'raw_export', 
                                    scale = 30, region=([-85.4664, 42.36926], [-85.37169, 42.36926], [-85.37169, 42.46446], [-85.4664, 42.46446], [-85.4664, 42.36926]))
    batch.Task.start(raw_export)

    # pull file from GDrive
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    file_position = np.min(np.where(
        [file1['title'] == "raw_export.tif" for file1 in file_list]))
    file_id = file_list[file_position]['id']
    file1 = drive.CreateFile({'id':file_id})
    file1.GetContentFile('raw_export.tif')


    # run an ee data analysis function
    canny = ee.Algorithms.CannyEdgeDetector(image, 10, 1)

    canny_export = batch.Export.image.toDrive(canny, description = 'canny', 
                                    scale = 30, region=([-85.4664, 42.36926], [-85.37169, 42.36926], [-85.37169, 42.46446], [-85.4664, 42.46446], [-85.4664, 42.36926]))
    batch.Task.start(canny_export)

    # pull file from GDrive
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    file_position = np.min(np.where(
        [file1['title'] == "canny.tif" for file1 in file_list]))
    file_id = file_list[file_position]['id']
    file1 = drive.CreateFile({'id':file_id})
    file1.GetContentFile('canny.tif')
