import os
# 1) python fileni yonidagi barcha txt fayllarni umumiy so'zlarini sonini qaytarish (file soni qancha bo'lsa shuncha protses yaratilinishi kerak) 

def count_txt_files(folder_path):
    count = 0
    for item in os.listdir(folder_path):
        if item.endswith(".txt") :
            count += 1
    return count

def get_folder_names(folder_path):
    folders = []
    for item in os.listdir(folder_path):
        if item.endswith('.txt') :
            folders.append(item)
    return folders

def reader(file_name):
    with open(file_name, 'r') as file:
        result = file.read()
        return result

def word_counter(text):
    result = text.split()
    return len(result)


# 6) rasmlarning urllarini ozida jamlovchi list oching va har bir listni ichidagi elementlar soniga qarab protsess yarating. Har protses o`sha rasmni yuklab olish vazofasini bajarsin

# 7) css darslarini 20tasini tugatish

