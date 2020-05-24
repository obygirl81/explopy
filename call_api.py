# Use the request library to simplify making a REST API call from pytthon
import requests 

# import json library to read teh data passed back
import json
# Put in key to access my computer Vision Service
SUBSCRIPTION_KEY = '286747d63cbd405a802a492dd20cec34'

# Put in address of the Computer Vision service
vision_service_address = 'https://pythonimageanal.cognitiveservices.azure.com/'

# Add the name of the function you want to call the address
address = vision_service_address + 'analyze'

# Per documentation for the analyze image function
# There are three optional parameters
parameters = {'visualFeatures': 'Description,Color','language': 'en'}

# Open the image to get a file object containing the image to analyze
image_path = './Images/polarBear.jpeg'
image_data = open(image_path, 'rb').read()

# Per documentation, specify subscription key and content type
headers = {'Content-Type': 'application/octet-stream', 
           'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

# Per documentation, we use the HTTP POST to call the analyze image function
response = requests.post(address, headers=headers, params=parameters, data=image_path)

# Raise an exception if teh call returns an error
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))