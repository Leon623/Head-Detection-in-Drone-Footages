import torch
import cv2
from PIL import Image

model_path = 'latest_final.pt'
device = torch.device('cpu')

model = torch.hub.load('../yolov5_master', 'custom', path=model_path, source='local')

image_path = 'HT21/test/HT21-12/img1/000105.jpg'
img = Image.open(image_path).convert('RGB')

results = model([img], 1024)
results.render()

cv2.imshow("asd", cv2.pyrDown(cv2.cvtColor(results.ims[0], cv2.COLOR_BGR2RGB)))
cv2.waitKey(0)
