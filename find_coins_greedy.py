def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    coin_count = {coin: 0 for coin in coins}
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            coin_count[coin] += 1
    
    return {coin: count for coin, count in coin_count.items() if count > 0}

print(find_coins_greedy(113))

