text = "  Hello123 World  "
word = "Python"
number = "12345"
spaces = "   \t   "
first_name = "PRABHAT"
last_name = "mishra"
csv_data = "apple,mango,banana"
filename = "reports.pdf"
sentence = "I like Java"

# repr preserves the exact quotes and literals
print("Original text:", repr(text))

print(f"{word} is alphabets:", word.isalpha()) # True
print(f"{word} is alpha numeric", word.isalnum()) # True

print(f"{text} is alpha numeric:", text.isalnum()) # False (contains spaces)

print(f"{number} is digit" , number.isdigit()) # True
print(f"{word} is digit" , word.isdigit()) # False

print(f"{first_name} is upper :" , word.isupper()) # True
print(f"{last_name} is lower :" , word.islower()) # True

print(f"lets convert {first_name} to lower case", first_name.lower()) # "prabhat"
print(f"lets convert {last_name} to upper case", last_name.upper()) # "MISHRA"

print(f"check if {spaces} is white spaces", spaces.isspace()) # True
print(f"check if {text} is white spaces", text.isspace()) # False

print(f"lets right strip the spaces from {text}", text.rstrip())
print(f"lets left strip the spaces from {text}", text.lstrip())
print(f"lets strip the spaces from {text}", text.strip())

print(f"filename endswith .pdf:", filename.endswith(".pdf")) # True
print(f"filename starts with rep:", filename.startswith("rep")) # True

print(f"{sentence} and", sentence.replace("Java", 'Python'))

fruits = csv_data.split(",")
print("Fruits from csv data:", fruits)

joined = " | ".join(fruits)
print(F"All the fruits :", joined)



