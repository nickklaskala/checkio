#!/usr/bin/env checkio --domain=py run number-guess

# .game-info-short {        margin-left: auto;        margin-right: auto;    }    .game-info td,    .game-info-short td {        padding: 8px 8px 8px 8px;        border-bottom: 1px dotted #8FC7ED;    }    .game-info td.tight,    .game-info-short td.tight {        padding: 0;        border-bottom: none;    }    .head-border {        border-bottom: 2px solid #8FC7ED !important;    }    .quote {        padding-left: 5%;        padding-right: 2%;        margin-bottom: 32px;    }    .quote-author {        float: right;        font-style: italic;        font-size: .9em;    }    .remark {        padding: 0;        font-size: .9em;    }...When you have eliminated all which is impossible, then whatever remains, however improbable, must be the    truth.
# Sir Arthur Conan Doyle -Sherlock        Holmes
# 
# You are given an unknown number within the range of 1 to 100, inclusive.    Your task is toguess what the number is by performing a series of guesses.
# 
# Your solution will need to guess the number by submitting aninteger divisorranging from 2 to 10,    and thenumber you guessed.    At each attempt you will get information as a list of tuples. Each tuple contains the remainder result along with    your previous divisor.
# 
# You should find the number within 8 guesses. We will give you a little extra info on your first attempt...Use    it wisely young grasshopper...
# 
# Consider the following example:
# AttemptDivisorGuessSubmitResponse1299(2,99)(1,5),(1,2)Remark #1:
# You try a divisor of 2            and try your luck with 99; however, you've got a response of a list of tuples, returning the remainder of            your previous divisor and your previous divisor. ( that means you still need to guess )
# 2391(3,91)(1,5),(1,2),(2,3)Remark #2:
# Your solution suggests            91 because it passed with the response data, isn't it? ( 91%5=1; 91%2=1 ) Again, you've still got a            response. Next guess, then.3641(6,41)(1,5),(1,2),(2,3),(5,6)Remark #3:
# Your solution suggests            41 because it passed with the response data. ( 41%5=1; 41%2=1; 41%3=2 ) Again, you've still got a response.4471(4,71)(1,5),(1,2),(2,3),(5,6),(3,4)Remark #4:
# Your solution suggests            71 because it passed with the response data. ( 71%5=1; 71%2=1; 71%3=2; 71%6=5 ) Again, you've still got a            response.5and, so on...678
# 
# You get the idea...
# 
# Input:Information about the previous attempt. A list of tuples. Each tuple contains its remainder    and the previous divisor.
# 
# Output:A list of integer divisors and your best guess. A list of two integers.
# 
# 
# Precondition:
# 0<number ≤ 100
# 
# 
# END_DESC

def checkio(attempts):
    return [2, 1]


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    MAX_ATTEMPT = 8

    def initial_referee(data):
        data["attempt_count"] = 0
        data["guess"] = 0
        return data

    def check_solution(func, goal, initial):
        prev_steps = [initial]
        for attempt in range(MAX_ATTEMPT):
            divisor, guess = func(prev_steps[:])
            if guess == goal:
                return True
            if divisor <= 1 or divisor > 10:
                print("You gave wrong divisor range.")
                return False
            if guess < 1 or guess > 100:
                print("You gave wrong guess number range.")
                return False
            prev_steps.append((goal % divisor, divisor))
        print("Too many attempts.")
        return False

    assert check_solution(checkio, 47, (2, 5)), "1st example"
    assert check_solution(checkio, 94, (3, 7)), "2nd example"
    assert check_solution(checkio, 52, (0, 2)), "3rd example"