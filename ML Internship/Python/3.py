#* and arg name
sum=0
def addition(*num):
    global sum
    for i in num:
        sum=sum+i
    print(sum)

addition(1,2,5)

