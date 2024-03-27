'''
This script reads the climate data from the WorldClim dataset and extracts the data for the Canadian provinces and territories.
'''

import rasterio
import numpy as np
import os 
import csv 

datasets = {}

# Locations of the provinces and territories in Canada
locations = {
  'BC': {'lat': 53.73, 'long': -127.65, 'variables': {}},
  'AB': {'lat': 55.00, 'long': -115.00, 'variables': {}},
  'SK': {'lat': 55.00, 'long': -106.00, 'variables': {}},
  'MB': {'lat': 56.42, 'long': -98.74, 'variables': {}},
  'ON': {'lat': 50.00, 'long': -85.00, 'variables': {}},
  'QC': {'lat': 53.00, 'long': -70.00, 'variables': {}},
  'NB': {'lat': 46.50, 'long': -66.16, 'variables': {}},
  'PE': {'lat': 46.25, 'long': -63.00, 'variables': {}},
  'NS': {'lat': 44.89, 'long': -63.00, 'variables': {}},
  'NL': {'lat': 53.14, 'long': -57.66, 'variables': {}},
  'YT': {'lat': 65.00, 'long': -135.00, 'variables': {}},
  'NT': {'lat': 63.59, 'long': -115.51, 'variables': {}},
  'NU': {'lat': 65.04, 'long': -92.55, 'variables': {}},
}

# Load the tif files after downloading the data from the WorldClim website https://www.worldclim.com/version2
def load_tif_files(folder): 
  for filename in os.listdir(folder):
    if filename.endswith(".tif"):
      dataset = rasterio.open(os.path.join(folder, filename))
      name = filename.split('5m_')[1]
      name = name.split('.tif')[0]
      datasets[name] = dataset

# Populate the locations with the climate data
def populate_locations(): 
  for key, ds in datasets.items():
    band1 = ds.read(1)
    for loc in locations:
      lat = locations[loc]['lat']
      long = locations[loc]['long']
      x, y = ds.index(long, lat)
      locations[loc]['variables'][key] = band1[x, y]

# Save the data as a csv file
def save_as_csv(): 
  headers = ['location', 'lat', 'long']
  headers.extend(datasets.keys())
  with open('climate.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    for loc in locations:
      row = [loc, locations[loc]['lat'], locations[loc]['long']]
      for key in datasets.keys():
        row.append(locations[loc]['variables'][key])
      csv_writer.writerow(row)
    

if __name__ == "__main__":
  folder = 'wc2.1_5m_bio'
  load_tif_files(folder)
  populate_locations()
  save_as_csv()
