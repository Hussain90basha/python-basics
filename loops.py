

# for, while
# continue, break

value = 0 

while value < 10:
    if value == 5:
        # increment is very important
        value = value + 1
        continue
    # print(value) 
    value = value + 1

sample = ["server1", "server2", "server3", "server4", 123]

idx = 0

while idx < len(sample):
    # print(sample[idx])
    idx += 1 # idx = idx + 1

# in -> membership operator (checks whether that element is present or not)
# print(1 in sample)
# print("server1" in sample)   

# idx = iterator
# sample = iterable

for ele in sample:
    print(ele) 
print(ele)    

# access elements inside a list with index using for loop
# range, enumerate
print(list(range(5)))    

for idx in range(len(sample)):
    ele = sample[idx]
    print(idx, ele)

print (enumerate(sample))
for val, idx in enumerate(sample):
    print(val, idx)    


# tuple unpacking
# a, b = (1, 2)
# print(a, b)    