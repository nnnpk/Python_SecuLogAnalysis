import hashlib


passphrase = b"hello world"

def getpasshash(passphrase):
	hash_passphrase = hashlib.md5(passphrase)
	hash_passphrase = hash_passphrase.hexdigest()

	return hash_passphrase

def converthash(hash_passphrase):
	pass_bin = format(int(hash_passphrase,16),'0>128b')

	pass_bin_array = []

	for i in range(0, len(pass_bin), 2):
	 	pass_bin_array.append(pass_bin[i:i+2])


	return pass_bin_array







if __name__ == "__main__":
	hash_passphrase=(getpasshash(passphrase))
	print(hash_passphrase)
	print(converthash(hash_passphrase)) 