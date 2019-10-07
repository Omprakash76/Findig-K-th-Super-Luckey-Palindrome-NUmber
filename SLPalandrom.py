import numpy as np
k = int(input("enter Kth digit : "))
list0 = list()
list1 = list()

p = ["4","7"]

def check(n):
    for value in list1:
        if value not in p:
            return 5
        
def count(v):
    i = 0 
    for x in list1:
        if x == v:
            i = i+1
    return i




def new_funk():        
    
    fourth = count('4')
    # print(fourth)
    seven = count('7')
    # print(seven)
    c = check(4)
    # print(c)
    if c != 5:
        if (len(list1) == 4 or len(list1) == 7):
            if (fourth == 4 or fourth == 7 or seven == 7 or seven == 4):
                if list1 == list1[::-1]:
                    list0.append(x)
                    list1.clear()
                    # print("This no. is super luckey palindrome no.")
    else:
        list1.clear()


# while True:
for x in np.arange(4444, 4747475):
    x = str(x)
    # print(x)
    
    for element in x:
        list1.append(element)
    # print(list1)
    new_funk()
    # print(list0[-1])
    if len(list0) == k:
        break
print(list0[-1])
