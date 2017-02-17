arr_before_sort = [3,7,8,5,2,1,9,5,4]

def quick_sort(arr):
	
	'''选定一个基准元素, 将基准元素与数组中最后一个元素交换位置'''
	arrlen = len(arr)
	if arrlen == 1 or arrlen == 0 : return arr
	
	pivotIndex = int(arrlen/2)
	pivotVar = arr[pivotIndex]
	arr[pivotIndex],arr[-1] =  arr[-1], arr[pivotIndex]
	
	'''从左到右（除了最后的基准元素），循环移动小于基准元素的所有元素到数组开头，留下大于等于基准元素的元素接在后面。在这个过程它也为基准元素找寻最后摆放的位置'''
	sortIndex = 0	
	for var in arr[sortIndex:-1]:
		if(var <= pivotVar):
			index = arr.index(var)
			arr[sortIndex],arr[index] = arr[index], arr[sortIndex]
			sortIndex = sortIndex + 1
		else:
			continue

	arr[sortIndex],	arr[-1] = arr[-1], arr[sortIndex]
	
	
	'''递归排序左右两个子集, arr[0:sortIndex]会新建数组，操作不会在原数组上生效'''
	left = quick_sort(arr[0:sortIndex])
	right = quick_sort(arr[sortIndex+1:])
	left.append(arr[sortIndex])

	return left + right

	
print("before Sort:",arr_before_sort)
arr_after_sort = quick_sort(arr_before_sort)
print("After Sort:",arr_after_sort)		
