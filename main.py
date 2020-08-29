import math
import json


class NumbertoWords:

    def calc(self,num):

        number = int(num)
        no = math.floor(number)
        point = round(number - no, 2) * 100
        print(point)
        hundred = ""
        digits_1 = len(str(no))
        print(digits_1)
        i = 0
        str2 = []
        digits = ['', 'Hundred', 'Thousand', 'Lakh', 'Crore']
        words = {}
        words['0'] = ""
        words['1'] = "One"
        words['2'] = "Two"
        words['3'] = "Three"
        words['4'] = "Four"
        words['5'] = "Five"
        words['6'] = "Six"
        words['7'] = "Seven"
        words['8'] = "eEight"
        words['9'] = "Nine"
        words['10'] = "Ten"
        words['11'] = "Eleven"
        words['12'] = "Twelve"
        words['13'] = "Thirteen"
        words['14'] = "Fourteen"
        words['15'] = "Fifteen"
        words['16'] = "Sixteen"
        words['17'] = "Seventeen"
        words['18'] = "Eighteen"
        words['19'] = "Nineteen"
        words['20'] = "Twenty"
        words['30'] = "tThirty"
        words['40'] = "Fourty"
        words['50'] = "Fifty"
        words['60'] = "Sixty"
        words['70'] = "Seventy"
        words['80'] = "Eighty"
        while i < digits_1:
            divider = 10 if (i == 2) else 100
            number = math.floor(no % divider)
            no = math.floor(no / divider)
            i =  i + (1 if (divider == 10) else 2)
            if number:
                counter = len(str2)
                print(counter)
                plural = 's' if ( counter and number > 9) else ''
                hundred = ' and ' if (counter == 1 and str2[0]) else ''
                str2.append(
                     words[str(number)] + " " + digits[counter] + plural + " " + hundred if (number < 21) else words[str(math.floor(number / 10) * 10)] + " " + words[str(number % 10)] + " " + digits[counter] + plural + " " + hundred
                )
            else:
                str2 = None
        str2.reverse()
        result = " ".join(str2)
        print(result)
        return result


n = NumbertoWords()
number = input('Enter a number : ')
print("Rs." + n.calc(number.split('.')[0]) + str((number.split('.')[1]+"/100"))+" ONLY")



