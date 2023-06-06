import boto3
import pprint

photo='image.png'
client=boto3.client('rekognition')
   
with open(photo, 'rb') as image:
    response = client.detect_labels(Image={'Bytes': image.read()})

pprint.pprint(response, sort_dicts=False)