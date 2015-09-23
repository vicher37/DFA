__author__ = 'vickyzhang'

from pandas import read_csv
def process():
    words = read_csv('american-words.80', header=None)
    def get_value(word):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        sum = 0
        for letter in word:
            letter_value = letters.find(letter)
            if letter_value == -1:
                letter_value = 0
            sum += letter_value
        return sum
    words['values'] = words[0].apply(get_value)
    words = words[words['values'] == 100]
    words['length'] = words[0].apply(len)
    words = words.sort(columns='length')
    print(words)

if __name__ == '__main__':
    process()