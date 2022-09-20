# todo, make a question and game class.
# todo, save results to file to simulate a database?

import os
import requests
import html
import random

def get_question():
    response = requests.get('https://opentdb.com/api.php?amount=1')
    response_json = response.json()
    question_data = response_json['results'][0]
    question = parse_question(question_data)
    return question 

def parse_question(question):
    data = {}
    data['category'] = question.get('category')
    data['type'] = question.get('type')
    data['difficulty'] = question.get('difficulty')
    data['question'] = html.unescape(question.get('question'))
    data['choices'] = []

    data['choices'].append(
        (1, question.get('correct_answer'))
    )
    for incorrect in question.get('incorrect_answers'):
        data['choices'].append((0, incorrect))
    random.shuffle(data['choices']) # shuffle, otherwise all answers are idx 0
    return data

def print_question(question):
    print(f"Category: {question.get('category')}")
    print(f"Type: {question.get('type')}")
    print(f"Difficulty: {question.get('difficulty')}")
    print(f"Question: {question.get('question')}")
    for count, choice in enumerate(question['choices']):
        print(f'{count} - {choice[1]}')

def run():
    """
    Runs the game
    """
    playing = True
    questions = 0
    correct = 0
    while playing:
        os.system('clear')
        print(f"Questions: {questions}  -- Correct {correct}")
        q = get_question()
        print_question(q)
        user_choice = int(input(f'Enter Choice > ').lower())
        questions += 1
        if q['choices'][user_choice][0] == 1:
            print("Correct!")
            print(f"Questions: {questions}  -- Correct {correct}")
            correct += 1
        else:
            print("Wrong!")
        keep_playing = input(f'Again? (Y or N) > ').lower()
        if keep_playing != 'y':
            playing = False
            print('Goodbye!')
        

if __name__ == "__main__":
    run()
