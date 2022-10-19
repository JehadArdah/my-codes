## lists , dictionaries , sets , tuples
all_names=['jehad','ahmad','khalid','ebrahim']
exist_names=['jehad','khalid','ebrahim']

s_all_names=set(all_names)
s_exist_names=set(exist_names)

print('exist students :',s_all_names.intersection(s_exist_names))
print('missing students :',s_all_names.union(s_exist_names)-s_all_names.intersection(s_exist_names))