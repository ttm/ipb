import networkx as x, pylab as p

with open('../data/first.txt', 'r') as f:
    ppl = f.read().split('\n')[:-1]

nodes = {
    'teachers': [],
    'who': '',
    'students': []
}

for p in ppl:
    p_ = p.split(' ')
    quality = int(p_[0])
    name = ' '.join(p_[1:])
    if quality > 0:
        nodes['teachers'].append(name)
    elif quality == 0:
        nodes['who'] = name
    else:
        nodes['students'].append(name)

g = x.DiGraph()

for t in nodes['teachers']:
    g.add_edge(t, nodes['who'])

for s in nodes['students']:
    g.add_edge(nodes['who'], s)

x.draw_networkx(g)
p.show()
