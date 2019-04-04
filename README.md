![Imgur](https://i.imgur.com/iEWAtkS.gif?1)

# MerOCenv: Web Python-environment

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/carmelosammarco/MerOCenv/master?urlpath=lab/tree/Notebook/MerOC-env.ipynb)  [![Gitter](https://badges.gitter.im/MerOCenv/community.svg)](https://gitter.im/MerOCenv/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)


Python environment created using [MyBinder](https://mybinder.org). The environment contains modules for analyse and manipulate netCDF files which below listed:

- netCDF4
- ftputil
- motuclient
- csv342 
- pandas 
- xarray
- shapely 
- fiona 
- cdo
- nco
- **MerOCenv**: Copy of the [tool4nc](https://github.com/carmelosammarco/tool4nc) python module.

To use this environment just click on the ![Binder](https://mybinder.org/badge_logo.svg) icon on the top of the page. You will be redirected to the project's jupiter-lab web page.

# Case examples:

## I have many netCDF files and I would like to convert all of them in CSV: 

```
import os
from MerOCenv import nctocsv

Input_DIR = 'the/directory/you/want/to/use'
Out_DIR = 'the/directory/you/want/to/use'

for filename in os.listdir(Input_DIR):
    if filename.endswith(".nc"):
       nctocsv (filename, Out_DIR)
```

## I want to overlay in my GIS project (as shape-file) data from a variable which is contained in my netCDF file:

```
import os
from MerOCenv import nctoshape

Input_DIR = 'the/directory/you/want/to/use'
Out_DIR = 'the/directory/you/want/to/use'
Variable = ‘Variable name’

for filename in os.listdir(Input_DIR):
    if filename.endswith(".nc"):
       nctoshape (filename, Out_DIR, Variable)
```

## I have a folder with a month of data divided in daily files. These files are downloaded from the same dataset and I would like to concatenate all the daily files in a montly one:

```
from MerOCenv import concatnc

Input_DIR = 'the/directory/where/you/store/the/daily/file'

concatnc (Input_DIR) #it will generate the concatenated.nc file
```

## I have many netCDF files and I would like to convert all of them in GRD: 

```
import os
from MerOCenv import nctogrd

Input_DIR = 'the/directory/you/want/to/use'
Out_DIR = 'the/directory/you/want/to/use'

for filename in os.listdir(Input_DIR):
    if filename.endswith(".nc"):
       nctogdr (filename, Out_DIR)
```

## I have one year file but i realised that it is better have the data organised by Month. Furthermore, I would like also add a suffix to each file:

```
from MerOCenv import splitnc

Input_file = 'my_input_file.nc'
Out_DIR = 'the/directory/you/want/to/output/the/results'
type = "MONTH"
suffix = "text/to/append/at/each/file"


splitnc (Input_file, Out_DIR, type, suffix)
```
