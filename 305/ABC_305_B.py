coordinates = [0, 3, 4, 8, 9, 14, 23]

p, q = map(str, input().split())

p_coords = ord(p) - 65
q_coords = ord(q) - 65

print(abs(coordinates[p_coords] - coordinates[q_coords]))
