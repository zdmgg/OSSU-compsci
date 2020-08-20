def computegrade(score):
    if (score >= 1.0 or score <= 0.0) :
        print('Bad score')
    elif (score <= 1.0 or score >= 0.0) :
        if score >= 0.9 :
            return 'A'
        elif score >= 0.8 :
            return 'B'
        elif score >= 0.7 :
            return 'C'
        elif score >= 0.6 :
            return 'D'
        else :
            return 'F'
    else:
        return 'Bad score'

try:
    score = input("Enter Score: ")
    score = float(score)
    grade = computegrade(score)
    print(grade)

except:
    print('Bad score')
