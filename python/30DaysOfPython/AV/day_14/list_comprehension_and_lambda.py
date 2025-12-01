"""
Day 14 in 30 Day Of Pyhton - List comprehension y functions lambdas.
"""

# 1.Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

numbers_filters = [number for number in numbers if number <= 0]

# 2.Flatten the following list of lists of lists to a one dimensional list

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattern_list = [number for row1 in list_of_lists for row2 in row1 for number in row2]

# 3.Using list comprehension create the following list of tuples:
"""
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
"""
number_list = [(i, i*0+1, i, i*i, i*i*i, i*i*i*i, i*i*i*i*i) for i in range(11)]

# 4.Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

#flattern_countries_lis = [[country, country[0:2] country] for row in countries for ]


