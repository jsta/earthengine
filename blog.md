
# Are Google Earth Engine analyses reproducible?

## Summary

More and more research papers are making use of Google Earth Engine (EE) to do geocomputation with gridded data and satellite (remote sensing) output. Are these analyses reproducible? Will they be reproducible in 2-3 years? In the following blog post, I explore these questions and conclude that:

* If a paper uses EE to simply pull/crop/extract data they answer is likely yes. 

* If a paper uses any computation functions then the analyses have a hard dependency on the EE remote servers. Should they go away, the paper will no longer be reproducible. 

## Dependencies

Before we begin let's set up our python environment and initialize EE where [python dependencies](environment.yml) are:

- python=3.7.3
- earthengine-api        
- pydrive
- numpy
- scikit-image        

```
conda env create -n earthengine -f environment.yml
source activate earthengine
earthengine authenticate
```

## Walkthrough

First, we must manually initialize EE and connect `pydrive`:

```
ee.Initialize()
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
```

Then we need to identify an EE image product. We will focus on the Landsat 8 panchromatic band product and select a tile overlapping Gull Lake Michigan (path: 21, row: 31, date: 2019-01-26). You can find the path and row numbers an arbitrary region of interest using [this tool](https://landsat.usgs.gov/landsat_acq#convertPathRow). The scenario here is that we will attempt to extract the coastline of Gull Lake using an EE workflow. Note that save the raw data to Google Drive clipped to a bounding box around the Gull Lake watershed using the `region` argument of `batch.Export.image.toDrive`.

```
image = ee.Image('LANDSAT/LC08/C01/T1/LC08_021031_20190126').select('B8')
raw_export = batch.Export.image.toDrive(image, description = 'raw_export', 
                                    scale = 30, region=([-85.4664, 42.36926], [-85.37169, 42.36926], [-85.37169, 42.46446], [-85.4664, 42.46446], [-85.4664, 42.36926]))
batch.Task.start(raw_export)
```

Next, we can pull the results from Drive to our local machine using some `pydrive` commands:

```
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
file_position = np.min(np.where(
    [file1['title'] == "raw_export.tif" for file1 in file_list]))
file_id = file_list[file_position]['id']
file1 = drive.CreateFile({'id':file_id})
file1.GetContentFile('raw_export.tif')
```

![](comparison.png)

It's obnoxious that I have to go to the code editor to read the docs (argument descriptions)
No native python docs exist bc the code editor is soley js
The docs don't have code examples...

### Find path and row of landsat scene
https://landsat.usgs.gov/landsat_acq#convertPathRow
https://developers.google.com/earth-engine/datasets/

## Recommendations

### Use EE as a remote data source not a computation platform

I was able to reproduce data fetching code from 2016 that uses legacy formatting of Landsat file names (https://github.com/acgeospatial/GoogleEarthEnginePy/blob/master/OrderData.py).

gdal has tools for finding and downloading from ee!
https://www.gdal.org/drv_eeda.html

## Further reading

https://geohackweek.github.io/raster/04-workingwithrasters/
https://gis.stackexchange.com/a/297042/32531
https://developers.google.com/earth-engine/datasets/
https://geoscripting-wur.github.io/Earth_Engine/
