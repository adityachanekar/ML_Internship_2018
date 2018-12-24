my_tupple=(1,'Hello',4.05)

print(my_tupple)

my_tupple= 1,'hello',4.0,[1,2,3],('test',)
#accessing nested elements
my_tupple[3][1]=10
print(my_tupple[3])
#find element in tupple
print(1 in my_tupple)

#count total elements in a touple
total = my_tupple.count(1)
print(total)

