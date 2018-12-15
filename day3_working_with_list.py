#Inserting element to the lis
print("THIS CODE ADD ELEMENT TO THE EXISTING LIST(CLASSMATE)")
classmates =['emma','alex','johnvict','clinton','tope']
classmates.insert(0,'D dot')
classmates.insert(3,'grace')
classmates.insert(5,'ridwan')
print(classmates)

#Removing element fromt the list
print("\nOFTEN YOU'LL WANT TO REMOVE ITEM OR SET FROM A LIST\n")
print(classmates)
del classmates[2]
print(classmates)

#Removing item using pop
print("\nREMOVING ITEM FROM THE LIST USING POP\n")
popped_classmate = classmates.pop()
print(classmates)
