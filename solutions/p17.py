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
# Two useful functions are defined. One function converts an integer to
# a string of that integer in words (e.g., 4 -> four). Another function
# counts the number of alphabetic characters in a string. As for the algorithm,
# each number 1 through 1000 is converted into words. These words are run
# through the second function above and the running total calculated.
#
# In the interest of reusability, numbers up to 1e12 - 1 (one less than one
# trillion) are converted to words.

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
                    #100: 'hundred'}

powers_of_ten = ['', 'thousand', 'million', 'billion', 'trillion']

class NumericWord(object):
    __MAX_NUMBER = int(1e12-1)
    def __init__(self, num, extraAnds=False):
        '''NumericWord(num) -> new NumericWord object using the integer num'''
        NumericWord.check_max_number(num) # Raise exception of number is too big
        if not num >= 0:
            raise ValueError, 'Argument num must be a non-negative integer.'
        if not num <= NumericWord.__MAX_NUMBER:
            raise ValueError, 'Argument num must be less than or equal to', __MAX_NUMBER
        
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
        new_num = self.__numAsInt + other.__numAsInt
        return NumericWord(new_num, extraAnds=self.__extraAnds)
    
    @staticmethod
    def check_max_number(num):
        if num > NumericWord.__MAX_NUMBER:
            raise ValueError, 'Argument num must be less than ' + \
                str(NumericWord.__MAX_NUMBER)
    
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
            try: # Assume int(dig) as already in base_ints_to_words
                grouped_digit_words.append(base_ints_to_words[dig_int])
            except KeyError: # dig_int was not already in base_ints_to_words
                if dig_int == 0:
                    grouped_digit_words.append('')
                    continue
                new_str = '' # Need to do to actual work
                if len(dig) == 3 and dig[0] is not '0': # Deal with a three-group
                    new_str += base_ints_to_words[int(dig[0])] + ' hundred '
                    if dig[-2:] == '00': # Is there more to say after hundreds?
                        grouped_digit_words.append(new_str[:-1])
                        continue
                if extraAnds and len(dig) == 3 : # British?
                    new_str += 'and '
                # Now deal with the tens and ones
                try:
                    new_str += base_ints_to_words[int(dig[-2:])]
                    grouped_digit_words.append(new_str)
                    continue
                except KeyError:
                    if dig[-2] is not '0':
                        new_str += base_ints_to_words[int(dig[-2])*10]
                    if dig[-1] is not '0':
                        if dig[-2] is not '0': # The teens have already been dealt with
                            new_str += '-'
                        new_str += base_ints_to_words[int(dig[-1])] + ' '
                grouped_digit_words.append(new_str[:-1])
        
        tens_idx = 0
        number_groups = []
        for words in grouped_digit_words[-1::-1]:
            if words is not '':
                complete_group = words + ' ' + powers_of_ten[tens_idx]
                number_groups.insert(0,complete_group)
            tens_idx += 1
        #number_groups.append(grouped_digit_words[-1])
        
        num_as_str = ' '.join(number_groups)
        return num_as_str