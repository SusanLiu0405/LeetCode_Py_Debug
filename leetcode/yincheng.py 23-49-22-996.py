'''
num1 = "23"
num2 = "33"
sum = "56"
return the sum as a str = num1 + num2
'''
num1 = "345"
num2 = "789"
sum = "1134"

m = len(num1) - 1
n = len(num2) - 1
sum = []
flag = 0
while m >= 0 and n >= 0:
    curr_sum = int(num1[m]) + int(num2[n])
    curr_sum += flag
    if curr_sum >= 10:
        flag = 1
    else:
        flag = 0
    sum.append(curr_sum % 10)
    m -= 1
    n -= 1
while m >= 0:
    sum.append(int(num1[m]))
    m -= 1
while n >= 0:
    sum.append(int(num2[n]))
    n -= 1

print(sum[::-1])




    


