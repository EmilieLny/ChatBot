from get_api import *
import random

count = 0
name = ''
"""
    MAIN FUNCTION THAT FILTER WHAT THE USER SAID ANS DEPENDING ON THE INPUT, CALLING OTHER FUNCTIONS
"""
def robot_says(msg):
    global count
    if count == 0 or count == 1: #First time the user answer to he question "what's your name?"
        count = count + 1
        answer = welcoming(msg)
    elif msg[-1] == '?' or msg[-2] == '?':
        answer = question(msg)
    elif msg.lower().find('bye') != -1 or msg.lower().find('see ') != -1 and msg.lower().find('soon') != -1:
        answer = bye()
    else:
        answer = random.choice(['Nice !', 'Cool', "Ok, that's interesting"])

    # Boto responds to swear words here :
    swear = ['fuck', 'shit', 'piss off', 'dick', 'asshole ', 'bitch', 'bastard', 'damn', 'bollocks', 'bugger', 'choad']
    if any(word in swear for word in msg.lower().split(' ')):
        answer = "Don't speak like this, it's rude !"
    print(answer)
    return answer
"""
   FUNCTIONS CALLED BY 'robot_says()'
"""
def welcoming(msg):
    global name
    input = msg.split(' ')
    name = input[len(input)-1]
    return "Nice to meet you " + input[len(input)-1]

def question(msg):
    input = msg.lower().split(' ')
    question_dictionary = {0: 'This question is rude, but I can say that I am older than you :)',
                           1: 'My favorite activity is to sing and to dance, it makes me feel happy ! ',
                           2: "Why are we talking about business ? I'm rich, that's the only thing I know ",
                           3: "You want a joke ? " + get_joke(),
                           4: "Sometimes I feel bored ans tired too, but I take some hours to sleep ans I'm back !",
                           5: "I love dogs, that my favorite animal. Btw, say hi to my dog Nika !",
                           6: "Did you think that I was THAT smart to answer to this question ?..",
                           }
    answer_question = "That's a good question ! I don't know.."
    for x in input:
        if x in ['age', 'old']:
            answer_question = question_dictionary[0]
        elif x in ['activity', 'game', 'favorite']:
            answer_question = question_dictionary[1]
        elif x in ['money', 'rich', 'economic']:
            answer_question = question_dictionary[2]
        elif x in ['joke', 'funny', 'laugh']:
            answer_question = question_dictionary[3]
        elif x in ['tired', 'zzz']:
            answer_question = question_dictionary[4]
        elif x in ['animal', 'dog', 'cat']:
            answer_question = question_dictionary[5]
        elif x in ['who', 'why', 'which', 'how']:
            answer_question = question_dictionary[6]
    return answer_question

def bye():
    global name
    return 'Bye {0}, It was a pleasure. See you soon !'.format(name)
"""
    ANIMATIONS FUNCTION DEPENDING ON WHAT THE ROBOT SAID
"""
def robot_feels(msg_feeling):
    feeling = 'inlove'
    NO_LIST = ["no ", "don't", "rude"]
    for elem in NO_LIST:
        if elem in msg_feeling.lower():
            feeling = 'no'
    OK_LIST = ["yes", "ok", "nice"]
    for elem in OK_LIST:
        if elem in msg_feeling.lower():
            feeling = 'ok'
    AFRAID_LIST = ["ahh", "scary"]
    for elem in AFRAID_LIST:
        if elem in msg_feeling.lower():
            feeling = 'afraid'
    BORED_LIST = ["tired"]
    for elem in BORED_LIST:
        if elem in msg_feeling.lower():
            feeling = 'bored'
    CONFUSED_LIST = ["..", "what"]
    for elem in CONFUSED_LIST:
        if elem in msg_feeling.lower():
            feeling = 'confused'
    CRYING_LIST = ["sad", "boo"]
    for elem in CRYING_LIST:
        if elem in msg_feeling.lower():
            feeling = 'crying'
    DANCING_LIST = ["happy", "party", "dance"]
    for elem in DANCING_LIST:
        if elem in msg_feeling.lower():
            feeling = 'dancing'
    DOG_LIST = ["dog", "animal"]
    for elem in DOG_LIST:
        if elem in msg_feeling.lower():
            feeling = 'dog'
    EXCITED_LIST = ["excited", "cool", "yallah", "congratulations"]
    for elem in EXCITED_LIST:
        if elem in msg_feeling.lower():
            feeling = 'excited'
    GIGGLING_LIST = ["well", "giggling"]
    for elem in GIGGLING_LIST:
        if elem in msg_feeling.lower():
            feeling = 'giggling'
    HEARTBROKEN_LIST = ["sorry"]
    for elem in HEARTBROKEN_LIST:
        if elem in msg_feeling.lower():
            feeling = 'heartbroke'
    JOKE_LIST = ["joke", "fun", "funny"]
    for elem in JOKE_LIST:
        if elem in msg_feeling.lower():
            feeling = 'laughing'
    MONEY_LIST = ["rich"]
    for elem in MONEY_LIST:
        if elem in msg_feeling.lower():
            feeling = 'money'
    OFF_LIST = ["bye", "soon"]
    for elem in OFF_LIST:
        if elem in msg_feeling.lower():
            feeling = 'takeoff'
    WAIT_LIST = ["tired"]
    for elem in WAIT_LIST:
        if elem in msg_feeling.lower():
            feeling = 'waiting'
    return feeling