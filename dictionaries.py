d = {}
d_1 = dict()

# Dictonaires are key:value pair based
# Also known as hashmaps
# Dictionaries are mutable datatype

sample = {'a' : 1, 'b' : 2}
print(sample['a'], sample.get('b'))

sample['a'] = 10
print(sample)

# Keys in dictonaries, once defined can't be changed
# Hence they should be of immutable datatype, for e.g. tuple, string

sample = {("a", "b"): 1, 'b': 2}
print(sample)