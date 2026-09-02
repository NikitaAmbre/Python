#Practice Questions on user defined func

# 1. Write a function that takes two numbers as arguments and prints the larger number.
def larger(a, b):
    if a > b:
        print("Larger number is:", a)
    else:
        print("Larger number is:", b)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
larger(num1, num2)

# 2. Write a function that takes a string and returns the first character that appears only once.
def first_unique(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None
text = input("Enter a string: ")

result = first_unique(text)
print("First non-repeating character:", result)

# 3. Write a function that takes a list and moves all 0s to the end while maintaining the order of the other elements.
def move_zeros(numbers):
    result = []
    for num in numbers:
        if num != 0:
            result.append(num)
    for num in numbers:
        if num == 0:
            result.append(num)
    return result
numbers = [0, 1, 0, 3, 12]
print("Original list:", numbers)
print("New list:", move_zeros(numbers))

# 4. Write a function that takes a sentence and returns the longest word.
def longest_word(sentence):
    words = sentence.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
sentence = input("Enter a sentence: ")
print("Longest word is:", longest_word(sentence))

# 5. Write a function that takes a list and returns a new list after removing duplicates.[donot use set]
def remove_duplicates(numbers):
    new_list = []
    for num in numbers:
        if num not in new_list:
            new_list.append(num)
    return new_list
numbers = [1, 2, 2, 3, 1, 4, 3]
print("Original list:", numbers)
print("List after removing duplicates:", remove_duplicates(numbers))
