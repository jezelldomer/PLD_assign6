#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation

import random

print (f"\033[1;36;40mGood day! There will be an \033[1;37;40m Addition Quiz \033[1;36;40mtoday. ")
name = input("\033[1;35;40m  Please enter your name: ")
print (f"\033[0;37;40mThis is your 10 Item Quiz,\033[1;33;40m {name}.\033[0;37;40m Good Luck! ")

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
    range4_1 = random.randint(0,99)
    range4_2 = random.randint(0,99)
    print ("\033[1;37;40m[ Item No. 4 ]")
    print (f"\033[1;33;40m4. What is {range4_1} + {range4_2}? ")
    user_ans_4 = int(input("\033[1;35;40mAnswer here: "))
    prog_ans_4 = range4_1 + range4_2
    if prog_ans_4 == user_ans_4:
        print ("\033[1;32;40mYour Answer Is Correct! ")
    elif prog_ans_4 != user_ans_4:
        print (f"\033[1;37;40mYour Answer is  \033[1;31;40mWrong. \033[1;37;40mThe answer should be \033[1;31;40m{prog_ans_4}. ")
    range5_1 = random.randint(0,99)
    range5_2 = random.randint(0,99)
    print ("\033[1;37;40m[ Item No. 5 ]")
    print (f"\033[1;33;40m5. What is {range5_1} + {range5_2}? ")
    user_ans_5 = int(input("\033[1;35;40mAnswer here: "))
    prog_ans_5 = range5_1 + range5_2
    if prog_ans_5 == user_ans_5:
        print ("\033[1;32;40mYour Answer Is Correct! ")
    elif prog_ans_5 != user_ans_5:
        print (f"\033[1;37;40mYour Answer is  \033[1;31;40mWrong. \033[1;37;40mThe answer should be \033[1;31;40m{prog_ans_5}. ")
    print ("\033[2;36;40mYou're Halfway there, you can do it! ")
    range6_1 = random.randint(0,99)
    range6_2 = random.randint(0,99)
    print ("\033[1;37;40m[ Item No. 6 ]")
    print (f"\033[1;33;40m6. What is {range6_1} + {range6_2}? ")
    user_ans_6 = int(input("\033[1;35;40mAnswer here: "))
    prog_ans_6 = range6_1 + range6_2
    if prog_ans_6 == user_ans_6:
        print ("\033[1;32;40mYour Answer Is Correct! ")
    elif prog_ans_6 != user_ans_6:
        print (f"\033[1;37;40mYour Answer is  \033[1;31;40mWrong. \033[1;37;40mThe answer should be \033[1;31;40m{prog_ans_6}. ")
    range7_1 = random.randint(0,99)
    range7_2 = random.randint(0,99)
    print ("\033[1;37;40m[ Item No. 7 ]")
    print (f"\033[1;33;40m7. What is {range7_1} + {range7_2}? ")
    user_ans_7 = int(input("\033[1;35;40mAnswer here: "))
    prog_ans_7 = range7_1 + range7_2
    if prog_ans_7 == user_ans_7:
        print ("\033[1;32;40mYour Answer Is Correct! ")
    elif prog_ans_7 != user_ans_7:
        print (f"\033[1;37;40mYour Answer is  \033[1;31;40mWrong. \033[1;37;40mThe answer should be \033[1;31;40m{prog_ans_7}. ")

addition()
