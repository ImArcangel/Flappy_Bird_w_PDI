archivo = open('tablero.txt', 'r+')
players = ['NA', 'NA', 'NA']
i = 0
for line in archivo.readlines():
    players[i] = line
    i += 1
    print(line)
print(players)

players = ['A', 'B', 'C']
print(players)

for i in players:
    archivo.write(str(players))