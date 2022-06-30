def score(dice):
    sum = 0
    for roll in range(1,7):
        if dice.count(roll) > 2:
            if roll == 1:
                sum = 1000
            else:
                sum = 100*roll
            for i in range(3):
                del dice[dice.index(roll)]
            print(dice)
            break
    
    if 1 in dice:
        sum += 100*dice.count(1)
    if 5 in dice:
        sum += 50*dice.count(5)
    return sum
