for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("sorry no i")

#else contant will no print if we using break between any range 

for x in range(5):
    print("iteration no {} in for loop". format(x+1))
else:
    print("else  block in loop")
print("out of loop")
