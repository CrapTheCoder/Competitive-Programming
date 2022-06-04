for _ in range(int(input())):
    lie = truth = 0

    for __ in range(int(input())):
        question = input()
        answer = input()

        if sum(question.count(i) for i in 'aeiou') == sum(answer.count(i) for i in 'aeiou'):
            truth += 1
        else:
            lie += 1

    print('jane' if truth >= lie else 'secretbff')