# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam",
            "sausage","spam", "spam", "bacon",
            "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    odd_list = [item for item in number_list if item % 2 !=0]
    return odd_list

# print all_odd(number_list)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    even_list = [item for item in number_list if item %2 == 0]

    # below is long form version of the
    # list comrehension above, for reference
    # even_list = []
    # for item in number_list:
    #         if item % 2 == 0:
    #             even_list.append(item)

    return even_list

#print all_even(number_list)

# Write a function that takes a list of strings and RETURNS a new list with all strings of length 4 or greater.
def long_words(word_list):
    string_longer_than_four = [word for word in word_list if len(word)>=4]
    return string_longer_than_four

# print long_words(word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    new_list = sorted(number_list)
    return new_list[0]

# print smallest(number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    # joel says redo it the long way
    # new_list = sorted(number_list)
    # return new_list[-1]

    largest_elem = 0
    for num in number_list:
        if num > largest_elem:
            largest_elem = num
    return largest_elem

# print number_list
# print largest(number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    new_list = [numbers/2.0 for numbers in number_list]
    return new_list

# print halvesies(number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):

    # written with for loop
    # word_len_list = []
    # for word in word_list:
    #     word_len_list.append(len(word))
    # return word_len_list

    # written with list comprehension
    word_len_list = [len(word) for word in word_list]
    return word_len_list

# print word_list
# print word_lengths(word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    sum = 0
    for num in number_list:
        sum += num
    return sum

# print number_list
# print sum_numbers(number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    result = 1
    for num in number_list:
        result *= num
    return result

# print number_list
# print mult_numbers(number_list)

# Write a function that joins all the strings in a list together
# (without using the join method) and returns a single string.
def join_strings(word_list):

    long_string = ""
    for word in word_list:
        long_string += word
    return long_string

# print word_list
# print join_strings(word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return float(sum_numbers(number_list))/len(number_list)

print number_list
print sum_numbers(number_list)
print len(number_list)
print average(number_list)

# code review by heather -- done before 5 pm!