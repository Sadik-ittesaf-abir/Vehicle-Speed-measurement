import cv2
count_line_position = 550


#Draw line on road

cv2.line(frame1,(25,count_line_position),(1200,count_line_position),(255,127,0),3)

#center point detection

def center_handle(x,y,w,h):
x1=int(w/2)
y1=int(h/2)
cx=x+x1
cy=y+y1

return cx,cy

detect = []


#at end

center = center_handle(x,y,w,h)
detect.append(center)
cv2.circle(frame1,center,4,(0,0,255),-1)


#count

for(x,y) in detect :

if y<(count_line_position + offset) and y>(count_line_position - offset) :

counter +=1

cv2.line(frame1,(25,count_line_position),(1200,count_line_position),(255,127,0),3)

detect.remove(x,y)
print("Vehicle Counter:"+str(counter))

cv2.putText(frame1, "VEHICLE COUNTER:"+str(counter),(450,70),cv2.FONT_HERSHEY_SIMPLEX,(0,0,255),5)


cv2.imshow('Vdo Original',frame1)

if cv2.waitkey(1) == 13
break


