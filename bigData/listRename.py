import os
def renameFiles():
	file_list = []
	#os.listdir list all files in a given directory
	fileDir = os.listdir("/Users/Luiz/desktop/python/prank")
	#for below just to exclude the .DS_Store file 
	#os.getcwd() returns the current working directory
	saved_path = os.getcwd()
	#change the current working directory
	os.chdir("/Users/Luiz/desktop/python/prank")
	for i in fileDir:
		if not i.startswith('.'):
			file_list.append(i)

	for file_name in file_list:
		#os.rename, function to rename files(source, destinarion)
		#string.translate , first argument is a table to translate a 
		#of characters in another set of characters (as we are not using
		#it we set the first argument as none)
		#the second argument is a list of characters that should be deleted
		os.rename(file_name, file_name.translate(None, '0123456789'))
	#changes directory back for the initial working directory
	os.chdir(saved_path)

renameFiles()