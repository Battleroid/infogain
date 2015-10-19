"""
Calculate the Gain of all (or a list) columns against a parent (decision)
column. Unless a output file is specified the results will be printed to stdout
in a basic table.

Input should be a properly formatted CSV file. If using multiple target columns
instead of --all flag be sure to use a comma delimited list (ex: age,income).

Usage:
    gain.py <file> (--all | --targets <targets>) (--parent <parent>) [--except <except>] [-o <results> | --output <results>] [-v | --verbose]
    gain.py -h | --help

Options:
    -h --help  Show this screen.
"""

from __future__ import division
from collections import Counter
from docopt import docopt
import math
import pandas
import sys


def entropy(l):
    """
    Calculate entropy of parent attribute.

    Args:
        l (List): List of integers or floats

    Returns:
        float
    """
    p = Counter(l)
    total = float(len(l))
    return -sum(count/total * math.log(count/total, 2) for count in p.values())


def entropy_of_q(df, target, against):
    """
    Calculate entropy of target column against decision attribute.

    Args:
        df (py:class:`pandas.DataFrame`): DataFrame of original data
        target (str): Column to calculate entropy for
        against (str): Decision attribute column

    Returns:
        float: Entropy of the given column given the decision attribute
    """
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
    verbose = args['-v'] or args['--verbose']
    if verbose:
        print 'Verbose on'
    # Read CSV into DataFrame, get Decision attribute
    df = pandas.read_csv(args['<file>'])
    parent = args['<parent>']
    # Get target columns to compare against
    if args['--all']:
        targets = df._get_numeric_data().columns.difference(
                [args['<parent>']]).tolist()
    elif args['--targets']:
        targets = args['<targets>'].split(',')
    if args['--except']:
        ignore = args['<except>'].split(',')
        targets = [x for x in targets if x not in ignore]
    if not targets:
        print 'No columns selected, exiting.'
        sys.exit(1)
    # Calculate Decision (parent) entropy
    parent_entropy = entropy(df[parent])
    if verbose:
        print 'Parent is', parent
        print 'Parent entropy is', parent_entropy
        print 'Target columns:', targets
    # For each target column calculate the gain
    gain = dict()
    for t in targets:
        e_t = entropy_of_q(df, t, parent)
        gain[t] = parent_entropy - e_t
        if verbose and (args['-o'] or args['--output']):
            print t, 'e:', e_t
    # If output file specified, save results as CSV
    if args['-o'] or args['--output']:
        filename = args['<results>']
        odf = pandas.DataFrame([gain.values()], columns=gain.keys())
        odf.to_csv(filename, index=False)
    else:
        # Else just print to stdout
        if verbose:
            print ''
        print 'Parent ({}):\t{}'.format(parent, parent_entropy)
        print 'Gains:'
        for n, v in sorted(gain.items()):
            print n, '\t', v


if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)
