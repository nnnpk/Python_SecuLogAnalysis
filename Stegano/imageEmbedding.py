import cv2
import numpy as np
from passwordFunctions import *
from filenameParser import *



#####################################################################
##################### Loading Sample Images #########################
#####################################################################

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


#####################################################################
################### Image Embedding Modules #########################
#####################################################################

def encryptsecimg(secimg):
	#Divide the bgr by 4 and siplate to 3 binary strings
	list_result=[]

	for n in range(len(secimg)):
	    l = secimg[n]
	    for num in range(len(l)):
	        px = l[num]
	        for num in range(len(px)):
	            color = int(px[num]/4)
	            color = '{:06b}'.format(color)
	            color = ([color[i:i+2] for i in range(0, len(color), 2)])
	            for b2 in color:
	#                result_array = np.append(result_array,b2)
	                list_result.append(b2)

	list_result.reverse()
	result_array = np.asarray(list_result,dtype=np.int)
	
	return result_array




def embedsecimg(medimg,secimg):
	encrypted_array = (encryptsecimg(secimg))
	total_axis = medimg.shape[0] * medimg.shape[1] * medimg.shape[2]
	medimg = medimg.reshape(total_axis,)
	for n in range(len(encrypted_array)):
		color_bin = format(medimg[n],'08b')[:-2] + str(format(encrypted_array[n],'02'))
		# converting binary back to integer
		medimg[n] = int(color_bin,2)

	medimg = medimg.reshape(760,1024,3)

	medimg = medimg.astype(np.uint8)


	return medimg

def embedpassword(embeddedimg,passphrasearray):
	total_axis = embeddedimg.shape[0] * embeddedimg.shape[1] * embeddedimg.shape[2]
	embeddedimg = embeddedimg.reshape(total_axis,)
#	print(len(embeddedimg))
	for i in range(len(passphrasearray)):
		n = len(embeddedimg) -i - 1
#		print(n)

#		print(format(embeddedimg[n],'08b')[:-2])
#		print(str(format(passphrasearray[i],'02')))

		color_bin = str(format(embeddedimg[n],'08b')[:-2]) + str(passphrasearray[i])
		# converting binary back to integer
#		print(color_bin)
		embeddedimg[n] = int(color_bin,2)

	embeddedimg = embeddedimg.reshape(760,1024,3)
	embeddedimg = embeddedimg.astype(np.uint8)

	return embeddedimg


def embedfilename(embeddedimg,filename_bin_array):
	total_axis = embeddedimg.shape[0] * embeddedimg.shape[1] * embeddedimg.shape[2]
	embeddedimg = embeddedimg.reshape(total_axis,)
#	print(len(embeddedimg))

	length_bin = filename_bin_array_length_bin(filename_bin_array)
	# Embeding the length of filename and extesion binary
	for i in range(len(length_bin)):
		n = -64 - i - 1
		color_bin = str(format(embeddedimg[n],'08b')[:-2]) + str(length_bin[i])
		embeddedimg[n] = color_bin


	# Embeding the binary of file name and extension
	for i in range(len(filename_bin_array)):
		n = -68 -i - 1
		color_bin = str(format(embeddedimg[n],'08b')[:-2]) + str(filename_bin_array[i])

		embeddedimg[n] = int(color_bin,2)

	embeddedimg = embeddedimg.reshape(760,1024,3)
	embeddedimg = embeddedimg.astype(np.uint8)

	return embeddedimg


def detachpassphrase(embeddedimage):
	total_axis = embeddedimage.shape[0] * embeddedimage.shape[1] * embeddedimage.shape[2]
	embeddedimage = embeddedimage.reshape(total_axis,)
#	print(len(embeddedimage))
	passphrasearray  = []
	for i in range(64):
		n = len(embeddedimage) - i - 1
#		print (n)
#		print (embeddedimage[n])
		pass_bin = format(embeddedimage[n],'08b')[-2:]
