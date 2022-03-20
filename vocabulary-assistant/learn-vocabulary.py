import random

#=================================================================================
def get_words(file_name):
    word_list = []
    
    with open(file_name,'r',encoding="utf-8") as file:
        for line in file:
            for word in line.split("/\/n"):
                word_list.append(word.strip())  # get over \n

    return word_list
#=================================================================================
def get_key(val, my_dict):  # function to return key for any value
    for key, value in my_dict.items():
         if val == value:
             return key
    return "key doesn't exist"
#=================================================================================

false_words = []
meaning = {}
count = 0
correct_ans = 0
false_ans = 0

in_english = get_words("english.txt")
in_greek = get_words("greek.txt") 

if not(len(in_greek) == len(in_english)):
    raise Exception("Same amount of English and Greek words is needed.")

while count < len(in_english):  # fill the dictionary
    meaning[in_english[count]] = in_greek[count]
    count+=1
count = 0

tested_words = []
flag = 0
while count != len(in_english):
    rand_num = random.randint(0, len(in_english)-1)
    if not tested_words: 
        tested_words.append(rand_num)
    else:
        for i in tested_words:
            if i == rand_num:
                flag = 1
                break
    if flag == 1:
        flag = 0
        continue
    else:
        print("Ποια ειναι η σημασία της λέξης: ", get_key(in_greek[rand_num], meaning))

        val = input("Enter your value: ")
        if val == in_greek[rand_num]:
            correct_ans += 1
        else:
            false_ans += 1
            false_words.append(get_key(in_greek[rand_num], meaning))
            
        tested_words.append(rand_num)
        count += 1

print("\n\t      Your score was\n", "Correct answers:",correct_ans, "  Wrong answers:",false_ans,"\n")
print("You did the following mistakes: ",false_words, "\n")