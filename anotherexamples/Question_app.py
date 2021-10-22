import Question

score = 0
for question in Question.questionsList:
    print(question)
    answerInput = input("Enter your answer - ")
    if(question.__contains__("Apple") and answerInput == 'a'):
        score = score + 1
    if (question.__contains__("Banana") and answerInput == 'b'):
        score = score + 1
    if (question.__contains__("Apple") and answerInput == 'b'):
        score = score + 1

print("Total score is "+str(score)+"/3")

