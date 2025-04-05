array = [3,1,2,10,3]
for i in range((len(array) - 1)):
    res = array[i]+array[i+1]
    print(res)

cores = array.copy()
print("copy",cores)

# import random
# num =  int [3,4,2,8,45,9]
# show = num.random()
# print(show)


li = [4,9,6,0]
# out : 4,13,19,19
# algo 
# init - Empty list
# variable init =0 
# for loop i
# add number var to add in varbial 

lise = []
x = 0
for i in li:
    x += i
    lise.append(x)
print(lise)


li = [4, 8, 6, 0]  # Define li before using it
lise = []
x = 0

for i in li:
    x = x+i
    lise.append(x)

print(lise)
