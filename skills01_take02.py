# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", 
                "sausage", "spam", "spam", "bacon",
                "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    # odd_list = []
    # for num in number_list:
    #     if num % 2 != 0:
    #         odd_list.append(num)
    odd_list = [num for num in number_list if num % 2!= 0]

    return odd_list

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    even_list = [num for num in number_list if num % 2 == 0]
    return even_list

# Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
def long_words(word_list):
    long_words = [word for word in word_list if len(word) >= 4]
    return long_words

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    smallest_int = 0
    for num in number_list:
        smallest_int = min(num, smallest_int)
    return smallest_int
"""
last pass at this used "sorted" function:
"""
# def smallest(number_list):
#     new_list = sorted(number_list)
#     return new_list[0]


# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    largest_int = 0
    for num in number_list:
        largest_int = max(num, largest_int)
    return largest_int

"""
previous version used "sorted" returning index[-1],
and also a longer form version:
"""
# def largest(number_list):
#     largest_elem = 0
#     for num in number_list:
#         if num > largest_elem:
#             largest_elem = num
#     return largest_elem


# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    halfs_list = [num / 2.0 for num in number_list]
    return halfs_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    len_list = [len(word) for word in word_list]
    return len_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    result = 0
    for num in number_list:
        result = result + num
    return result

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    result = 1
    for num in number_list:
        result = result * num
    return result

# Write a function that joins all the strings in a list together
# (without using the join method) and returns a single string.
def join_strings(word_list):
    new_string = ""
    for word in word_list:
        new_string = new_string + word
    return new_string

# Write a function that takes a list of integers and returns the average
# (without using the avg method)
def average(number_list):
    count = 0
    sum = 0.0
    for num in number_list:
        sum = sum + num
        count += 1
    average = sum / count     

    return average

"""
last pass used a super concise variation on this one:
"""
# def average(number_list):
#     return float(sum_numbers(number_list))/len(number_list)


