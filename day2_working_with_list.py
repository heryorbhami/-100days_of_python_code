#Working with List
#List is the collection of item in a particular order
#it allow you to store set of information in one place
#Example of List

classmates =['emma','alex','johnvict','clinton','tope']
#accessing the list
print(classmates)

#using index to access element in the list
print("\nAccessing element in index [2]")
print("\n",classmates[2].title())

#Modifying the list
print("\nchanging element at index [0]")
classmates[0] = 'samson'
print(classmates)

print("\nAppending element to the end of the list")
classmates.append('grace')
print(classmates)
