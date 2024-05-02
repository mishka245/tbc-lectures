a=[3,4,5,8]
b=[3,2,0,0]
c=[]

for i in range(len(a)):
    try:
        elem = a[i] / b[i]
        c.append(elem)
    except ZeroDivisionError:
        print("Zero division", i)
        c.append("Err")
        break

print("Final result is", c)