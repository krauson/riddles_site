# upload 266
import random

from flask import Flask, render_template, request

from models import database
from pwe_curd import (add_points, check_username_password, create_table,
                      create_user, get_users_scores)
from riddles import format_str, get_list_from_str, get_riddle

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/riddles')
def riddles():
    str1 = 'hello my name is hagai'
    former_correct_answer = request.args.get('correct_answer')
    msg = None
    if former_correct_answer is not None:
        former_possible_answers = request.args.get('possible_answers')
        former_possible_answers = get_list_from_str(former_possible_answers)
        for i in range(len(former_possible_answers)):
            former_possible_answers[i] = format_str(former_possible_answers[i])
        chosen_num = request.args.get('user_answer')
        chosen_num = int(chosen_num) - 1
        user_answer = former_possible_answers[chosen_num]
        if former_correct_answer == user_answer:
            username = request.args.get('username')
            add_points(username)
            msg = '{} was a correct answer! you earned 5 points:)'
            msg = msg.format(former_correct_answer)
        else:
            msg = 'Wrong answer.. the correct answer was: {}'
            msg = msg.format(former_correct_answer)

    riddle = get_riddle()
    question = riddle['question']
    question = format_str(question)
    username = request.args.get('username')
    possible_answers = riddle['incorrect_answers']
    possible_answers.append(riddle['correct_answer'])
    for i in range(len(possible_answers)):
        possible_answers[i] = format_str(possible_answers[i])

    correct_answer = riddle['correct_answer']
    correct_answer = format_str(correct_answer)

    random.shuffle(possible_answers)

    print(f'current correct answer: {correct_answer}')

    return render_template('riddles_page.html', msg=msg,
     possible_answers=possible_answers,
    correct_answer=correct_answer,
     question=question, username=username, str1=str1)


@app.route('/register', methods=['GET', 'POST'])
def register():
    create_table()
    print('username:')
    print(request.form.get('username'))
    username = request.form.get('username')
    password = request.form.get('password')
    if username is None:
        return render_template('register.html')
    else:
        is_added = create_user(username, password)
        print(f'the answer is {is_added}')
        if bool(is_added) is True:
            user_status = f'Welcome {username}, you are user number {is_added} in our website!'
        else:
            user_status = f'Error! The name {username} is already taken.'

        print(f'is valid :{is_added}')
        return render_template('register.html', username=username,
         user_status=user_status, is_added=is_added)


@app.before_request
def _db_connect():
    database.connect()


@app.teardown_request
def _db_close(_):
    if not database.is_closed():
        database.close()


@app.route('/login', methods=['GET', 'POST'])
def login():
    print('Im in login function')
    username = request.form.get('username')
    print(username)
    if username is None:
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if check_username_password(username, password):
            msg = 'welcome {}, so good to see you again:)'.format(username)
            is_valid = True
            return render_template('login.html', username=username,
             msg=msg, is_valid=is_valid)
        else:
            msg = 'Error! username or password incorrect'
            return render_template('login.html', msg=msg)


@app.route('/scores')
def show_score_table():
    print('showing scores table!')
    users = get_users_scores()
    username = request.args.get('username')
    return render_template('scores_table.html', users=users, username=username)


if __name__ == '__main__':
    app.run()
