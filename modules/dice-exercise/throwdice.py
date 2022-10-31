from dice import dice

def throw(n):
    return [dice() for _ in range(n)]
print(throw(2))

# 5 rolls: [2, 5, 3, 5, 4]
# 2 rolls: [2, 2]
