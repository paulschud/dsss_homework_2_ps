import random


def random_number(min, max):
    """
    Random integer.
    """
    return random.randint(min, max) 


def random_operation():
    return random.choice(['+', '-', '*'])


def calculation(OperandOne, OperandTwo, Operation):
    Problem = f"{OperandOne} {Operation} {OperandTwo}"        #constructs the problem
    if Operation == '+': Answer = OperandOne + OperandTwo     #calcualtes sum
    elif Operation == '-': Answer = OperandOne - OperandTwo   #calculates difference
    else: Answer = OperandOne * OperandTwo                    #calculates product
    
    return Problem, Answer 

def math_quiz():
    UserScore = 0 #initialize score


    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(0,3): #loop with 3 runs
        OperandOne = random_number(1, 10) #get random numnber between 1 and 10
        OperandTwo = random_number(1, 5)  #get second random numnber between 1 and 5
        Operation = random_operation()   #get random operation: +, - or *

        Problem, Answer = calculation(OperandOne, OperandTwo, Operation) #calculate the math problem
        print(f"\nQuestion: {Problem}")                                #output question for user
        UserAnswer = int(input("Your answer: "))                       #retrieve input from user and convert to integer

        if UserAnswer == Answer:                                       #compare if user_answer is correct
            print("Correct! You earned a point.")                      
            UserScore += 1                                            #increment score by 1
        else:
            print(f"Wrong answer. The correct answer is {Answer}.")

    print(f"\nGame over! Your score is: {UserScore}" )              #print score

if __name__ == "__main__":
    math_quiz()
