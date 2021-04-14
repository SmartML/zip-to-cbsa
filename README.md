# ZIP code to CBSA

This is a mapping of United States Postal Service (USPS) ZIP codes to Core-Based Statistical Areas defined by the Office of Management and Budget. We are using the shapefiles for [year 2018 Core Based Statistical Areas](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html) and [year 2019 ZIP Code Tabulation Areas following the 2010 Census](https://catalog.data.gov/dataset/tiger-line-shapefile-2019-2010-nation-u-s-2010-census-5-digit-zip-code-tabulation-area-zcta5-na), and do a geospatial join. The result is saved in both Excel and .csv formats, `US_ZIP_CBSA.xlsx`/`US_ZIP_CBSA.csv`. While there are clear limitations to the correctness of this approach, e.g. ZIP codes change, it should get you 99% of the way. See also: [https://www.huduser.gov/portal/datasets/usps_crosswalk.html](https://www.huduser.gov/portal/datasets/usps_crosswalk.html).

## Creating the .xlsx/.csv File

The following assumes you are using `conda` as your Python package manager. Open a terminal, navigate to this repository, and: 

```
conda create -n cbsa python=3.8 openpyxl requests geopandas tqdm -y
conda activate cbsa
python zip_to_cbsa.py
```

Those steps will create and activate the environment, download and unpack the data needed from census.gov to './data', and create the files `US_ZIP_CBSA.xlsx`/`US_ZIP_CBSA.csv`.
