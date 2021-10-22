import Question
from Question_Class import Question_Class


# We are building questions to answers
questionsandAnswers = [Question_Class(Question.questionsList[0], "a"),
                        Question_Class(Question.questionsList[1], "b"),
                        Question_Class(Question.questionsList[2], "b")
                       ]

# print(questionsandAnswers[0])

def take_test(questionsandAnswers):
    score = 0
    for question in questionsandAnswers:
        answer = input(question.questionActual)
        if(answer == question.response):
            score += 1

    print("Total score is "+str(score)+"/3")

take_test(questionsandAnswers)
