# 2018 ZIP code to 2019 CBSA

This is a mapping of United States Postal Service (USPS) ZIP codes to Core-Based Statistical Areas defined by the Office of Management and Budget. While there are clear limitations to the correctness of the approach used here, it should get you 99% of the way. See also: [https://www.huduser.gov/portal/datasets/usps_crosswalk.html](https://www.huduser.gov/portal/datasets/usps_crosswalk.html).

## Creating the .xlsx/.csv File

The following assumes you are using `conda` as your Python package manager. Open a terminal, navigate to this repository, and: 

```
conda env create -n cbsa python=3.8 openpyxl requests geopandas tqdm -y
conda activate cbsa
python zip_to_cbsa.py
```

Those steps will download the data needed from census.gov to './data', and create the files `US_ZIP_CBSA.xlsx`/`US_ZIP_CBSA.csv`.
