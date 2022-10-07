# You will be given an array of numbers.
# You have to sort the odd numbers in ascending order
# while leaving the even numbers at their original positions.
# EXAMPLE BELOW
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
from typing import List
import re


def sort_array(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


print(sort_array([5, 3, 2, 8, 1, 4]))
print(sort_array([5, 3, 1, 8, 0]))


# You probably know the 'like' system from Facebook and other pages.
# People can 'like' blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item.
# Implement the function which takes an array containing the names of people that like an item.
# It must return the display text as shown in the examples:
# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
# []                                -->  'no one likes this'
# ['Peter']                         -->  'Peter likes this'
# ['Jacob', 'Alex']                 -->  'Jacob and Alex like this'
# ['Max', 'John', 'Mark']           -->  'Max, John and Mark like this'
# ['Alex', 'Jacob', 'Mark', 'Max']  -->  'Alex, Jacob and 2 others like this'

# def likes(names: List[str]) -> str:
#     word_like = ["like this", "likes this"]
#     statement = ""
#     if len(names) == 0:
#         statement = 'no one ' + word_like[1]
#     elif len(names) == 1:
#         statement = names[0] + ' ' + word_like[1]
#     elif len(names) == 2:
#         statement = names[0] + ' and ' + names[1] + ' ' + word_like[0]
#     elif len(names) == 3:
#         statement = names[0] + ', ' + names[1] + ' and ' + names[2] + ' ' + word_like[0]
#     elif len(names) > 3:
#         # finds the number of names without the first 2
#         remains: str = str(len(names) - 2)
#         statement = names[0] + ', ' + names[1] + ' and ' + remains + ' others ' + word_like[0]
#     return statement


# def likes(names):
#     if not names:
#         return 'no one likes this'
#     elif len(names) == 1:
#         return '{} likes this'.format(*names)
#     elif len(names) < 4:
#         return "{} and {} like this".format(", ".join(names[:len(names) - 1]), names[-1])
#     else:
#         return '{}, {} and {} others like this'.format(names[0], names[1], len(names) - 2)

# def likes(names):
#     return {
#         0: "no one likes this",
#         1: "{} likes this",
#         2: "{} and {} like this",
#         3: "{}, {} and {} like this"
#     }.get(len(names), "{}, {} and {length} others like this").format(*names, length=len(names) - 2)

def likes(names):
    result = {
        0: lambda _names: "no one likes this",
        1: lambda _names: "{0} likes this".format(_names[0]),
        2: lambda _names: "{0} and {1} like this".format(_names[0], _names[1]),
        3: lambda _names: "{0}, {1} and {2} like this".format(_names[0], _names[1], _names[2]),
        4: lambda _names: "{0}, {1} and {2} others like this".format(_names[0], _names[1], len(_names) - 2)
    }
    return result[len(names) if len(names) < 4 else 4](names)


def test_liskes_():
    expected = "Ama likes this"
    actual = likes(["Ama"])
    assert expected == actual


# print(likes([]))
print(likes(['Peter']))


# print(likes(['Max', 'Ama']))
# print(likes(['Max', 'John', 'Ama']))
# print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
# print(likes(['Angelina Kyeah', 'Emmanuel Asamoah', 'John', 'Ama', 'Kingsford', 'Mary']))
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
def to_jaden_case(string):
    result = [word.capitalize() for word in string.split(" ")]
    return " ".join(result)


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))


#  given a list of numbers and letters extract only the numbers
# Eg [1, 2, 'a', 'b'] ==> [1,2]
# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
def filter_list(l):
    return [x for x in l if type(x) == int]


print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 'a', 'b', 0, 15]))


# given 2 numbers add and return binary of sum
def add_binary(a, b):
    result = a + b
    return format(result, "b")


# split by space
# convert to a list
#  find the max and min value of the list
# join max and min value by space
def high_and_low(string: str) -> str:
    split_num = [int(x) for x in string.split(" ")]
    max_val = str(max(split_num))
    min_val = str(min(split_num))
    return max_val + " " + min_val


print(high_and_low("1 2 3 4 5 -6"))


# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
# Move the first letter of each word to the end of it,
# then add "ay" to the end of the word. Leave punctuation marks untouched.
# Example
# pig_it('Pig latin is cool') ==>  igPay atinlay siay oolcay
# pig_it('Hello world !')     ==>  elloHay orldway !
def pig_it(text: str) -> str:
    words = text.split(" ")
    f = map(lambda w: w[1:len(w)] + w[0], words)
    result: List[str] = []
    for x in f:
        result.append(x + "ay") if str(x).isalpha() else result.append(x)
    return " ".join(list(result))


print(pig_it("Pig latin is cool"))
print(pig_it('Hello world !'))


# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]
# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
def unique_in_order(string: str):
    string = string + '!'
    split_letters = [x for x in [*string]]
    count = -1
    result = []
    while count != len(split_letters) - 1:
        if split_letters[count] != split_letters[count + 1]:
            result.append(split_letters[count + 1])
        count += 1

    result.pop(-1)
    return result


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))


def insert_sort():
    num_list = []
    while True:
        num = int(input("Enter a number: "))
        num_list.append(num)
        num_list.sort()
        print("{} inserted at index {}: list ={}".format(num, num_list.index(num), num_list))


# insert_sort()


def valid_number(phone: List[str]):
    pattern = '[0-9]{3}\\-[0-9]{3}\\-[0-9]{4}$'
    count = 0
    while count < len(phone):
        result = phone[count] if re.match(pattern, phone[count]) else phone[count] + " in correct"
        print(result)
        count += 1


def valid_email(emails: List[str]):
    pattern = '[a-z]{2,15}\\.[a-z]{2,30}[\\@]gmail.com$'
    count = 0
    while count < len(emails):
        result = True if re.match(pattern, emails[count]) else False
        print(result)
        count += 1


valid_number(["054-867-0632", "0548670632"])
valid_email(["godfred.asas@gmail.com", "0548670632"])


def get_index(numbers: List[int]) -> List[str]:
    return [str(numbers.index(x)) for x in numbers]


print("index ", get_index([1, 2, 3, 4, 5, 6, 7]))


def counts(teamA, teamB):
    result = []
    item1 = []
    item2 = []
    size = len(teamB) - 1
    first_item = teamB[0]
    second_item = teamB[size]
    for x in teamA:
        for y in teamA:
            if x <= first_item:
                item1.append(x)
            elif y <= second_item:
                item2.append(y)
    return len(set(item1)), len(set(item2))


print(counts([1, 2, 3], [2, 4]))
