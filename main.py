data = ['Asad', 'Vohid', "Mmu_hamadaziz", 'uhamMmadaidyubxon', 'udratulloP']

def sorting(word):
    count= 0 
    for letter in word:
        if letter.isupper():
            count+= 1

            
    if count == 1:
        if word.istitle():
            return 1
        elif word[-1].islower(): return 2
        else:  return 3
    else: raise ValueError

data.sort(key=sorting)
print(data)