#		print(pass_bin)
		passphrasearray.append(pass_bin)

	passphrase = ""

	passphrase = passphrase.join(str(i) for i in passphrasearray)

	passphrase = hex(int(passphrase,2))[2:]


	return passphrase


def detachfilename(embeddedimage):
	total_axis = embeddedimage.shape[0] * embeddedimage.shape[1] * embeddedimage.shape[2]
	embeddedimage = embeddedimage.reshape(total_axis,)
#	print(len(embeddedimage))


	filename_bin_array_length_bin = []
	for i in range(4):
		n = len(embeddedimage) - i - 65
		file_length_bin = format(embeddedimage[n],'08b')[-2:]

		filename_bin_array_length_bin.append(file_length_bin)

	filenamelength = ""

	filenamelength = filenamelength.join(str(i) for i in filename_bin_array_length_bin)

	filenamelength = int(filenamelength,2)


	filename_bin_array = []
	for i in range(filenamelength):
		n = len(embeddedimage) - i -69
		file_name_bin = format(embeddedimage[n],'08b')[-2:]

		filename_bin_array.append(file_name_bin)

	filename_bin = ""
	filename = ""
	filename_bin = filename_bin.join(str(i) for i in filename_bin_array)
	filenamechar = ([filename_bin[i:i+8] for i in range(0, len(filename_bin), 8)])
	for i in filenamechar:
		i = int(i,2)
		i = chr(i)
		filename += i

	return filename



def detachsecimg(embeddedimg):
	total_axis = embeddedimg.shape[0] * embeddedimg.shape[1] * embeddedimg.shape[2]
	embeddedimg = embeddedimg.reshape(total_axis,)
#	print(len(embeddedimg))
	detached_list = []
	for n in range(1751040):
		brg_bin = format(embeddedimg[n],'08b')[-2:]
		detached_list.append(brg_bin)

	detached_list.reverse()
	detached_array = np.asarray(detached_list,dtype=np.int)

	return detached_array


def decryptsecimg(embeddedimg):
	# Shape the array, so every brg color takes one row
	#nol = encrypted_array[0]/3

	encrypted_array = detachsecimg(embeddedimg)

	nol = (len(encrypted_array))/3
	encrypted_array = encrypted_array.reshape(int(nol),3)

	restore_list = []
	for n in range(len(encrypted_array)):
		restore_color = (str(format((encrypted_array[n][0]),'02')))+(str(format((encrypted_array[n][1]),'02')))+(str(format((encrypted_array[n][2]),'02')))
		restore_color = int(restore_color,2)*4
		restore_list.append(restore_color)

	restore_array = np.asarray(restore_list,dtype=np.int)
	restore_array.shape
	restore_array=restore_array.reshape(380,512,3)

	restore_array = restore_array.astype(np.uint8)
	
	return  restore_array



########################################################################
#################### Test the modules ##################################
########################################################################



if __name__ == "__main__":
	encrypted_array = (encryptsecimg(secimg))
	print("Encrpted Image shape: ")
	print(encrypted_array.shape)


#	decrpted_array = (decrptsecimg(encrypted_array))
#	print("Encrpted Image Data: ")
#	print(decrpted_array)

	embedded_array = (embedsecimg(medimg,secimg))
	print("Embedded Image Data: ")
	print (embedded_array)


	passphrase = getpasshash(b"hello world")
	pass_array = converthash(passphrase)
#	print (pass_array)
	final_embedded_array = embedpassword(embedded_array,pass_array)


#	print("Final Image Data: ")
#	print(final_embedded_array)
	cv2.imshow("image",final_embedded_array)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	cv2.imwrite('./output/embeddedimage.jpg',final_embedded_array)

	decrypted_array = (decryptsecimg(final_embedded_array))

	print(detachpassphrase(final_embedded_array))

	cv2.imshow("image",decrypted_array)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	cv2.imwrite('./output/secretimage.jpg',decrypted_array)