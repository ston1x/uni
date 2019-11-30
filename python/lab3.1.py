def string_to_words(string, separator):
    try:
        return string.split(separator)
    except Exception as e:
        print(e)

try:
    string = input("Enter the string divided by a separator: ")
    separator= input("Enter the character by which the string will be splitted (separator): ")
except Exception as e:
    print(e)
words = string_to_words(string, separator)
print(words)
