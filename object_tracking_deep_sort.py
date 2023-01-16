import cv2
import numpy as np

from object_detection import ObjectDetection
from deep_sort.deep_sort import Deep
import time 

#Load Object Detection

od = ObjectDetection("dnn_model/yolov4-csp-swish.weights", 'dnn_model/yolov4-csp-swish.cfg")
od.load_class_names("dnn_model/classes.txt")
od.load_detection_model(image_size = 640, #416 - 1280
                       nmsThreshold = 0.4
                       confThreshold = 0.3) 



#Load Object Tracking Deep Sort

deep = Deep(max_distance = 0.7, nms_max_overlap=1, n_init=3, max_age=15, max_iou_distance = 0.7)

tracker = deep.sort_tracker()

cap = cv2.VideoCapture("link")
ret, img = cap.read()
rows, cols, _= img.shape

count = 0
while True : 
ret, img = cap.read()
if not ret : 
break

count +=1
if count % 3! = 0: 
continue 




area_1 = [(,) , (,), (,), (,) ]
area_2 = [(,) , (,), (,), (,) ]

#tracking vehicles roundabout
vehicle_entering = {}
vehicle_elapsed_time = {}

result = cv2.pointPolygonTest (np.array (area_1, np.int32), (int(cx), int(cy)), Fasle)

if result >=0 : 
vehicles_entering [object_id] = time.time()
print(vehicle_entering)

if object_id in vehicles_entering :
result = cv2.pointPolygonTest(np.array (area_2, np.int32), (int(cx), int(cy)), Fasle)

if result >= 0 : 
elapsed_time = time.time() - vehicles_entering [object_id] 

vehicle_elapsed_time[object_id] = elapsed_time


#calc avg speed

distance = 65 #meters
a_speed_ms = distance / elapsed_time
a_speed_kh = a_speed_ms * 3.6
 
 

