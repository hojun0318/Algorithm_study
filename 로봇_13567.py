M, n = map(int, input().split())

direct = 'east'
org_x, org_y, x, y = M - 1, 0, 0, 0

for _ in range(n):
    act, value = map(str, input().split())

    if act == 'TURN' and value == '0':
        if direct == 'east':
            direct = 'north'
        elif direct == 'north':
            direct = 'west'
        elif direct == 'west':
            direct = 'south'
        elif direct == 'south':
            direct = 'east'
    if act == 'TURN' and value == '1':
        if direct == 'east':
            direct = 'south'
        elif direct == 'south':
            direct = 'west'
        elif direct == 'west':
            direct = 'north'
        elif direct == 'north':
            direct = 'east'
    
    if act == 'MOVE':
        if direct == 'east':
            org_y += int(value)
        elif direct == 'west':
            org_y -= int(value)
        elif direct == 'south':
            org_x += int(value)
        elif direct == 'north':
            org_x -= int(value)

    if org_x < 0 or org_x >= M or org_y < 0 or org_y >= M:
        print(-1)
        exit(0)        

if 0 <= org_x < M and 0 <= org_y < M :
    x = org_y
    y = M - org_x - 1
    print(x, y)
else:
    print(-1)