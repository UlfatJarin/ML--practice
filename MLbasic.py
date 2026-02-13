##Basic Math
#  -Mean , Median , Mode

values= [ 50,70,70, 90, 45, 76, 99, 88]
values.sort()

mean = sum(values)/ len(values)
print("mean value:", mean)
 
if len(values)%2==0 :
    mid = len(values)//2
    median= (values[mid-1]+ values[mid])/2
    print("median", median)

else:
    median = values[len(values)//2]
    print("median", median)

mode = max(values, key = values.count)
print("mode", mode)



#dataset = 

