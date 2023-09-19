import random
import sys
import time
from pytimedinput import timedInput

class Quiz:
    def __init__(self, questions = []):
        self.questions = questions

    def __is_valid_input_choice(self, response):
        return (
            len(response) == 1 and
            response[0] >= 'a' and
            response[0] <= chr(ord('a') + len(self.questions[self.current_question]['choices']) - 1)
        )

    def start(self):
        self.current_question = 0
        self.points = 0
        random.shuffle(self.questions)

        while (self.current_question < len(self.questions)):
            random.shuffle(self.questions[self.current_question]['choices'])
            self.ask_quistion()
            response = self.get_response()
            
            if not self.__is_valid_input_choice(response):
                print('Oops: Ran out of time!')
            elif self.is_correct_response(response):
                print('Yaaay: Correct Answer!')
                self.points += 10
            else:
                print('Oops: Incorrect Answer!')

            self.current_question += 1
            time.sleep(2)
            print()

        print(f"Your Score: {self.calc_score():.2f}")
        
    def is_finished(self):
        return self.current_question == len(self.questions)

    def ask_quistion(self):
        if self.is_finished():
            print('Error: The quiz is finished')
        else:
            print(self.questions[self.current_question]['question'])
            for choiceId, choice in enumerate(self.questions[self.current_question]['choices'], start=ord('a')):
                print(f"{chr(choiceId)} ) {choice}")

    def get_response(self):
        print('Please Choose one of the options: ')
        response, timeout = timedInput('Enter the option ID: ', 10, False)
        if timeout:
            return response.lower()
 
        while not self.__is_valid_input_choice(response):
            response, timeout = timedInput('Please enter a valid ID, (for example b): ', 10, False)
            if timeout:
                return response.lower()

        return response.lower()

    def is_correct_response(self, response):
        response_idx = ord(response) - ord('a')
        return self.questions[self.current_question]['answer'] == self.questions[self.current_question]['choices'][response_idx]

    def calc_score(self):
        numOfQuestions = len(self.questions)
        try:
            return self.points / numOfQuestions
        except ZeroDivisionError:
            print('Error: There\'s no questions in the quiz')
            sys.exit(1)


def main():
    quiz = Quiz([
        {
            "question": "What's my name",
            "answer": "Osama",
            "choices": ['Osama', 'Anas', 'Lina', 'Ahmad']
        },
        {
            "question": "What is the capital of France?",
            "answer": "Paris",
            "choices": ['Paris', 'London', 'Berlin']
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "answer": "Mars",
            "choices": ['Mars', 'Venus', 'Jupiter']
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "answer": "William Shakespeare",
            "choices": ['William Shakespeare', 'Jane Austen', 'Charles Dickens']
        },
        {
            "question": "What is the largest mammal in the world?",
            "answer": "Blue Whale",
            "choices": ['Blue Whale', 'Elephant', 'Giraffe']
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "answer": "Carbon Dioxide",
            "choices": ['Carbon Dioxide', 'Oxygen', 'Nitrogen']
        }
    ])
    quiz.start()

main()