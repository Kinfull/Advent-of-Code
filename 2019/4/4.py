passwords = 0


for i in range(193651, 649729):
    index = 1
    for j in str(i):        
        if j == str(i[index]):
            for k in str(i):
                if k == i:
                    passwords += 1
                    break  
            break
        if index < len(i):
            index += 1  


print(passwords)
        