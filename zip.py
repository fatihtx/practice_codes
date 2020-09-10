a = [ 0,   2,    1]
b = ["a", "b", "c"]

x = zip(b, a)

list_us = list(x)

print(list_us)

#list_usz = list(zip(*list_us))

#print(list_usz)

list_us.sort(key = lambda x: x[1])
#sort(key = lambda x: x[1])

print(list_us)

list_uz = list(zip(*list_us))

print(list_uz)
