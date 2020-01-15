#DAN + Encryption => DANCRYPTION
#Developped by Naveen Dhananjaya Hettiwaththa


import random

def encrypt(inptext , method , type):
    word_matrix = []
    cols = []
    primary = []
    secondary = []
    helper = []
    text = ""
    string = ""

    for i in range(len(inptext)):
        helper.append(inptext[i])

    for i in range(len(helper)):
        if helper[i] == " ":
            text += "#"
        else:
            text += helper[i]


    for i in range(len(text)):
        row = []
        for j in range(len(text)):
            row.append(text[i] + text[j])

        word_matrix.append(row)

        
    for i in range(len(word_matrix)):
        primary.append(word_matrix[i][i])

    for i in range(len(word_matrix)):
        secondary.append(word_matrix[i][len(word_matrix)- 1 - i])

        

    for i in range(len(word_matrix)):
        row = []
        for j in range(len(word_matrix[0])):
            row.append(word_matrix[j][i])

        cols.append(row)

    
    if len(type) == 0:
        row_num = random.randint(0 , len(word_matrix)-1)
        col_num = random.randint(0 , len(cols)-1)
        while row_num == col_num:
            row_num = random.randint(0 , len(word_matrix)-1)
            col_num = random.randint(0 , len(cols)-1)
    else:
        row_num = type[0]
        col_num = type[1]


    rand_row = word_matrix[row_num]
    rand_col = cols[col_num]

    # print(word_matrix[rand_row])
    # print(cols[rand_col])
    # print(secondary)

    if len(type) != 0:
        rand_row = word_matrix[type[0]]
        rand_col = cols[type[1]]
    if method == "crossed":
        string += "&&"
        for i in range(len(primary)):
            if primary[i][0] == secondary[i][0] and primary[i][1] == secondary[i][1]:
                string += str(random.randint(0 , 9))
            elif primary[i][0] == secondary[i][0]:
                string += primary[i][1] + secondary[i][1]

        return string
    elif method == "random":

        row_len = str(len(str(row_num)))
        col_len = str(len(str(col_num)))

        string += str(row_num)
        string += "-"
        string += str(col_num)
        string += "-"

        for i in range(len(rand_row)):
            if rand_row[i][0] == rand_col[i][0] and rand_row[i][1] == rand_col[i][1]:
                string += str(random.randint(0 , 9))
            elif rand_row[i][0] == rand_col[i][0]:
                string += primary[i][1] + secondary[i][1]

        return string



def decrypt(inptext , enc_text):
    text = ""
    helper = []
    list = ["0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]

    for i in range(len(inptext)):
        helper.append(inptext[i])

    for i in range(len(helper)):
        if helper[i] == " ":
            text += "#"
        else:
            text += helper[i]


    res_enc = ""

    if enc_text[0] == "&":
        res_enc = encrypt(text , "crossed" , [])
        if len(res_enc) == len(enc_text):
            for i in range(len(enc_text)):
                if (res_enc[i] != enc_text[i]) and (res_enc[i] not in list):
                    return False
                elif res_enc[i] != enc_text[i] and (res_enc[i] in list):
                    pass

            return True

        else:
            return False


    else:
        
        splits = enc_text.split("-")
        col_index = int(splits[1])
        row_index = int(splits[0])
        word_matrix = []
        cols = []
        primary = []
        secondary = []

        for i in range(len(text)):
            row = []
            for j in range(len(text)):
                row.append(text[i] + text[j])

            word_matrix.append(row)

        
        for i in range(len(word_matrix)):
            primary.append(word_matrix[i][i])

        for i in range(len(word_matrix)):
            secondary.append(word_matrix[i][len(word_matrix)- 1 - i])

        

        for i in range(len(word_matrix)):
            row = []
            for j in range(len(word_matrix[0])):
                row.append(word_matrix[j][i])

            cols.append(row)
            

        res_enc = encrypt(text , "random" , [row_index , col_index])


        if (len(res_enc) == len(enc_text)):
            for i in range(len(enc_text)):
                if (res_enc[i] != enc_text[i]) and (res_enc[i] not in list):
                    return False
                elif res_enc[i] != enc_text[i] and (res_enc[i] in list):
                    pass

            return True
        else:
            return False
                



act_text = "Eminem is the gratest male artist in the world"
itext = encrypt(act_text , "random" , [])
# print("Actual Text:" , act_text)
# print("Encrypted Text:" , itext)
res = decrypt(act_text  , "8-27-sts#sg")
print("Deyrcption result:" , res)