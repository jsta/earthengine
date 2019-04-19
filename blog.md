
# Are Google Earth Engine analyses reproducible?

## Summary

More and more research papers are making use of Google Earth Engine (EE) to do geocomputation with gridded data and satellite (remote sensing) output. Are these analyses reproducible? Will they be reproducible in 2-3 years? If a paper uses EE to simply pull/crop/extract data they answer is likely yes. If a paper uses any computation functions then the analyses have a hard dependency on the EE remote servers remaining in operation. Should they go away, the paper will no longer be reproducible. In the following **Walthrough** section we'll step through both of these approaches.

## Dependencies

Before we begin let's set up our python environment and initialize EE where python dependencies are:

- python=3.7.3
- earthengine-api
- grass-session 

```
conda env create -n earthengine -f environment.yml
source activate earthengine
earthengine authenticate
```

## Walkthrough



It's obnoxious that I have to go to the code editor to read the docs (argument descriptions)
No native python docs exist bc the code editor is soley js
The docs don't have code examples...

### Find path and row of landsat scene
https://landsat.usgs.gov/landsat_acq#convertPathRow

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
