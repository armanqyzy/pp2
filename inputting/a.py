# Sequence Types: list, tuple, range
listt = input().split()
tuplee = tuple(input().split())
rangee = range(int(input()), int(input()), int(input()))

print(listt)
print(tuplee)
print(list(rangee))  # Convert range to a list for display

# Mapping Type: dict
inputting = {}

while True:
    keyy = input("Enter an 'exit' to stop")
    if keyy=='exit':
        break
    
    valuee = input()
    inputting[keyy] = valuee

print(inputting)


# Set Types: set, frozenset
sett = set(input().split())
frozensett = frozenset(input().split())
print(sett)
print(frozensett)

# Boolean Type: bool
booll = bool(input())
print(booll)

# Binary Types: bytes, bytearray, memoryview
bytess = bytes(input(), 'utf-8')
bytearrayy = bytearray(input(), 'utf-8')
memview = memoryview(bytess)
print(bytess)
print(bytearrayy)
print(memview)

# None Type: NoneType
nonetypee = None
print(nonetypee)

