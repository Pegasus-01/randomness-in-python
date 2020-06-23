import random

#basic examples of randomness


print(random.choice(range(100)))
print(random.choice([1, 2, 3, 4, 5, 6]))
print(random.choice("RudranilMaity"))


print(random.randrange(1, 100, 2))


print(random.random())


random.seed(10) #use seed to get exact same number in randomness
print(random.random())



list_numbers = [12, 22, 32, 42, 52]

random.shuffle(list_numbers)

print(list_numbers)