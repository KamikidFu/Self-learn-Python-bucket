def rec_coin(money, coins):
    #Default value
    min_coins = money

    #Base case
    if money in coins:
        return 1
    #Recur case
    else:
        #For every coin value that is less or equal to money
        for i in [c for c in coins if c <= money]:
            num_coins = 1 + rec_coin(money-i, coins)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

key_string = int(input('Please input how many money to change coin:\n'))
key_coins_kind = input('Please input what kind of coin exists:\n').split(',')
key_coins = []
for i in range(len(key_coins_kind)):
    key_coins.append(int(key_coins_kind[i]))
print(rec_coin(key_string,key_coins))