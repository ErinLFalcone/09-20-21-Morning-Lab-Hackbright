"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums


def get_odd_indices(items):
    
    odd_indexes = []

    i = 1

    while i <= len(items):
        odd_indexes.append(items[i])
        i += 2
    
    return odd_indexes

    


def print_as_numbered_list(items):
    
    i=1

    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    
    i = start
    while i < stop:
        print(i)
        i += 1


def censor_vowels(word):
    
    chars = ""
    vowels = "aeiou"

    for letter in word:
        if letter in vowels:
            chars += "*"
        else:
            chars += letter

    return chars


def snake_to_camel(string):
    
    camel = []

    camel = string.split("_")

    camel_string = ""

    for word in camel:
        camel_string += word.title()
    
    return camel_string

def longest_word_length(words):
    
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return len(longest)


def truncate(string):
    
    result = ""

    for char in string:
        if char != result[-1]:
            result += char
    
    return result


def has_balanced_parens(string):
    
    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
    
    if parens != 0:
        return False
    else:
        return True
    


def compress(string):
    
    # result = ""
    # i = 1
    # for char in string:
    #     if char != result[-1]:
    #         if i != 1:
    #             result += i
    #         i = 1
    #         result += char
        
    #     else:
    #         i += 1
    
    # return result
    
