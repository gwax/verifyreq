"""Script to verify installed packages match pip requirement files."""

import argparse
import pkg_resources


def get_args(args=None):
    parser = argparse.ArgumentParser(
        description='Package installation verifier')
    parser.add_argument(
        'requirement', help='pip requirement file to verify against',
        type=argparse.FileType('rt'))
    return parser.parse_args(args=args)


def main():
    """Get args and run verifier."""
    args = get_args()
    reqs = args.requirement.readlines()
    reqs = list(reqs)
    for l in reqs:
        print(l)
    pkg_resources.require(reqs)
