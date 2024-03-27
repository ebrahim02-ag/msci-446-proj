 
## MSCI 446 Group Project - Predicting Animal Endangerment Status: 	Dataset Design & Benchmarking

## Final Dataset: final_dataset.csv

## Goals of this project

- Collect diverse wildlife data to create a dataset
- Assess the performance of ML algorithms on the dataset
- Demonstrate the dataset's utility
- Ensure accessibility for future researchers 
- Enable discovery of information about the current biodiversity crisis.

## Depenendencies
- pandas
- matplotlib
- numpy 
- rasterio
- seaborn

## Files
####  climate.csv 
 - create a csv file from the bioclamtic variables of every Canadian province by using the geotiff
 files from worldclimV2

#### data_process.ipynb 
- Load and preprocess the CAN-SAR data, map the bioclamatic data and clean it up to create the final dataset

#### benchmark.ipynb
- Benchmarking ML models on the final dataset

## Data Sources: 
- https://www.worldclim.com/version2 
- https://osf.io/e4a58/ 


#### additional data files: 
- data-processes/Can-SAR_data_dictionary.xlsx : dictionary of all the column's descriptions in CAN-SAR 
- data-processes/CAN-SAR_database.csv : original Cansar data
- data-processes/climate.csv: climate.py output after porcessing worldclimV2