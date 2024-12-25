import requests
import os
import zipfile
from zipfile import ZipFile
download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def main():
    #zipped_csvs = []
    path = 'downloads'
    list_directories = os.listdir(path=os.getcwd())
    print(list_directories)
    if path not in list_directories:    
        os.mkdir(path)
    os.chdir(path)
    print('helloWorld')
    for uri in download_uris:
        zip_name = uri.split('https://divvy-tripdata.s3.amazonaws.com/')[1]
        r = requests.get(uri)

        with open(zip_name, 'wb') as file:
            file.write(r.content)

        if zipfile.is_zipfile(zip_name):
            with ZipFile(zip_name) as myzip:
                myzip.extractall()
                print(list_directories)
        os.remove(zip_name)     

        print('done')
if __name__ == "__main__":
    main()
