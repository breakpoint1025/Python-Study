import os

def rename_files():
	files = os.listdir(r"E:\VPC")
	print(files)
	for file in files:
		print(file)

def walk_files():
	for root, dirs, files in os.walk(r"E:\VPC"):
		for file in files:
			print(os.path.join(root,file))

def for_loop_test():
	for i, element in zip([1,2,3], [4,5,6]):
		print(i)
		print(element)
		
		
rename_files()		
walk_files()
for_loop_test()