import cv2
import numpy as np

def trans():
  img=cv2.imread(r'c:\\opencv\your\xia_screw.png')

  height = img.shape[0];
  width = img.shape[1];
  min_val = 255;
  for i in range(0,height):
    for j in range(0,width):
      val = (int(img[i][j][0])+img[i][j][1]+img[i][j][2])/3
      if min_val > val:
        min_val = val
  img_a =  np.full((height,width,1),255,dtype=np.uint8);
  for i in range(0,height):
    for j in range(0,width):
      if (img[i][j] == (255,255,255)).all():
        img_a[i][j] =  0;
      else:
          val = (int(img[i][j][0])+img[i][j][1]+img[i][j][2])/3;
          op_val = int(255-val)*255/(255-min_val)
          if (op_val > 255):
            op_val = 255
          img_a[i][j] = op_val
  b,g,r = cv2.split(img)
  img_t = cv2.merge((b,g,r,img_a))
  rlt = cv2.imwrite(r'c:\\opencv\your\tmp.png',img_t)
  print(min_val)

img=cv2.imread(r'c:\\opencv\your\Untitled.png')

height = img.shape[0];
width = img.shape[1];
img_t =  np.full((810,1440,3),255,dtype=np.uint8);

for i in range(0,810):
  for j in range(0,1440):
    img_t[i][j] = img[i+3][j+4]
  
cv2.imwrite(r'c:\\opencv\your\whole.png',img_t)