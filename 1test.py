import cv2
def nothing(d):
    print d
    pass
img=cv2.imread('test.jpeg')
cv2.namedWindow('image')
cv2.createTrackbar('D','image',0,20,nothing)
    #while(1):
    #d=cv2.getTrackbarPos('D','image')
    #print 'loop'+str(d)
    #cv2.imshow('image',img)
    #k=cv2.waitKey(1)&0xFF
    #if k=='27':
#break
cv2.imshow('image',img)
k=cv2.waitKey()
print k
cv2.destroyAllWindows()
