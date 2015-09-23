__author__ = 'vickyzhang'

from pandas import read_csv
def process():
    """
        The main process. It reads in a txt file, assigns values to each word, and sorts it according to the value.
    """
    words = read_csv('american-words.80', header=None)
    def get_value(word):
        """
            A sub-process run on each word. It gets the value of each letter, and add up the values for the whole word.
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        sum = 0
        for letter in word:
            letter_value = letters.find(letter)
            if letter_value == -1:
                letter_value = 0
            sum += letter_value
        return sum
    words['values'] = words[0].apply(get_value)
    # get those words whose values are 100
    words = words[words['values'] == 100]
    # get the length of these words and sort ascending
    words['length'] = words[0].apply(len)
    words = words.sort(columns='length')
    return words

if __name__ == '__main__':
    print(process())