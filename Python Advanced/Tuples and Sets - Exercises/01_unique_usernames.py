n = int(input())

unique_users = {input() for x in range(n)}

[print(user) for user in unique_users]
