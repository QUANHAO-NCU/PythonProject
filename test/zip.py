a = [1,2,3,4,5]
b = [2,4,6,8,10]
zip1 = zip(a,b)
unpack = zip(*zip(a,b))#这里只执行了解压的操作，而不是字面上的解压又压缩
#解压：zip(*zip(var,var,...))