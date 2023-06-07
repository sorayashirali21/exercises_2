#pr 2

file_path = 'email-Eu-core.txt'
N = 1005


def count_node_eadges(file_path):
    nodes = set()
    eadges = 0

    with open(file_path, 'r') as file:
        for line in file:
            sender, receiver = map(int, line.strip().split())
            nodes.add(sender)
            nodes.add(receiver)
            eadges += 1

    num_nodes = len(nodes)
    return num_nodes, eadges

num_nodes, num_eadges = count_node_eadges(file_path)
print('Result Question 2: ')
print('Number of eadges: ', num_eadges)

#======================================================
'output pr 2:'
'تعداد یال ها'