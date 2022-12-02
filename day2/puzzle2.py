with open('input1', 'r') as input_data:
    rounds = input_data.readlines()

for i in range(len(rounds)):
    current_round = rounds[i].strip().split()
    #if current_round[1] == 'X':
    #    current_round[1] = 'A'
    #elif current_round[1] == 'Y':
    #    current_round[1] = 'B'
    #else:
    #    current_round[1] = 'C'
    rounds[i] = current_round

scores = {'A': 1, 'B': 2, 'C': 3}
outcomes = {'W': 6, 'L': 0, 'D': 3}
wins = {'A': 'C', 'B': 'A', 'C': 'B'}
loses = {'A': 'B', 'B': 'C', 'C': 'A'}


total = 0
for i in rounds:
    score = 0
    if i[1] == 'Y': #i[0] == i[1]:
        #draw
        #score += scores[i[1]] + outcomes['D']
        score += scores[i[0]] + outcomes['D']
    else:
        #not a draw
        #score += scores[i[1]]
        if i[1] == 'Z': #i[0] == wins[i[1]]:
            #win
            score += outcomes['W'] + scores[loses[i[0]]]
        #    score += outcomes['W']
        elif i[1] == 'X': #i[0] == loses[i[1]]:
            #lose
            score += outcomes['L'] + scores[wins[i[0]]]
            #score += outcomes['L']
    total += score
print(total)
