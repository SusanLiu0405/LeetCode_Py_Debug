from typing import List

def swapMinAndMax(array: List[int]) -> List[int]:
    min = 0
    max = 0
    for i in range(len(array)):
        if array[i] < array[min]:
            min = i
        if array[i] > array[max]:
            max = i
    array[min], array[max] = array[max], array[min]
    return array

# Alternative Solution:
# def swapMaxAndMin(nums):
#     if not nums or len(nums) < 2:
#         return nums

#     min_index = nums.index(min(nums))
#     max_index = nums.index(max(nums))

#     # 交换最大和最小数字
#     nums[min_index], nums[max_index] = nums[max_index], nums[min_index]

#     return nums

input_array = input("请输入数组，用空格分隔：")
# 将输入的字符串转换为整数列表
array = list(map(int, input_array.split()))
print(swapMinAndMax(array))


# In[3]:


# 从键盘输入数组的维度
rows, cols = map(int, input("请输入行数和列数，用空格分隔：").split())

# 创建一个空的二维数组
array = [[0 for _ in range(cols)] for _ in range(rows)]

print("请输入二维数组的元素，每行以空格分隔：")

# 从键盘输入二维数组的元素
for i in range(rows):
    array[i] = list(map(int, input().split()))

my_variable = array
print(my_variable)


# In[ ]:




