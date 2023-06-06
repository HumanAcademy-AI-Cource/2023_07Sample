import cv2

photo = "image.png"

# 標準機能で画像読み込み
with open(photo, "rb") as image:
    print(image.read()[:30])

print("-----------------------------")

cv_image = cv2.imread(photo) # OpenCVで画像を読み込み
print(cv_image[:2])