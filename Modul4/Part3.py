print(*map('%2d x %2d = %3d'.__mod__, ((k, i, i * k)
for k in range(*map(int.__add__, (0, 1), map(int, input().split())))
for i in range(1, 11))), sep='\n')