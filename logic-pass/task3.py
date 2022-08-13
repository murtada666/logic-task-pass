def repeated_char (userChar, sentence):
    count = sentence.count(userChar)

    return count

#user input    
desired_char = str(input("enter the desired char: "))
user_string = str(input("enter the sentence: "))
#main
print ( "the count is: " + str(repeated_char(desired_char, user_string)))