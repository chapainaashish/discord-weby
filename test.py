
import json
import requests
url = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases2_v1/FeatureServer/2/query?where=Country_Region%20%3D%20'NEPAL'&outFields=Country_Region,Last_Update,Lat,Confirmed,Deaths,Recovered,Active,Incident_Rate,People_Tested,Mortality_Rate,People_Hospitalized&outSR=4326&f=json"
response = requests.get(url)
print(response.json()["features"][0]["attributes"])

# print(json.dumps(response.json()["features"][0]["attributes"], indent=4))
