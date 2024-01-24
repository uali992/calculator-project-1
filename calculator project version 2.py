#!/usr/bin/env python
# coding: utf-8

# In[17]:


print("Select an operation to perform")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

operation = input()

if operation == "1":
    numb1 = input("Enter first number: ")
    numb2 = input("Enter second number: ")
    print("The sum is " + str(int(numb1) + int(numb2)))

elif operation == "2":
    numb1 = input("Enter first number: ")
    numb2 = input("Enter second number: ")
    print("The sum is " + str(int(numb1) - int(numb2)))
elif operation == "3":
    numb1 = input("Enter first number: ")
    numb2 = input("Enter second number: ")
    print("The sum is " + str(int(numb1) * int(numb2)))
elif operation == "4":
    numb1 = input("Enter first number: ")
    numb2 = input("Enter second number: ")
    print("The sum is " + str(int(numb1) / int(numb2)))
else:
    print("Invalid Entry")


# In[ ]:





# In[ ]:




