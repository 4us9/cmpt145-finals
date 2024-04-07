x = 20
y = x # here only one number object is created. And the two frames share the same address memroy. y points to the SAME OBJECT as x. Remember: x is simply just a naming.
# variables are only for names and they are not data values or objects.
x = 20
y = 20 # has its own separate object now. So even if x changes, it will not be affected since they don't share the same
# address in the memory.

print(x)
print(y)