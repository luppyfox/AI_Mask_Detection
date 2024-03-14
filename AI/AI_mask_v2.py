import cv2

Conf_threshold = 0.8
NMS_threshold = 0.3
COLORS = [(0, 255, 0),(255, 0, 0)]

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

class_name = []
with open('C:/Users/Luppyfox/Desktop/mask_detection/v1/obj.names', 'r') as f:
    class_name = [cname.strip() for cname in f.readlines()]
net = cv2.dnn.readNet('C:/Users/Luppyfox/Desktop/mask_detection/v1/custom-yolov4-detector_best.weights', 'C:/Users/Luppyfox/Desktop/mask_detection/v1/custom-yolov4-detector.cfg')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
#net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
#net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
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
        Name = class_name[int(classid)]
        label = str(Name) + " : " + str(score)
        cv2.rectangle(cutframe, box, color, 2)
        cv2.putText(cutframe, label, (box[0], box[1]-10),cv2.FONT_HERSHEY_COMPLEX, 0.3, color, 1)
    cv2.imshow('frame', cutframe)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()