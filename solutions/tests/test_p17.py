# test_p17.py
#
# Unit tests for Project Euler problem 17

from p17 import *
import unittest

class IntToWordsTest(unittest.TestCase):
    def test_known_values(self):
        #self.assertEqual(NumericWord.word(0, extraAnds=True), 'zero')
        self.assertEqual(NumericWord.word(1, extraAnds=True), 'one')
        self.assertEqual(NumericWord.word(2, extraAnds=True), 'two')
        self.assertEqual(NumericWord.word(3, extraAnds=True), 'three')
        self.assertEqual(NumericWord.word(4, extraAnds=True), 'four')
        self.assertEqual(NumericWord.word(5, extraAnds=True), 'five')
        self.assertEqual(NumericWord.word(6, extraAnds=True), 'six')
        self.assertEqual(NumericWord.word(7, extraAnds=True), 'seven')
        self.assertEqual(NumericWord.word(8, extraAnds=True), 'eight')
        self.assertEqual(NumericWord.word(9, extraAnds=True), 'nine')
        self.assertEqual(NumericWord.word(10, extraAnds=True), 'ten')
        self.assertEqual(NumericWord.word(11, extraAnds=True), 'eleven')
        self.assertEqual(NumericWord.word(12, extraAnds=True), 'twelve')
        self.assertEqual(NumericWord.word(13, extraAnds=True), 'thirteen')
        self.assertEqual(NumericWord.word(14, extraAnds=True), 'fourteen')
        self.assertEqual(NumericWord.word(15, extraAnds=True), 'fifteen')
        self.assertEqual(NumericWord.word(16, extraAnds=True), 'sixteen')
        self.assertEqual(NumericWord.word(17, extraAnds=True), 'seventeen')
        self.assertEqual(NumericWord.word(18, extraAnds=True), 'eighteen')
        self.assertEqual(NumericWord.word(19, extraAnds=True), 'nineteen')
        self.assertEqual(NumericWord.word(20, extraAnds=True), 'twenty')
        self.assertEqual(NumericWord.word(21, extraAnds=True), 'twenty-one')
        self.assertEqual(NumericWord.word(22, extraAnds=True), 'twenty-two')
        self.assertEqual(NumericWord.word(23, extraAnds=True), 'twenty-three')
        self.assertEqual(NumericWord.word(24, extraAnds=True), 'twenty-four')
        self.assertEqual(NumericWord.word(25, extraAnds=True), 'twenty-five')
        self.assertEqual(NumericWord.word(26, extraAnds=True), 'twenty-six')
        self.assertEqual(NumericWord.word(27, extraAnds=True), 'twenty-seven')
        self.assertEqual(NumericWord.word(28, extraAnds=True), 'twenty-eight')
        self.assertEqual(NumericWord.word(29, extraAnds=True), 'twenty-nine')
        self.assertEqual(NumericWord.word(30, extraAnds=True), 'thirty')
        self.assertEqual(NumericWord.word(31, extraAnds=True), 'thirty-one')
        self.assertEqual(NumericWord.word(40, extraAnds=True), 'forty')
        self.assertEqual(NumericWord.word(41, extraAnds=True), 'forty-one')
        self.assertEqual(NumericWord.word(50, extraAnds=True), 'fifty')
        self.assertEqual(NumericWord.word(51, extraAnds=True), 'fifty-one')
        self.assertEqual(NumericWord.word(60, extraAnds=True), 'sixty')
        self.assertEqual(NumericWord.word(61, extraAnds=True), 'sixty-one')
        self.assertEqual(NumericWord.word(70, extraAnds=True), 'seventy')
        self.assertEqual(NumericWord.word(71, extraAnds=True), 'seventy-one')
        self.assertEqual(NumericWord.word(80, extraAnds=True), 'eighty')
        self.assertEqual(NumericWord.word(81, extraAnds=True), 'eighty-one')
        self.assertEqual(NumericWord.word(90, extraAnds=True), 'ninety')
        self.assertEqual(NumericWord.word(91, extraAnds=True), 'ninety-one')
        self.assertEqual(NumericWord.word(100, extraAnds=True), 'one hundred')
        self.assertEqual(NumericWord.word(101, extraAnds=True),
                         'one hundred and one')
        self.assertEqual(NumericWord.word(102, extraAnds=True),
                         'one hundred and two')
        self.assertEqual(NumericWord.word(109, extraAnds=True),
                         'one hundred and nine')
        self.assertEqual(NumericWord.word(110, extraAnds=True),
                         'one hundred and ten')
        self.assertEqual(NumericWord.word(111, extraAnds=True),
                         'one hundred and eleven')
        self.assertEqual(NumericWord.word(120, extraAnds=True),
                         'one hundred and twenty')
        self.assertEqual(NumericWord.word(121, extraAnds=True),
                         'one hundred and twenty-one')
        self.assertEqual(NumericWord.word(130, extraAnds=True),
                         'one hundred and thirty')
        self.assertEqual(NumericWord.word(131, extraAnds=True),
                         'one hundred and thirty-one')
        self.assertEqual(NumericWord.word(199, extraAnds=True),
                         'one hundred and ninety-nine')
        self.assertEqual(NumericWord.word(200, extraAnds=True),
                         'two hundred')
        self.assertEqual(NumericWord.word(201, extraAnds=True),
                         'two hundred and one')
        self.assertEqual(NumericWord.word(240, extraAnds=True),
                         'two hundred and forty')
        self.assertEqual(NumericWord.word(255, extraAnds=True),
                         'two hundred and fifty-five')
        self.assertEqual(NumericWord.word(303, extraAnds=True),
                         'three hundred and three')
        self.assertEqual(NumericWord.word(404, extraAnds=True),
                         'four hundred and four')
        self.assertEqual(NumericWord.word(505, extraAnds=True),
                         'five hundred and five')
        self.assertEqual(NumericWord.word(606, extraAnds=True),
                         'six hundred and six')
        self.assertEqual(NumericWord.word(707, extraAnds=True),
                         'seven hundred and seven')
        self.assertEqual(NumericWord.word(808, extraAnds=True),
                         'eight hundred and eight')
        self.assertEqual(NumericWord.word(909, extraAnds=True),
                         'nine hundred and nine')
        self.assertEqual(NumericWord.word(999, extraAnds=True),
                         'nine hundred and ninety-nine')
        self.assertEqual(NumericWord.word(1000, extraAnds=True),
                         'one thousand')
        self.assertEqual(NumericWord.word(1001, extraAnds=True),
                         'one thousand and one')
        self.assertEqual(NumericWord.word(1111, extraAnds=True),
                         'one thousand one hundred and eleven')
        self.assertEqual(NumericWord.word(2222, extraAnds=True),
                         'two thousand two hundred and twenty-two')
        self.assertEqual(NumericWord.word(3333, extraAnds=True),
                         'three thousand three hundred and thirty-three')
        self.assertEqual(NumericWord.word(4444, extraAnds=True),
                         'four thousand four hundred and forty-four')
        self.assertEqual(NumericWord.word(5555, extraAnds=True),
                         'five thousand five hundred and fifty-five')
        self.assertEqual(NumericWord.word(6666, extraAnds=True),
                         'six thousand six hundred and sixty-six')
        self.assertEqual(NumericWord.word(7777, extraAnds=True),
                         'seven thousand seven hundred and seventy-seven')
        self.assertEqual(NumericWord.word(8888, extraAnds=True),
                         'eight thousand eight hundred and eighty-eight')
        self.assertEqual(NumericWord.word(9999, extraAnds=True),
                         'nine thousand nine hundred and ninety-nine')
        self.assertEqual(NumericWord.word(10000, extraAnds=True),
                         'ten thousand')
        self.assertEqual(NumericWord.word(10008, extraAnds=True),
                         'ten thousand and eight')
        self.assertEqual(NumericWord.word(10632, extraAnds=True),
                         'ten thousand six hundred and thirty-two')
        self.assertEqual(NumericWord.word(11611, extraAnds=True),
                         'eleven thousand six hundred and eleven')
        self.assertEqual(NumericWord.word(11999, extraAnds=True),
                         'eleven thousand nine hundred and ninety-nine')
        self.assertEqual(NumericWord.word(12190, extraAnds=True),
                         'twelve thousand one hundred and ninety')
        self.assertEqual(NumericWord.word(25000, extraAnds=True),
                         'twenty-five thousand')
        self.assertEqual(NumericWord.word(25006, extraAnds=True),
                         'twenty-five thousand and six')
        self.assertEqual(NumericWord.word(25030, extraAnds=True),
                         'twenty-five thousand and thirty')
        self.assertEqual(NumericWord.word(25400, extraAnds=True),
                         'twenty-five thousand four hundred')
        self.assertEqual(NumericWord.word(99999, extraAnds=True),
                         'ninety-nine thousand nine hundred and ninety-nine')
        self.assertEqual(NumericWord.word(100000, extraAnds=True),
                         'one hundred thousand')
        self.assertEqual(NumericWord.word(100001, extraAnds=True),
                         'one hundred thousand and one')
        self.assertEqual(NumericWord.word(195366, extraAnds=True),
                         'one hundred and ninety-five thousand three hundred and sixty-six')
        self.assertEqual(NumericWord.word(240609, extraAnds=True),
                         'two hundred and forty thousand six hundred and nine')
        self.assertEqual(NumericWord.word(903011, extraAnds=True),
                         'nine hundred and three thousand and eleven')
        self.assertEqual(NumericWord.word(int(1e6), extraAnds=True),
                         'one million')
        self.assertEqual(NumericWord.word(int(1e6 + 1), extraAnds=True),
                         'one million and one')
        self.assertEqual(NumericWord.word(2000020, extraAnds=True),
                         'two million and twenty')
        self.assertEqual(NumericWord.word(3000300, extraAnds=True),
                         'three million three hundred')
        self.assertEqual(NumericWord.word(4004000, extraAnds=True),
                         'four million four thousand')
        self.assertEqual(NumericWord.word(5050000, extraAnds=True),
                         'five million and fifty thousand')
        self.assertEqual(NumericWord.word(8800309, extraAnds=True),
                         'eight million eight hundred thousand three hundred and nine')
        self.assertEqual(NumericWord.word(10000000, extraAnds=True),
                         'ten million')
        self.assertEqual(NumericWord.word(10000411, extraAnds=True),
                         'ten million four hundred and eleven')
        self.assertEqual(NumericWord.word(10203040, extraAnds=True),
                         'ten million two hundred and three thousand and forty')
        self.assertEqual(NumericWord.word(52333000, extraAnds=True),
                         'fifty-two million three hundred and thirty-three thousand')
        self.assertEqual(NumericWord.word(700800208, extraAnds=True),
                         'seven hundred million eight hundred thousand two hundred and eight')
        self.assertEqual(NumericWord.word(999999999, extraAnds=True),
                         'nine hundred and ninety-nine million nine hundred and ninety-nine thousand nine hundred and ninety-nine')
        self.assertEqual(NumericWord.word(1000000000, extraAnds=True),
                         'one billion')
        self.assertEqual(NumericWord.word(8631911155, extraAnds=True),
                         'eight billion six hundred and thirty-one million nine hundred and eleven thousand one hundred and fifty-five')
        self.assertEqual(NumericWord.word(15630383711, extraAnds=True),
                         'fifteen billion six hundred and thirty million three hundred and eighty-three thousand seven hundred and eleven')
        self.assertEqual(NumericWord.word(980059103860, extraAnds=True),
                         'nine hundred and eighty billion fifty-nine million one hundred and three thousand eight hundred and sixty')

                         
                         
        
        
        
        
        
        
        
        
        
        
        
