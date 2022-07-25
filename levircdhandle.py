import os
import cv2
newName = "levirLight"
types = ["train", "val", "test"]
picTypes = ["A", "B", "label"]

if(not newName in os.listdir()):
    os.mkdir(newName)

for type in types:
    for picType in picTypes:
        try:
            os.makedirs(os.path.join(newName, type, picType))
        except:
            pass
    if(not "EDGE" in os.listdir(os.path.join(newName, type))):
        os.makedirs(os.path.join(newName, type, "EDGE"))


for type in types:
    for picType in picTypes:
        pics = os.listdir(os.path.join(type, picType))
        # print(len(pics))
        for pic in pics:
            cvpic = cv2.imread(os.path.join(type, picType, pic), -1)
            result = []
            for i in range(4):
                for j in range(4):
                    tmp = cvpic[i*256:i*256+256, j*256:j*256+256]
                    cv2.imwrite(os.path.join(newName, type, picType, pic.replace(".", "_"+str(i*4+j)+".")), tmp)
                    
for type in types:
    labelDir = os.path.join(newName, type, "label")
    files = os.listdir(labelDir)
    for file in files:
        tmp = cv2.imread(os.path.join(newName, type, "label", file))
        out = cv2.Canny(tmp, 80, 200)
        cv2.imwrite(os.path.join(newName, type, "EDGE", file), out)