import random
count = 0
streak_count = []
streaks = []
amount = 100
for i in range(amount):
    count += 1
    coin = random.randint(0, 1)
    if coin == 0:
        streaks.append("H")
    elif coin == 1:
        streaks.append("T")
    if len(streaks) > 1:
        if streaks[-1] != streaks[0]:
            streaks = [streaks[-1]]
    if len(streaks) == 6:
        streak_count.append(1)
streak_length = len(streak_count)
decimal_value = len(streak_count) / amount
result = f"There is a 6 same face flip streak {decimal_value * 100}% of the time."

print(streak_count)
print(result)
