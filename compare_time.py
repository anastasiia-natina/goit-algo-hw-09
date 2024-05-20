import time
import matplotlib as plt
from find_coins_greedy import find_coins_greedy
from find_min_coin import find_min_coins

def test_greedy_time(amount):
    start_time = time.time()
    find_coins_greedy(amount)
    end_time = time.time()
    return end_time - start_time

amounts = range(1, 1001)
greedy_times = [test_greedy_time(amount) for amount in amounts]

def test_dp_time(amount):
    start_time = time.time()
    find_min_coins(amount)
    end_time = time.time()
    return end_time - start_time

amounts = range(1, 1001)
dp_times = [test_dp_time(amount) for amount in amounts]

plt.plot(amounts, greedy_times, label='Жадібний алгоритм')
plt.plot(amounts, dp_times, label='Алгоритм динамічного програмування')
plt.xlabel('Сума')
plt.ylabel('Час виконання (с)')
plt.title('Порівняння часу виконання алгоритмів')
plt.legend()
plt.show()