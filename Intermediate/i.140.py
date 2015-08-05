vertices, en_pairs = map(int, raw_input().split())
matrix = [vertices * [0] for i in range(vertices)]

for i in range(en_pairs):
    left_nodes, right_nodes = [i.split() for i in raw_input().split('->')]
    for left_node in left_nodes:
        for right_node in right_nodes:
            matrix[int(left_node)][int(right_node)] = 1

print ""
for row in matrix:
    print ''.join(map(str, row))