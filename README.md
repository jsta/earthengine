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

 * Identify file objects
 * Perform an analysis (on the EE platform)
 * Return file objects
 * Generate comparable file objects (not through EE)
 * Reproduce analysis (un-authenticated with EE)

File objects can only be returned to Google Drive (and opaque Earth Engine repository objects). See [PyDrive](https://github.com/gsuitedevs/PyDrive)

