##############################################################
################### Sample Image File ########################
##############################################################

#secimage_path = "./SampleImages/image.BMP"
secimage_path = "D:/SecurityApp/Stegano/SampleImages/image.jpg"




##############################################################
################# Filename Parser Functions ##################
##############################################################


def getfilenamebin(filename):
	filename_list = filename.split("/")
	filename = filename_list[-1]
	filename = filename.rstrip("\n")
#	print (filename)
	filename_bin = ""
	for i in filename:
		bin =  (format(ord(i),'08b'))
#		print(bin)
		filename_bin += bin
	return filename_bin



def convertfilenamebin(filename_bin):

	filename_bin_array = []

	for i in range(0, len(filename_bin), 2):
		filename_bin_array.append(filename_bin[i:i+2])

	return filename_bin_array

def filename_bin_array_length_bin(filename_bin_array):
	length = len(filename_bin_array)
	length_bin = format(length,'08b')

	filename_bin_array_length_bin_array = []
	for i in range(0, len(length_bin), 2):
		filename_bin_array_length_bin_array.append(length_bin[i:i+2])

	return filename_bin_array_length_bin_array





#################################################################
#################### Test the functions #########################
#################################################################

if __name__ == "__main__":
	filename_bin=getfilenamebin(secimage_path)
	print(filename_bin)
	filename_bin_array=convertfilenamebin(filename_bin)
	print(filename_bin_array)
	print(filename_bin_array_length_bin(filename_bin_array))