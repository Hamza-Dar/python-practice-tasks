s= input("Enter your string: ")

num_count= sum(i.isdigit() for i in s)
char_count= sum(i.isalpha() for i in s)

print("LETTERS: " +str(char_count))
print("DIGITS: " +str(num_count))
