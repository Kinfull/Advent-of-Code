with open(r"2020\2\2.txt", "r") as f:
    passwordDict = [cords.rstrip("None") for cords in f.readlines()]


def PasswordFix(input_list):
    array = input_list[:]
    
    for index in array:
        """
        if(index[1] == "-"):
            lowerRange = index[0]
        else:
            lowerRange = index[0:1]
        if(index[3] == " "):
            upperRange = index[2]
        else:
            upperRange = index[2:3]
        if(index[4] != " "): 
            policy = index[4]
        else:
            policy = index[5]"""

PasswordFix(passwordDict)