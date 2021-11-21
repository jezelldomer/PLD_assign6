#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation

import random

print (f"\033[1;36;40mGood day! There will be an \033[1;37;40m Addition Quiz \033[1;36;40mtoday. ")
name = input("\033[1;35;40m  Please enter your name: ")
print (f"\033[1;30;40m This is your 10 Item Quiz,\033[1;33;40m {name}.\033[1;30;40m Good Luck! ")

def addition():
    score = 0
    range1_1 = random.randint(0,99)
    range1_2 = random.randint(0,99)
    print ("\033[1;37;40m[ Item No. 1 ]")
    print (f"\033[1;33;40m1. What is {range1_1} + {range1_2}? ")
    user_ans_1 = int(input("\033[1;35;40mAnswer here: "))
    prog_ans_1 = range1_1 + range1_2
    if prog_ans_1 == user_ans_1:
        print ("\033[1;32;40mYour Answer Is Correct! ")
    elif prog_ans_1 != user_ans_1:
        print (f"\033[1;37;40mYour Answer is  \033[1;31;40mWrong. \033[1;37;40mThe answer should be \033[1;31;40m{prog_ans_1}. ")
    range2_1 = random.randint(0,99)
    range2_2 = random.randint(0,99)
    print ("\033[1;37;40m[ Item No. 2 ]")
    print (f"\033[1;33;40m2. What is {range2_1} + {range2_2}? ")
    user_ans_2 = int(input("\033[1;35;40mAnswer here: "))
    prog_ans_2 = range2_1 + range2_2
    if prog_ans_2 == user_ans_2:
        print ("\033[1;32;40mYour Answer Is Correct! ")
    elif prog_ans_2 != user_ans_2:
        print (f"\033[1;37;40mYour Answer is  \033[1;31;40mWrong. \033[1;37;40mThe answer should be \033[1;31;40m{prog_ans_2}. ")
    range3_1 = random.randint(0,99)
    range3_2 = random.randint(0,99)
    print ("\033[1;37;40m[ Item No. 3 ]")
    print (f"\033[1;33;40m3. What is {range3_1} + {range3_2}? ")
    user_ans_3 = int(input("\033[1;35;40mAnswer here: "))
    prog_ans_3 = range3_1 + range3_2
    if prog_ans_3 == user_ans_3:
        print ("\033[1;32;40mYour Answer Is Correct! ")
    elif prog_ans_3 != user_ans_3:
        print (f"\033[1;37;40mYour Answer is  \033[1;31;40mWrong. \033[1;37;40mThe answer should be \033[1;31;40m{prog_ans_3}. ")

addition()
