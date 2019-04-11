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

## Results

File objects can only be returned to Google Drive (and opaque Earth Engine repository objects). See [PyDrive](https://github.com/gsuitedevs/PyDrive)


