#Program for Sets data type - indexing and slicing don't work.
s = {10,20,30,40,50}
print("Set is  " , s)
ch = set("Hello") # Displays random char
print("CH is : " , ch)
lst=[1,2,3,4,5]
s=set(lst)
print("Set in lst : " , s)
s.update([6])
print("set : after update : " , s)
s.remove(1)
print("set : after remove : " , s)
#Frozenset - can't update or remove
s={50,60,70,80,90}
print(s)
fs = frozenset("Hello")
print("Frozen set : " , fs )
#Mapping data type - key:value seperated by , - dict datatype
d = {1:"One", 2: " Two", 3: "Three", 4: "Four"}
print("dictionary - " , d)
print("d[1] : " , d[1])
print("All keys : ", d.keys())
print("All Values : " , d.values())
# Redefine a value
d[2] = "Two_Dummy"
print("d[2] : " , d[2])
del d[1]
print("d: " , d)