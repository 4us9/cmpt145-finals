### Creating Dictionary Techniques
a = dict()

#Technique No. 1
b = dict(one = 1, two = 2, three = 3)
print(b) #Output: {'one': 1, 'two': 2, 'three': 3}

# Technique No.2
c = dict([('one', 1),('two', 2),('three', 3)])
print(c) # two ways of using the built-in dictionary object.
# this method is more work. But it helps you understand
#the data type you're using for the keys. Notice brackets outer, square as the second layer.

#Technique No.3
dict = {} # empty dictionary LITERAL
dict = {'one': 1, 'two': 2, 'three': 3, 'king': 1000}
print(dict)

# It is like you're manually doing what it is supposed to print out.
# notice the colons and separated commas.

print(len(dict)) # counts the total number of unique keys are
# present in the dictionary. I was confued because it gave three, and I thought it spits the key's last value.

dict['two'] = 300
dict['two'] += 300
print(dict)

# problem

ex = "This. is. a. period"
line = ex.strip().split(".") #Output: {['This', ' is', ' a', ' period']
print(line)

ex2 = "This, is, a, comma."
line2 = ex2.strip().split(",")
print(line2)

# see makes them into separate elements in a list by splitting when
# it sees commas only. The removal of the white spaces is so there is no
# unecessary stuff. Purely just the data/string that is not whitespaces