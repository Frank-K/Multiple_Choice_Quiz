# Name: Frank Karunaratna
# Date: 16 July 2015
# File Name: Assignment3.py
# Description: This program allows the user to do a 10 question multiple choice
#              quiz. The quiz is preloaded with 20 questions, and the user can
#              choose to add or delete questions.

import time

def main_menu():
    '''Displays the main menu of the program'''

    time.sleep(1)
    
    print ("")
    print ("-"*11)
    print (" Main Menu")
    print ("-"*11)
    print ("")
    print ("(1) Play")
    print ("(2) Create")
    print ("(3) Exit")
    print ("")

    #Allows the user to choose what they want to do
    input_type = 3
    user = user_input(input_type)

    

    #Displays the correct menu depending on what the user chose
    if user == 1:
        play()
        
    elif user == 2:
        create()
        
    elif user == 3:
        return


def user_input (input_type):
    '''Returns the error checked user input'''

    #Error checks the user input
    if input_type == 3:
        while True:
            try:
                user = int(input("Enter your choice: "))

                if user >= 1 and user <=3:
                    return user
                
                else:
                    print ("You must enter a number between 1 and 3")
                    print ("")
                    
            except:
                print ("You must enter a number between 1 and 3")
                print ("")
                
    elif input_type == 2:
        while True:
            try:
                user = int(input ("Enter your choice: "))

                if user >= 1 and user <=2:
                    return user
                
                else:
                    print ("You must enter a 1 or 2")
                    print ("")
                    
            except:
                print ("You must enter a 1 or 2")
                print ("")

    elif input_type == 4:
        while True:                
            user_answer = input ("Enter your answer: ")

            if user_answer.upper() in ("ABCD"):
                return user_answer.upper()
            
            else:
                print ("Your options are A/B/C/D")
                print ("")


def play():
    '''Displays the play menu'''

    time.sleep(1)
    
    print ("")
    print ("-"*11)
    print (" Play Menu")
    print ("-"*11)
    print("")
    print ("(1) Start a new quiz")
    print ("(2) Back to main menu")
    print("")

    #Allows the user to choose what they want to do
    input_type = 2
    user2 = user_input(input_type)
    print ("")

    #Displays the correct menu depending on what the user chose
    if user2 == 1:
        do_quiz()
        
    elif user2 == 2:
        main_menu()


def do_quiz():
    '''Cycles through the quiz'''
    
    print("Please wait while your quiz is being generated...")
    print ("")
    
    time.sleep(2)
    
    import random
    correct_count = 0

    #Reads the file and creates a list of the questions
    infile = open("questions.txt", "r")
    questions = infile.readlines()
    infile.close()

    proper_questions = []

    #Gets rid of any lines that are blank
    for question in questions:
        if question != "\n":
            proper_questions.append(question)    
    
    random.shuffle(proper_questions)

    #Loops through 10 questions
    for num in range(10):
        
        questions_parts = proper_questions[num].split("\t")

        #Prints the question
        print (str(num+1) + ") " + questions_parts[0] )
        
        for x in range(1,5):
            print ("    " + questions_parts[x])
            
        print ("")
        answer = questions_parts[5]

        #Allows the user to input their answer
        input_type = 4
        user_answer = user_input(input_type)

        #Checks if the user entered the correct answer    
        if user_answer == answer[0]: #answer[0] removes the \n from the end
            correct_count += 1
            print("You guessed right!")
            print("")
            
        else:
            print("Sorry, the correct answer is " + answer)

        time.sleep(0.5)
            
    #Calculates and prints the users score
    percentage = (correct_count / 10 *100)
    print ("")
    print("You scored: " + str(percentage) + " %!")

    time.sleep(0.5)

    play()
        
    
def create():
    '''Displays the create menu'''

    time.sleep(1)
    
    print ("")
    print ("-"*13)
    print (" Create Menu")
    print ("-"*13)
    print ("")
    print ("(1) Add questions")
    print ("(2) Delete questions")
    print ("(3) Back to main menu")
    print ("")

    #Allows the user to choose what they want to do
    input_type = 3
    user3 = user_input(input_type)

    #Displays the correct menu depending on what the user chose
    if user3 == 1:
        add_question()
        
    elif user3 == 2:
        delete_question()
        
    elif user3 == 3:
        main_menu()
        

def add_question():
    '''Adds a question to the question file'''

    time.sleep(1)

    #Allows the user to enter their question
    print ("")
    new_question = input("Enter the question you want to add: ")
    answer1 = input ("Answer (A) ")
    answer2 = input ("Answer (B) ")
    answer3 = input ("Answer (C) ")
    answer4 = input ("Answer (D) ")
    print ("")
    print ("The correct answer is...")

    #Forces the user to choose a correct answer
    input_type = 4
    real_answer = user_input(input_type)

    #Confirms that the user wants to add the question
    print ("")
    check = input ("Are you sure you want to add this question? (y/n) ")
    print ("")

    if check.lower() == "y":
        print ("Congratulation your question was added!")

        #Combines the parts of the questions
        a = "\n"+new_question+"\t(A) "
        b = answer1+ ""+"\t(B) "
        c = answer2+"\t(C) "
        d = answer3+"\t(D) "
        e = answer4+"\t"+(real_answer).upper()
        question = (a+b+c+d+e)

        #Writes the new question to the file
        outfile = open("questions.txt",'a')
        outfile.write(question)
        outfile.close()
        
        
    else:
        print ("Your question was NOT added")
        
    create()


def delete_question():
    '''Deletes a question from the question file'''

    time.sleep(1)
    
    print ("")
    print("Enter a keyword to search for a question.")
    print("The first instace of the keyword will be found and",end = "")
    print(" the first question containingthe keyword will be displayed.")
    print ("")
    keyword = input("Keyword: ")
    print ("")

    #Creates a list of the questions
    infile = open("questions.txt",'r')
    all_questions = infile.readlines()
    infile.close()
    
    count = 0
    found_keyword = False

    #Loops through the questions and searches for the keyword
    for questions in all_questions:
        if questions.lower().find(keyword.lower()) != -1:
            
            found_keyword = True
            
            words = questions.split("\t")
            
            print ("Question found:",words[0])
            
            break
        
        count = count + 1
        
    if found_keyword == False:
        print ("Your keyword was not found")
        create()
        
    else:
        #Confirms that the user wants to delete the question
        confirm = input("Are you sure you want to delete this question? (y/n) ")
        print ("")

        if confirm == "y":
            print ("Your question was deleted")
            
            outfile = open("questions.txt",'w')
            
            del(all_questions[count])
            
            for question in all_questions:
                outfile.write(question)
                
            outfile.close()

        else:
            print ("")
            print ("You question was NOT deleted")

    create()

    
def main():
    '''Displays title and calls the main menu'''
    
    print (("-"*24).center(80))
    print ("THE GREAT BRAIN QUIZ".center(80))
    print (("-"*24).center(80))
    main_menu()
    print ("")
    print ("THANKS FOR PLAYING")

main()
