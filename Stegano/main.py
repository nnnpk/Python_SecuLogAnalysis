import cv2
import numpy as np
from imageEmbedding import *
from imageProcessing import *
from passwordFunctions import *
from filenameParser import *
from optparse import OptionParser


####################################################################
############################ Sample Images #########################
####################################################################

#secimage_path = "./SampleImages/image.BMP"
secimage_path = "D:/SecurityApp/Stegano/SampleImages/image.jpg"

#medimage_path = "./SampleImages/image3.jpg"
medimage_path = "D:/SecurityApp/Stegano/SampleImages/image3.jpg"

#passphrase to use
passphrase = 'hello world'

#passphrase to detach the sec image
de_passphrase = "hello world"
#de_passphrase_bin = format(int(de_passphrase,16),'0>128b')

###################################################################
########################### Paser Options #########################

parser = OptionParser()

parser.add_option("-e","--embed",dest="embedimage_path",help="embed image name")
parser.add_option("-s","--secimg",dest="secimage_path",help="secret image name")
parser.add_option("-m","--medimg",dest="medimage_path",help="media image name")
parser.add_option("-p","--pass",dest="passwordphrase",help="file name")
(options,argrs) = parser.parse_args()


###################################################################


def hideimage(medimage,secimage,passphrase):
	passphash = getpasshash(bytes(passphrase,encoding='utf-8'))
	pass_array = converthash(passphash)
	filename_bin_array = convertfilenamebin(getfilenamebin(secimage))
	medimage = loadmedimg(medimage)
	secimage = loadsecimg(secimage)
	embedded_array = (embedsecimg(medimage,secimage))
	password_embeddedd_array =  embedpassword(embedded_array,pass_array)
	final_embeddedd_array = embedfilename(password_embeddedd_array,filename_bin_array)
	showimage(final_embeddedd_array)
	saveimage(final_embeddedd_array,"embeddedimage.png")


def unhideimage(embeddedimage,de_passphrase):
	embedded_array = cv2.imread(embeddedimage)
	passhash1 = detachpassphrase(embedded_array)
	passhash2 = getpasshash(bytes(de_passphrase,encoding='utf-8'))
#	print (passhash1)
#	print (passhash2)
	if passhash1 == passhash2:
		decrypted_array = (decryptsecimg(embedded_array))
		showimage(decrypted_array)
		filename = detachfilename(embedded_array)
		saveimage(decrypted_array,filename)
	else:
		pass





if __name__ == '__main__':
#	hideimage(medimage_path,secimage_path,passphrase)
#	unhideimage("./output/embeddedimage.png",de_passphrase)
	
	if options.embedimage_path and options.passwordphrase:
		try:
			unhideimage(options.embedimage_path,options.passwordphrase)
		except:
			pass

	if options.medimage_path and options.secimage_path and options.passwordphrase:
		try:
			hideimage(options.medimage_path,options.secimage_path,options.passwordphrase)
		except:
			print ("Please use the -h or --help for help, or use python gui.py for Graphical User Interface")
	else:
		print ("Please use the -h or --help for help, or use python gui.py for Graphical User Interface")




