#1.add a new key-value pair to dictionary
my_dictionary={'name':'python','age':25}
my_dictionary["city"]="hyderabad"
print(my_dictionary)

#2.dictionary access
prod_info={'name':'laptop','brand':'hp','price':'45000'}
print(prod_info['price'])

#3.dictionary removal
my_dict={'name':'python','age':25,'city':'hyderabad'}
my_dict.pop('city')
print(my_dict)

#4.print the keys present in dictionary
my_dict={'name':'python','age':25,'city':'hyderabad'}
print(my_dict.keys())

#5.print the vvalues present in dictionary
my_dict={'name':'python','age':25,'city':'hyderabad'}
print(my_dict.values())

#exercise1.dictionary update
dict={'name':'python','age':25,'city':'hyderabad'}
dict1={'state':'telangana','country':'india'}
print(dict.update(dict1))
#by using square brackets aslo we can update the key-value pair in the dictionary
dict['state']='telangana'
print(dict)


#exercise2.dictionary acess
dict={'name':'python','age':25,'city':'hyderabad'}
print(dict['name'])
