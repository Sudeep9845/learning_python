def change(L):
    print(id(L))
    L.append(5)
    print(id(L))

L1 = [1, 2, 3]
print(L1)
change(L1)
print(L1)

# without cloning 
# [1, 2, 3]
# 135018669219008
# 135018669219008
# [1, 2, 3, 5]
# L1 goes through the same id before and after the change function call, so the original list is modified.
# For tuples, since they are immutable, any attempt to modify them would result in an error.
L2 = [4,6,7]
print(id(L2))  
print(L2)
change(L2[:])
print(L2)

# with cloning