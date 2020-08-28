def str_to_dict(some_str):  
    """
    returnes dictionary, where keys are string characters, and values are their quantity in the string
    :param some_str: str
    :return: dict
    """
    dict = {}
    for i in range(len(some_str)):
        if some_str[i] in dict:
            dict[some_str[i]] += 1
        else:
            dict[some_str[i]] = 1
    return dict

def sec_smallest(numbers):
    """
    returns second smallest item in the list, without using the built-in sorting methods
    :param numbers: list[int]
    :return: int    
    """
    min = numbers[0]
    min2 = numbers[0]
    for i in range(1,len(numbers)):
        if numbers[i] < min:
            min = numbers[i]
    for i in range(1,len(numbers)):
        if (numbers[i] < min2) and (numbers[i] != min):
            min2 = numbers[i]
    return min2

def prime_nums(n):
    """
    returns list of numbers which are simple and < n
    :param n: int
    :return: list[int]
    """
    result = []

    if (n>2):
        result.append(2)
        for i in range(3,n):
            flag = True
            for div in range(2,((i//2)+1)):
                if (i % div == 0):
                    flag = False
                    break
            if flag: result.append(i)

    return result

def max_sum_index(tuples):  
    '''
    returnes index of tuple in the list with maximum sum of elements
    :param tuples: list[tuple]
    :return: int
    '''
    max = sum(tuples[0])
    maxInd = 0
    for i in range(0,len(tuples)):
        if (sum(tuples[i]) > max):
            max = sum(tuples[i])
            maxInd = i
    return maxInd
    
def gcd(x, y):   
    '''
    returns the greatest common divisor of n and m
    :params m,n: int
    :return: int
    '''
    result = 1
    for i in range(2, min(x,y)+1):
        if ((x%i==0) and (y%i==0)):
            result = i
    return result

def recursive_list_sum(data_list):
    """
    :param data_list: list[list]
    """
    sum = 0
    for i in data_list:
        if (type(i) is not list):
            sum += i
        else:
            sumList = recursive_list_sum(i)
            sum += sumList
    return sum

def debug(func):
    """
    returns function signature and it's return value
    :param func: function
    """
    def wrapper(*args):
        result = func(*args)
        print('{0}{1} was called and returned {2}'.format(func.__name__, args, result))
    return wrapper

class Conv:
    def __init__(self):
        self.val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        self.syb = [
            'M', 'CM', 'D', 'CD',
            'C', 'XC', 'L', 'XL',
            'X', 'IX', 'V', 'IV',
            'I'
        ]
        
    def to_roman(self, num):    
        """
        converts decimal numbers to Roman numerals
        :param self:
        :param n: int
        :return: str    
        """
        n = num
        i = 0
        result = ''
        for i in range (0,len(self.val)):
            while (n - self.val[i] >= 0):
                n = n - self.val[i]
                result = result + self.syb[i]
            if (n == 0):
                break
        return result

        