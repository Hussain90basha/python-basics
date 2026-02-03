t = ()
t1 = tuple()

sample = ("172.10.12.1", "172.10.12.2", True, 123, 123.45, 123.456)
print(type(sample), sample) 

# tuple is immutable

print(sample[0])
# sample[0] = (12)
# print(sample)
print(sample[0:2])
print(sample[-1])

env_list = ("DEV", "QA", "PRE-PROD", "PROD")

print(dir(tuple))
"""
['count', 'index']
"""

sample = (1, 2, 3, 4, 4, 5, 6, 6)
print(sample.count(6), sample.count(15))
print(sample.index(5))