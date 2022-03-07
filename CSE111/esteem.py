

def main():
    print('This program is an implementation of the Rosenberg')
    print('Self-Esteem Scale. This program will show you ten')
    print('statements that you could possibly apply to yourself.')
    print('Please rate how much you agree with each of the')
    print('statements by responding with one of these four letters:')
    print()
    print('D means you strongly disagree with the statement.')
    print('d means you disagree with the statement.')
    print('a means you agree with the statement.')
    print('A means you strongly agree with the statement.')
    total_score = 0
    questions = ['1. I feel that I am a person of worth, at least on an equal plane with others.','2. I feel that I have a number of good qualities','3. All in all, I am inclined to feel that I am a failure.','4. I am able to do things as well as most other people.','5. I feel I do not have much to be proud of.','6. I take a positive attitude toward myself.','7. On the whole, I am satisfied with myself.','8. I wish I could have more respect for myself.','9. I certainly feel useless at times.','10. At times I think I am no good at all.']
    for i in range(len(questions)):
        if i == 0 or i == 1 or i == 3 or i == 5 or i == 6:
            print(questions[i])
            answer = input('D, d, a, or A: ')
            while answer != 'D' and answer != 'd' and answer != 'a' and answer != 'A':
                print("I'm sorry, that is not a valid input.")
                answer = input('Please enter D, d, a, or A: ')
            total_score += int(positive_response(answer))
        else:
            print(questions[i])
            answer = input('D, d, a, or A: ')
            while answer != 'D' and answer != 'd' and answer != 'a' and answer != 'A':
                print("I'm sorry, {answer} is not a valid input.")
                answer = input('Please enter D, d, a, or A: ')
            total_score += int(negative_response(answer))
    print()
    print(f'Your total score is {total_score}.')
    print('A score below 15 may indicate problematic low self-esteem.')
    

def positive_response(answer):
    if answer == 'D':
        points = 0
    elif answer =='d':
        points = 1
    elif answer == 'a':
        points = 2
    elif answer == 'A':
        points = 3
    return points

def negative_response(answer):
    if answer == 'D':
        points = 3
    elif answer =='d':
        points = 2
    elif answer == 'a':
        points = 1
    elif answer == 'A':
        points = 0
    return points

main()