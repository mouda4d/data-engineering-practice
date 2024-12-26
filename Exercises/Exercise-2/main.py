import requests
import pandas as pd
import os

def main():
    ncei_url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
    dateTimeString = '2024-01-19 10:27'
    response = requests.get(ncei_url)
    #print(response.text)
    with open('NCEI.txt', 'w') as file:
        file.write(response.text)
    
    with open('NCEI.txt', 'r') as file:
        for line in file.readlines():
            #print(line)
            if dateTimeString in line:
                x = line
                break
            
    #print(x)
    csv_name = x[17:32]
    #print(csv_name)
    full_url = ncei_url + csv_name
    response = requests.get(full_url)
    with open(csv_name, 'wb') as file:
        file.write(response.content)
    #print(os.listdir('.'))

    df = pd.read_csv(csv_name)
    #print(df)
    print(df['HourlyDryBulbTemperature'].max())
if __name__ == "__main__":
    main()
