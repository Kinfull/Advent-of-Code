valid_passwords = 0

def brute_force_passwords(password):
    double = False
    requirements = False
    if password[1] >= password[0]:
        if password[1] == password[0]:
            double = True
        if password[2] >= password[1]:
            if password[2] == password[1]:
                double = True
            if password[3] >= password[2]:
                if password[3] == password[2]:
                    double = True
                if password[4] >= password[3]:
                    if password[4] == password[3]:
                        double = True
                    if password[5] >= password[4]: 
                        if password[5] == password[4]:
                            double = True
                        if double:
                            requirements = True
                            password_list.append(password)
    return requirements, password_list

password_list = []

###########part 1###########
for i in range(193651, 649729):
    requirements, password_list = brute_force_passwords(str(i))
    if requirements:
        valid_passwords += 1

print(valid_passwords)

###########part 2###########
password2 = 0

for i in password_list:
    number_of_duplicates = {}
    for j in i:
        number_of_duplicates[j] = i.count(j)
    if 2 in number_of_duplicates.values():
            password2 += 1    

print(password2)