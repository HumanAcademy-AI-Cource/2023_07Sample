#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import cv2

def detect_labels_local_file(photo):


    client=boto3.client('rekognition')
    
    image = cv2.imread(photo) # OpenCVで画像を読み込み
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # OpenCVで画像をグレースケール化
    ret, image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY) # 2値化
    byte_image = cv2.imencode(".PNG", image)[1].tobytes() # OpenCVで画像をPNG形式の画像データ（バイトデータ）に変換
    response = client.detect_labels(Image={'Bytes': byte_image}) # バイトデータをAWSに送って分析

    cv2.imwrite("kakou.png", image) # 確認用に保存
        
    print('Detected labels in ' + photo)    
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))

    return len(response['Labels'])

def main():
    photo='image.png' # 変更した場所

    label_count=detect_labels_local_file(photo)
    print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    main()
