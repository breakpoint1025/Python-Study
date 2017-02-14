import os

def rename_files():
	files = os.listdir(r"C:\GitHub\FreeCodeCamp-Study")
	print(files)
	for file in files:
		print(file)



def walk_files():
	for root, dirs, files in os.walk(r"C:\GitHub\FreeCodeCamp-Study"):
		for file in files:
			print(os.path.join(root,file))
		
		
rename_files()		
walk_files()