
myset = set([1,1,1,1,1,2])
mylist = [1,1,2,3]
mytuple = (1,1,2,3, mylist)
mytuple[-1][-1] = 100
mylist.append(100)
mylist.append(5)
print(mylist[::-1])
mylist.remove(2)
print(mylist[:])
print(mytuple)

print(type(myset))


print("hello python")