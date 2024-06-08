from funcs import count_txt_files, get_folder_names, reader, word_counter
from string import punctuation

file_path = 'C:/najot talim/oy5/dars10'

def words_count(path):
    result = 0
    num = count_txt_files(path)
    for i in range(num):
        names = get_folder_names(path)
        text = reader(f"{names[i]}")
        result += word_counter(text)
    return result

def num_count_file(path):
    """...."""
    count = 0
    num = count_txt_files(path)
    for i in range(num):
        names = get_folder_names(path)
        text = reader(f"{names[i]}")
        for i in text:
            if i.isnumeric():
                count += 1
    return count

def sentance_count(path):
    result = 0
    num = count_txt_files(path)
    for i in range(num):
        names = get_folder_names(path)
        text = reader(f"{names[i]}")
        for i in text:
            if i =='.':
                result += 1
    return result

def longest_sentance(path):
    result = 0
    num = count_txt_files(path)
    for i in range(num):
        names = get_folder_names(path)
        text = reader(f"{names[i]}")
        data =text.split('. ')
        for sentence in data:
            length = len(sentence)
            if length > result:
                result = length     
                longest = sentence
    return f'{longest} is {result} words'

def punc_remove(path):
    result = ''
    num = count_txt_files(path)
    for i in range(num):
        names = get_folder_names(path)
        text = reader(f"{names[i]}")
        for i in text:
            if i not in punctuation:
                result += i
    return result
