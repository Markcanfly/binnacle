from argparse import ArgumentParser
from helm.chart import HelmChart
from helm.helmbin import Helm
from command.regression import regression

def cmd_regression(args):
    old = HelmChart(args.old_chart)
    new = HelmChart(args.new_chart)
    values = args.values
    diff_format = args.diff_format
    helm = Helm()
    regression(helm, old, new, values, diff_format)

def cmd_diff(args):
    pass

def main() -> int:
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(title='subcommands')
    parser.add_argument('-d', '--diff-format', dest='diff_format', default='json')
    
    parser_regression = subparsers.add_parser('regression')
    parser_regression.add_argument('old_chart')
    parser_regression.add_argument('new_chart')
    parser_regression.add_argument('--values', action='append')
    # parser_regression.add_argument('--ignore-random') # TODO
    parser_regression.set_defaults(func=cmd_regression)

    parser_diff = subparsers.add_parser('diff')
    parser_diff.add_argument('chart')
    parser_diff.add_argument('--values', action='append')
    parser_diff.set_defaults(func=cmd_diff)

    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        parser.error("too few arguments")

if __name__ == '__main__':
    main()
