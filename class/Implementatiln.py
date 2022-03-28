for i in range(4): 
    for j in range(5): 
        print(f'({i}, {j})', end=' ')
    print()


def move_plans(n, plans):
    x, y = 1, 1
    moves = {
        'L': (0, -1),
        'R': (0, 1),
        'U': (-1, 0),
        'D': (1, 0)
    }
    plans = plans.split()
    for plan in plans:
        if plan in moves:
            t1 = moves[plan]
            nx = x + t1[0]
            ny = y + t1[1]
        if (nx<1) or (nx>n) or (ny<1) or (ny>n): 
            continue 
        
        x, y = nx, ny
        
    return f'({x}, {y})'

print(move_plans(5, 'D D L R U U U'))
print(move_plans(5, 'R R R U D D'))
