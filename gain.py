"""
Usage:
    gain.py <file> (--all | --targets <targets>) (--parent <parent>) [-o <results> | --output <results>]
    gain.py -h | --help

Options:
    -h --help  Show this screen.
"""

from __future__ import division
from collections import Counter
from docopt import docopt
import math
import pandas


def entropy(l):
    p = Counter(l)
    total = float(len(l))
    return -sum(count/total * math.log(count/total, 2) for count in p.values())

def entropy_of_q(df, target, against):
    total = df.count().values[0]
    grouped = df.groupby([target])
    e = 0.0
    for name, g in grouped:
        g_total = g.count().values[0]
        p = Counter(g[against].tolist())
        r = [(-x/g_total * math.log(x/g_total, 2)) for x in p.values()]
        e += g_total/total * sum(r)
    return e

def main(args):
    # Read CSV into DataFrame, get Decision attribute
    df = pandas.read_csv(args['<file>'])
    parent = args['<parent>']
    # Get target columns to compare against
    if args['--all']:
        targets = df._get_numeric_data().columns.difference([args['<parent>']]).tolist()
    elif args['--targets']:
        targets = args['<targets>'].split(',')
    # Calculate Decision (parent) entropy
    parent_entropy = entropy(df[parent])
    # For each target column calculate the gain
    gain = dict()
    for t in targets:
        e_t = entropy_of_q(df, t, parent)
        gain[t] = parent_entropy - e_t
    # If output file specified, save results as CSV
    if args['-o'] or args['--output']:
        filename = args['<results>']
        odf = pandas.DataFrame([gain.values()], columns=gain.keys())
        odf.to_csv(filename, index=False)
    else:
        # Else just print to stdout
        print 'Parent ({}):\t{}'.format(parent, parent_entropy)
        print '\nGains:'
        for n, v in sorted(gain.items()):
            print n, '\t', v


if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)
