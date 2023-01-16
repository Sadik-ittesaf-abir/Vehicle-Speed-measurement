import cv2

cap = cv2.VideoCapture("link")
ret, img = cap.read()
rows, cols, _ = img.shape

while True:
    ret, img = cap.read()

img = img[356: rows, 552: cols]

# show image
cv2.imshow("Img", img)
key = cv2.waitKey(33)
if key == 27:
    break

cv2.destroyAllWindows()  # vdo processing





