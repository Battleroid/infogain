from __future__ import division
from docopt import docopt
from collections import Counter
import pandas
import math


__doc__ = """
Usage:
    gain.py <file>
"""


def entropy(l):
    """Calculate 'parent' entropy."""
    p = Counter(l)
    total = float(len(l))
    return -sum(count/total * math.log(count/total, 2) for count in p.values())

def entropy_column(col, c):
    pass

def main(args):
    # import data
    data = pandas.read_csv(args['<file>'])
    print data
    # get class attribute entropy
    class_entropy = entropy(data['class'].tolist())
    print class_entropy
    # groupby decision attribute (in the future will use ALL columns as a decision attribute)
    decision_entropy = 0
    for name, g in data.groupby(['age']):
        print 'Group', name
        g_total = g.count().values[0]
        p = Counter(g['class'].tolist())
        r = []
        for v in p.values():
            r.append(-v/g_total * math.log(v/g_total, 2))
        print g_total, 'over', data.count().values[0], g_total/data.count().values[0] * sum(r)
        decision_entropy += g_total/data.count().values[0] * sum(r)
    print 'Column age:', decision_entropy
    print 'Gain of age:', class_entropy - decision_entropy


if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)
