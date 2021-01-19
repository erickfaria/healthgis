# Python Script for geocoding the addresses of health facilities

# Author: Erick de Oliveira Faria (https://orcid.org/0000-0003-0089-9602)

import pandas as pd
import geopy as gp
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Bing
from tqdm import tqdm
import os

# Set the directory and file name

path = ('E:\\Annuaire Santé')

os.chdir(path)

file =  pd.read_csv('medecins_france.txt', sep='\t')

geolocator = Bing(api_key='your_api_here')

geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
tqdm.pandas()
file['coord'] = file.iloc[:,1].apply(geocode)
file['point'] = file['coord'].apply(lambda loc: tuple(loc.point) if loc else None)

file_geocodage.to_csv('medecins_france.txt', sep='\t', index=False)