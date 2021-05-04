emp = {"Mary":23, "Gru":40, "Dan":34, "Caria":30}
print(emp)

print(emp["Mary"])  #we provide keys instead of index

#to add element in dictionary
emp["Ham"] = 23
print(emp)

#update
emp["Gru"] = 45
print(emp)

#delete.... deletes key and its associated value
del emp["Dan"]
print(emp)

# print(emp["Dan"])  #key error

#to get all keys...dict_keys is a structure that is iterable but not indexable
print(emp.keys())

# print(emp.keys()[0])   #error because not indexable

#to make it indexable conver into list
L = list(emp.keys())
print(L)
print(L[0])

#to get all values... same as keys()
print(emp.values())

# ** DICTIONARY IS UNORDERED


#convert dictionary to tuples
print(emp.items())




