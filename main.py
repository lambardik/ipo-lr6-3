num_strings = int(input("введите число строк: "))  
if num_strings <=0:  
    print("oшибочка")   
strings =[]   
for i in range(num_strings): 
    string = str(input("введите строку: "))   
    strings.append(string)   
words =[]   
for string in strings:  
    word = string.split()   
    for i in word:   
        if i not in words:   
            words.append(i)   
count = len(words)   
print("Кол-во слов: ", count)   