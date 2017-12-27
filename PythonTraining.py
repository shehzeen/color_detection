import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


#CHANGE varPath variable
varPath ='ENTER PATH HERE' 
os.chdir(varPath)


accumulate = np.zeros(3);
acc_pixel_num=0;
#covnew = [(0,0,0),(0,0,0),(0,0,0)]
folder = "ENTER TRAINING FOLDER WITH TRAINING FILES HERE"
sumxxt = [(0,0,0),(0,0,0),(0,0,0)]

file = open("Output_Mean_Cov.text","a")

def display(img,title):
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


for filename in os.listdir(folder):
    if ".png" not in filename:
        continue
    RBG  = cv2.imread(os.path.join(folder,filename));
    showCrosshair = False
    fromCenter = False
    display(RBG,'Image')
    YBR = cv2.cvtColor(RBG, cv2.COLOR_BGR2YCR_CB);    
    r = cv2.selectROI('IMG', YBR, fromCenter,showCrosshair)


    imCrop = YBR[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])];
    accumulate[0] = np.sum(imCrop[:,:,0])+accumulate[0]; #Y
    accumulate[1] = np.sum(imCrop[:,:,1])+accumulate[1]; #CR
    accumulate[2] = np.sum(imCrop[:,:,2])+accumulate[2]; #CB
    height,width = imCrop.shape[:2];
    
    acc_pixel_num = (height*width)+acc_pixel_num;
    #print height
    #print width
#    cv2.imshow("Image", imCrop)
#    cv2.waitKey(0)
    
    
    for i in xrange(height):
        for j in xrange(width):
            somearray = (imCrop[i,j,:]).astype(float)
            xxt = np.multiply.outer(somearray,somearray)
            sumxxt = np.multiply.outer(somearray,somearray) + sumxxt
            


#print 'SUMXXT'
#print sumxxt
print acc_pixel_num
print 'Sum/N'
sumoverN =(sumxxt/acc_pixel_num).astype(float)
print sumoverN
print (sumxxt/acc_pixel_num).astype(float)
mu =  (accumulate/acc_pixel_num).astype(float)
print 'Mean'
print mu
muround = (np.rint(mu)).astype(int)
file.write(str(muround[0])+" "+str(muround[1])+" "+str(muround[2])+"\n")

mu2= np.multiply.outer(mu,mu)
print mu2
print 'COV'
cov = (sumoverN - mu2)
roundcov = (np.rint(cov)).astype(int)
print roundcov
file.write(str(roundcov[0][0])+" "+str(roundcov[0][1])+" "+str(roundcov[0][2])+"\n"+str(roundcov[1][0])+" "+str(roundcov[1][1])+" "+str(roundcov[1][2])+"\n"+str(roundcov[2][0])+" "+str(roundcov[2][1])+" "+str(roundcov[2][2])+"\n")


file.close()














