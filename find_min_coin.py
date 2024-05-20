def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_used = [-1] * (amount + 1)
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                coin_used[x] = coin

    if min_coins[amount] == float('inf'):
        return {}

    coin_count = {coin: 0 for coin in coins}
    while amount > 0:
        coin = coin_used[amount]
        coin_count[coin] += 1
        amount -= coin
    
    return {coin: count for coin, count in coin_count.items() if count > 0}

print(find_min_coins(113))