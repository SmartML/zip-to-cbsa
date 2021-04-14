import requests
import zipfile
import os

import geopandas as gpd

from tqdm import tqdm


DATA_PATH = os.path.join(os.getcwd(), "data")

# download archives containing shapefiles
url_cbsa = "https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_cbsa_500k.zip" 
url_zip = "https://www2.census.gov/geo/tiger/TIGER2019/ZCTA5/tl_2019_us_zcta510.zip" 

response = requests.get(url_cbsa, stream=True)
total_size_in_bytes= int(response.headers.get('content-length', 0))
block_size = 1024
progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
with open(os.path.join(DATA_PATH, 'cb_2018_us_cbsa_500k.zip'), 'wb') as file:
    for data in response.iter_content(block_size):
        progress_bar.update(len(data))
        file.write(data)
progress_bar.close()

response = requests.get(url_zip, stream=True)
total_size_in_bytes= int(response.headers.get('content-length', 0))
progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
with open(os.path.join(DATA_PATH, 'tl_2019_us_zcta510.zip'), 'wb') as file:
    for data in response.iter_content(block_size):
        progress_bar.update(len(data))
        file.write(data)
progress_bar.close()

# extract the downloaded zip files
for file in os.listdir(DATA_PATH):
    if zipfile.is_zipfile(os.path.join(DATA_PATH, file)): 
        with zipfile.ZipFile(os.path.join(DATA_PATH, file)) as item: 
           item.extractall(path=DATA_PATH)

# read into geopandas, spatial join
us_zip = gpd.read_file(os.path.join(DATA_PATH, 'tl_2019_us_zcta510.shp'))
us_cbsa_500k = gpd.read_file(os.path.join(DATA_PATH, 'cb_2018_us_cbsa_500k.shp'))

us_zip_cbsa = gpd.sjoin(us_zip,
                        us_cbsa_500k[['NAME', 'CBSAFP', 'geometry']],
                        how="left",
                        op='intersects')

cols = ['ZCTA5CE10', 'NAME', 'CBSAFP']
us_zip_cbsa = us_zip_cbsa.reset_index()[cols]

# save as Excel/csv file
us_zip_cbsa.to_excel('US_ZIP_CBSA.xlsx', sheet_name='zip_to_cbsa')
us_zip_cbsa.to_csv('US_ZIP_CBSA.csv')