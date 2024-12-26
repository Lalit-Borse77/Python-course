# 1.check vowel or concenent

# vc="d"
# if vc=="a" or vc=="e" or vc=="i" or vc=="o" or vc=="u":
#     print("vowel")
# else:
#     print("concenent")

# 2.reverse a string

# a=("jay")[::-1]
# print(a)

# 3.convert a number from decimal to binary

# def tobinary(n):
#     if n>1:
#         tobinary(n//2)
#     print(n%2,end='')
# dec=287
# tobinary(dec)
# print()

# 4.reverse a number

# num=1234
# revers=0
# while num != 0:
#     digit = num % 10
#     revers=revers * 10 + digit
#     num //= 10
# print("reverse number :- "+str(revers))

# 5.Find duplicate character from a string


# def duplicate_characters(string):
# 	# Create an empty dictionary
# 	chars = {}

# 	# Iterate through each character in the string
# 	for char in string:
# 		# If the character is not in the dictionary, add it
# 		if char not in chars:
# 			chars[char] = 1
# 		else:
# 			# If the character is already in the dictionary, increment the count
# 			chars[char] += 1

# 	# Create a list to store the duplicate characters
# 	duplicates = []

# 	# Iterate through the dictionary to find characters with count greater than 1
# 	for char, count in chars.items():
# 		if count > 1:
# 			duplicates.append(char)

# 	return duplicates

# # Test cases
# print(duplicate_characters("geeksforgeeks"))

# 6.check if two string are a rotation of each other.

# str1 = "abcde";  
# str2 = "deabc";  

# if(len(str1) != len(str2)):  
#     print("Second string is not a rotation of first string");  
# else:  
#     try:  
#         #Concatenate str1 with str1 and store it in str1  
#         str1 = str1 + str1;  
#         #Check whether str2 is present in str1  
#         if(str1.index(str2)):  
#             print("Second string is a rotation of first string");  
#     except ValueError:  
#             print("Second string is not a rotation of first string");  

# 7.remove duplicates from array.

# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)

# 8.find the missing number in a given integer array of 1 to 100.

# def find_missing_number(nums):
#     return (100 * 101) // 2 - sum(nums)

# nums = list(range(1, 101))
# nums.remove(3)
# print(find_missing_number(nums))

# 9.find the 2nd largest number in an unsorted integer array.

# def find_2nd_largest(nums):
#     unique_nums = sorted(set(nums), reverse=True)
#     if len(unique_nums) < 2:
#         return None
#     return unique_nums[1]
# nums = [4, 2, 9, 6, 5, 1, 8, 3, 7]
# print("The 2nd largest number is:", find_2nd_largest(nums))

# 10.print next 20 leap years.

# def is_leap_year(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# def print_next_leap_years(n):
#     year = 2024  # Starting from the next leap year
#     count = 0
#     while count < n:
#         if is_leap_year(year):
#             print(year)
#             count += 1
#         year += 1
# print("The next 20 leap years are:")
# print_next_leap_years(20)

# 11.find prime numbers between 100 and 1000.

# def find_primes(start, end):
#     return [num for num in range(start, end + 1) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]

# print(find_primes(100, 1000))

# 12.convert any number to its equivalent word.

# def num_to_words(num):
#     d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
#         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
#         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
#         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
#         19: 'nineteen', 20: 'twenty',
#         30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
#         70: 'seventy', 80: 'eighty', 90: 'ninety'}
#     if num < 20:
#         return d[num]
#     elif num < 100:
#         return d[num // 10 * 10] + '-' + d[num % 10]
#     elif num < 1000:
#         return d[num // 100] + ' hundred and ' + num_to_words(num % 100)

# print(num_to_words(123))  # one hundred and twenty-three

# 13.return an array containing the digits of a given number.

# def get_digits(num):
#     return [int(d) for d in str(abs(num))]

# # Example usage:
# print(get_digits(12345))  # [1, 2, 3, 4, 5]
# print(get_digits(-67890))  # [6, 7, 8, 9, 0]

# 14.sort a given array of integer. 

# def sort_array(arr):
#     return sorted(arr)

# # Example usage:
# print(sort_array([5, 2, 8, 3, 1, 6, 4]))  # [1, 2, 3, 4, 5, 6, 8]

# 15.reverse a given array.

# arr = [1, 2, 3, 4, 5]
# arr = arr[::-1]
# print(arr)  # [5, 4, 3, 2, 1]

# 16.remove duplicate nodes in an unsorted linked list.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def remove_duplicates(head):
#     seen = set()
#     current = head
#     prev = None
#     while current:
#         if current.data in seen:
#             prev.next = current.next
#         else:
#             seen.add(current.data)
#             prev = current
#         current = current.next
#     return head

# 17.find the length of a singly linked list.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def length(head):
#     count = 0
#     current = head
#     while current is not None:
#         count += 1
#         current = current.next
#     return count

# b=(1)
# print(type(b))
# b=(1,)
# print(type(b))

# word="abcdefghij"
# print(word[:3]+word[3:])

# lambda

# X=lambda a,b:a&b
#     print(X(2,4))

# a=lambda x:x*2
# print(a(10))

# SLEEP

# import time
# print("welcome")
# time.sleep(3)
# print("this is show after 3 seconds")

# from math import pi
# print(pi)
