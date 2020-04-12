import cv2
import numpy as np

from imageEmbedding import *


#######################################################################################
####################### Loading Sample Images #########################################
#######################################################################################

# import secret image
secimg = cv2.imread("./SampleImages/image.BMP")
sec_width = 512
sec_height = 380
sec_dim = (sec_width,sec_height)
secimg = cv2.resize(secimg, sec_dim, interpolation = cv2.INTER_AREA)

# import median image
medimg = cv2.imread("./SampleImages/image3.jpg")
med_width = 1024
med_height = 760
med_dim = (med_width,med_height)
medimg = cv2.resize(medimg, med_dim, interpolation = cv2.INTER_AREA)


######################################################################################
#################### Image Processing Modules ########################################
######################################################################################


def loadmedimg(medimage):
	medimg = cv2.imread(medimage)
	med_width = 1024
	med_height = 760
	med_dim = (med_width,med_height)
	medimg = cv2.resize(medimg, med_dim, interpolation = cv2.INTER_AREA)

	return medimg

def loadsecimg(secimage):
	secimg = cv2.imread(secimage)
	sec_width = 512
	sec_height = 380
	sec_dim = (sec_width,sec_height)
	secimg = cv2.resize(secimg, sec_dim, interpolation = cv2.INTER_AREA)

	return secimg


def resizeimg(encrypted_array):
	scale_percent = 200 # percent of original size
	width = int(encrypted_array.shape[1] * scale_percent / 100)
	height = int(encrypted_array.shape[0] * scale_percent / 100)
	dim = (width, height)
	resizedsecimg = cv2.resize(secimg, dim, interpolation = cv2.INTER_AREA)

	return resizedsecimg


def showimage(img_array):
	cv2.imshow("image",img_array)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


def saveimage(img_array,imagename):
	cv2.imwrite('./output/'+imagename,img_array)






##################################################################################
########################## Testing ###############################################
##################################################################################


if __name__ == "__main__":
	# Show and save the embeddedimage
	embedded_array = (embedsecimg(medimg,secimg))
	showimage(embedded_array)
	saveimage(embedded_array,"embeddedimage.png")


#	print(encrypted_array.shape)
	
#	embedded_array = cv2.imread("./output/embeddedimage.png")
#	showimage(embedded_array)
	
	decrypted_array = (decryptsecimg(embedded_array))
#	print(decrpted_array)
#	decrpted_array = (resizeimg(decrpted_array))
	showimage(decrypted_array)
	saveimage(decrypted_array,"secretimage.png")


