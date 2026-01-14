def search(nums, target) -> int:
	# 如果nums这个array的地址为空
	if nums == None:
		return -1

	# 左指针指向index = 0，右指针指向index = array长度 - 1
	left = 0
	right = len(nums) - 1

	# 左指针和右指针不相邻的时候，执行while里面的代码
	while left + 1 < right:
		mid = (left + right) // 2  # id指针指向的index，是左右指针的index相加再除以2，并把这个数字向下取整
		if target == nums[mid]:  # mid指向的index对应的数值正好是target
			return mid
		elif target < nums[mid]:  # mid指针指向的index对应的数值有点大
			right = mid  # 把范围限定在分界线的左边（让右指针往左
		else:
			left = mid  # 把范围限定在分界线的右边（让左指针往右

	# 现在：左右指针做邻居
	# 如果左指针指向target，那么返回左指针指向的index。右边同理。找不到的话就return -1
	if target == nums[right]:
		return right
	if target == nums[left]:
		return left
	return -1

if __name__ == "__main__":
	element = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	target = 3
	print(search(element, target))