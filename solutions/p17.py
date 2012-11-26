# p17.py
#
# Solution to Project Euler problem 17
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.

# ALGORITHM
# One very useful class is defined. This class is able, among other things,
# to convert an int to a string of that integer written out. For example,
# the integer 38 would become 'thirty-eight'. Addition of the objects is
# also supported.
#
# In the interest of reusability, numbers up to 1e12 - 1 (one less than one
# trillion) are converted to words.

from solutionTimer import start, stop
import re

base_ints_to_words = {1: 'one',
                    2: 'two',
                    3: 'three',
                    4: 'four',
                    5: 'five',
                    6: 'six',
                    7: 'seven',
                    8: 'eight',
                    9: 'nine',
                    10: 'ten',
                    11: 'eleven',
                    12: 'twelve',
                    13: 'thirteen',
                    14: 'fourteen',
                    15: 'fifteen',
                    16: 'sixteen',
                    17: 'seventeen',
                    18: 'eighteen',
                    19: 'nineteen',
                    20: 'twenty',
                    30: 'thirty',
                    40: 'forty',
                    50: 'fifty',
                    60: 'sixty',
                    70: 'seventy',
                    80: 'eighty',
                    90: 'ninety'}

powers_of_ten = ['', 'thousand', 'million', 'billion', 'trillion']

class NumericWord(object):
    __MAX_NUMBER = int(1e12-1)
    def __init__(self, num, extraAnds=False):
        '''NumericWord(num) -> new NumericWord object using the integer num'''
        NumericWord.check_max_number(num) # Is num too big/small?
        
        self.__numAsInt = num
        self.__extraAnds = extraAnds
        self.__numAsWord = NumericWord.word(self.__numAsInt, self.__extraAnds)
    
    def __int__(self):
        return self.__numAsInt
    
    def __str__(self):
        return self.__numAsWord
    
    def __add__(self, other):
        if isinstance(other, int):
            new_num = self.__numAsInt + other
        else:
            new_num = self.__numAsInt + other.__numAsInt
        return NumericWord(new_num, extraAnds=self.__extraAnds)
    
    def __sub__(self, other):
        if isinstance(other, int):
            new_num = self.__numAsInt - other
        else:
            new_num = self.__numAsInt - other.__numAsInt
        return NumericWord(new_num, extraAnds=self.__extraAnds)
    
    def __cmp__(self, other):
        return self.__numAsInt - other.__numAsInt
    
    def __repr__(self):
        return 'p17.NumericWord(%d, extraAnds=%s)' % (self.__numAsInt, self.__extraAnds)
    
    
    @staticmethod
    def check_max_number(num):
        if not isinstance(num, int):
            raise TypeError, 'Argument num must be an integer.'
        if num < -NumericWord.__MAX_NUMBER or num > NumericWord.__MAX_NUMBER:
            raise ValueError, 'Argument num must be between '+ \
                str(-NumericWord.__MAX_NUMBER) + ' and ' + str(NumericWord.__MAX_NUMBER)
    
    @staticmethod
    def word(num, extraAnds=False):
        '''NumericWord.word(num, extraAnds=False) -> str
        
        Returns the word-form of the int num as a string.
        
        >>> NumericWord.word(535)
        'five hundred thirty-five'
        >>> NumericWord.word(535, extraAnds=True)
        'five hundred and thirty-five
        
        '''
        NumericWord.check_max_number(num)
        if num == 0:
            return 'zero'
        if num < 0:
            negative = True
            num *= -1
        else:
            negative = False
        # Convert num from 25311 to ['25', '311'], for example.
        grouped_digit_list = []
        int_str = str(num) # int_str == '25311'
        while True:
            grouped_digit_list.insert(0, int_str[-3:])
            int_str = int_str[:-3]
            if 1 <= len(int_str) <= 3:
                grouped_digit_list.insert(0, int_str)
                break
            if len(int_str) == 0:
                break
        
        # Convert each element in groupd_digit_list to proper word form
        grouped_digit_words = [] # Will hold ['twenty-five', 'three hundred eleven']
        for dig in grouped_digit_list: # dig is a string, like '532' or '1'
            dig_int = int(dig)
            if dig_int == 0:
                grouped_digit_words.append('')
                continue
            new_str = '' # Need to do actual work
            if len(dig) == 3 and dig[0] != '0': # Have to deal with hundreds
                new_str += base_ints_to_words[int(dig[0])] + ' hundred '
                if dig[-2:] == '00': # Are we done with this group?
                    grouped_digit_words.append(new_str[:-1]) # Get rid of space
                    continue
            if extraAnds and len(dig) == 3: # British
                new_str += 'and '
            # Ready to deal with the last two digits
            try: # One of the 'special' numbers in base_ints_to_words?
                new_str += base_ints_to_words[int(dig[-2:])]
                grouped_digit_words.append(new_str)
                continue
            except KeyError: # Not a 'special' number in base_ints_to_words
                new_str += base_ints_to_words[int(dig[-2])*10]
                new_str += '-'
                new_str += base_ints_to_words[int(dig[-1])]
                new_str += ' '
                grouped_digit_words.append(new_str[:-1])
        
        tens_idx = 0
        number_groups = []
        for words in grouped_digit_words[-1::-1]:
            if words != '':
                complete_group = words
                if powers_of_ten[tens_idx] != '':
                    complete_group += ' ' + powers_of_ten[tens_idx]
                number_groups.insert(0,complete_group)
            tens_idx += 1
        
        num_as_str = ' '.join(number_groups)
        if negative:
            num_as_str = 'negative ' + num_as_str
        return num_as_str

if __name__ == '__main__':
    start()
    count = 0
    for num in range(1, 1000 + 1):
        num_str = NumericWord.word(num, extraAnds=True)
        print num_str
        count += len(re.findall(r'[a-z]', NumericWord.word(num, extraAnds=True)))
    print 'Problem 17 ->', count
    stop()