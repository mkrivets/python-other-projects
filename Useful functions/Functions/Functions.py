from module import *

print('Str to dict:', str_to_dict('Something interesting'))
print('Sec_smallest:', sec_smallest([1, 0, 0, 0, 0, 0]))
print('Prime numbers:', prime_nums(4))
print(max_sum_index([(10, 20), (40, 32), (30, 25), (340, 78, 289)]))
print(gcd(160, 180))
print('The sum of a list is:', recursive_list_sum([1, 2, [3,4],[5,6], [7, 8, 9,[10, 11]]]))
print('\n')

@debug
def add(a, b):
    return a + b
add(3, 4)
print('\n')

print('Converted:', Conv().to_roman(3056))
print('\n')
