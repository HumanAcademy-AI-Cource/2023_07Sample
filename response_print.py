import boto3

photo="image.png"
client=boto3.client("rekognition")
   
with open(photo, "rb") as image:
    response = client.detect_labels(Image={'Bytes': image.read()})

print(response)