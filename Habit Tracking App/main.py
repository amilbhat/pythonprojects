import requests
from datetime import datetime
USERNAME = "ENTER YOUR USERNAME"
TOKEN = "MAKE A NEW TOKEN"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users" 

user_params = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

########################### For Creating Account ####################
# response  = requests.post(url = pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID ,
    "name": " Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"   
} 

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ################################# Updating the data 

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")

pixel_creation_config = {
    "date" : today,
    "quantity": input("How many kilometers did you cycle today? "),

}

# response  = requests.post(url = pixel_creation_endpoint, json = pixel_creation_config, headers=headers)
# print(response.text)

################################## Updating the existing Data

pixel_update_endpoint  = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

pixel_update_data = {
    "quantity": "15"
}

# response = requests.put(url = pixel_update_endpoint, json = pixel_update_data, headers=headers)
# print(response.text)

# ############################### Deleting The Pixel

pixel_delete_endpoint  = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# response = requests.delete(url = pixel_update_endpoint, headers=headers)
# print(response.text)
