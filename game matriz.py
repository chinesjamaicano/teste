matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite um local para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

    jogador1=9
tiro=int(input())
if tiro == 9:
    print("Head Shot, you win")
else:
    print("pinou, you lose")

jogador2=2
tiro=int(input())
if tiro == 2:
    print("Head Shot, you win")
else:
    print("pinou, you lose")
