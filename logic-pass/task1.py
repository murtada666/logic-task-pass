user_char = str(input("enter the desired char that you want it to be removed: "))
user_string = str(input("enter the sentence: "))

print ("Original string: " + user_string) 

#Empty string
result_str = "" 
   
for i in range(0, len(user_string)): 
    if i is not user_char[0]:
       result_str = user_string.replace(user_char[0],"")
    
    
#main
print ("String after removal of the given character : " + result_str)