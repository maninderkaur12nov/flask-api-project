import pandas as pd
import requests 
from sqlalchemy import create_engine 
import urllib

url ="https://wttr.in/London?format=j1"
response=requests.get(url)
data=response.json()
# print(response.status_code)
# print(response.text)
# print("Current temperature in London:", data['current_condition'][0]['temp_C'], "°C")
# print("🌡️ Temperature (°C):", data['current_condition'][0]['temp_C'])
# if 'current_condition' in data:
#     condition = data['current_condition'][0]
#     if 'weatherDesc' in condition:
#         print("☁️ Weather:", condition['weatherDesc'][0]['value'])
#     else:
#         print("No weather description available.")
# else:
#     print("No current condition data found.")

params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-SUJ2P8G\\MSSQLSERVER1;"
    "DATABASE=test1;"
    "Trusted_Connection=yes;"
)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
  


# Load into table (overwrite or append)
current=data['current_condition']
# Flatten it
df_flat = pd.json_normalize(current)
df_flat.to_sql('CurrentCondition', con=engine, if_exists='replace', index=False)
# print("💧 Humidity (%):", data['humidity'])
# print("☁️ Weather:", data['current_condition'][0]['weatherDesc'][0]['value'])
# print("💨 Wind Speed (km/h):", data['windspeedKmph'])
# print("🔆 UV Index:", data['uvIndex'])
# print("🌧️ Chance of Rain (%):", data['chanceofrain'])

# rates=data['rates']
# df=pd.DataFrame(list(rates.item()),columns=['currency','rates'])
# df['Base']=data['base']
# df['Date']=data['date']
# print("Extracteddata")
# print(df.head())
