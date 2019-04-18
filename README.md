# Are Google Earth Engine anaylses reproducible?

## Setup

```
conda env create -n earthengine -f environment.yml
source activate earthengine
earthengine authenticate
```

## Execute

```
python test.py
```

## Roadmap

 * ~~Identify file objects~~
 * ~~Perform an analysis (on the EE platform)~~
 * ~~Return file objects~~
 * Generate comparable file objects (not through EE)?
 * Reproduce analysis (un-authenticated with EE)

## Notes

### Available datasets

https://developers.google.com/earth-engine/datasets/

### Further reading

https://geoscripting-wur.github.io/Earth_Engine/
