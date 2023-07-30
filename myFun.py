import cv2
import torch.nn as nn
import torch.norm as norm
import torch
def myLoss(y_hat, y, img, origin_img):
  loss1 = nn.CrossEntropyLoss()
  loss2 = norm(img - origin_img, p = inf, dim = None, keepdim = True, dtype = torch.float)
       
