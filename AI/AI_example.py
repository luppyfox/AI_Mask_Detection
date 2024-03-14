import cv2 

Conf_threshold = 0.8
NMS_threshold = 0.5
COLORS = [(0, 255, 0)]

cap = cv2.VideoCapture(0)

# Tomato V2.1
# class_name = []
# with open('D:/Python WorkShop/Tomato AI V.2.1/obj.names', 'r') as f:
#     class_name = [cname.strip() for cname in f.readlines()]
# net = cv2.dnn.readNet('D:/Python WorkShop/Tomato AI V.2.1/WEIGHTS 64000.weights', 'D:/Python WorkShop/Tomato AI V.2.1/CFG 64000.cfg')

# Tomato V2.2
# class_name = []
# with open('D:/Python WorkShop/Tomato AI V.2.2/obj.names', 'r') as f:
#     class_name = [cname.strip() for cname in f.readlines()]
# net = cv2.dnn.readNet('D:/Python WorkShop/Tomato AI V.2.2/WEIGHTS 11000.weights', 'D:/Python WorkShop/Tomato AI V.2.2/CFG 11000.cfg')

# Classmate V1
class_name = []
with open('D:/Python WorkShop/Classmate AI V1/obj.names', 'r') as f:
    class_name = [cname.strip() for cname in f.readlines()]
net = cv2.dnn.readNet('D:/Python WorkShop/Classmate AI V1/WEIGHTS.weights', 'D:/Python WorkShop/Classmate AI V1/CFG.cfg')

# # YoloV4 tiny
# class_name = []
# with open('D:/Python WorkShop/Yolov4-tiny/coco.names', 'r') as f:
#     class_name = [cname.strip() for cname in f.readlines()]
# net = cv2.dnn.readNet('D:/Python WorkShop/Yolov4-tiny/yolov4-tiny.weights', 'D:/Python WorkShop/Yolov4-tiny/CFG.cfg')

net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255, swapRB=True)

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    cutframe = cv2.resize(frame, (320,320))
    classes, scores, boxes = model.detect(cutframe, Conf_threshold, NMS_threshold)
    for (classid, score, box) in zip(classes, scores, boxes):
        Def = 0
        color = COLORS[int(classid) % len(COLORS)]
        label = "%s : %f" % (class_name[classid], score)
        cv2.rectangle(cutframe, box, color, 2)
        cv2.putText(cutframe, label, (box[0], box[1]-10),cv2.FONT_HERSHEY_COMPLEX, 0.3, color, 1)
    cv2.imshow('frame', cutframe)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()