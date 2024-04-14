MEDIAN = 30
DIV_NUM = 3


lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]


for item in lst:

    if (item < MEDIAN) and (item % DIV_NUM == 0):
        
        
        print(item)
