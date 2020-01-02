from __future__ import print_function

import argparse
import pkg_resources


def get_version():
    return '%(prog)s ' + \
        pkg_resources.get_distribution('puppet_forge_query').version


def main():
    parser = argparse.ArgumentParser(
        description='Puppet's Forge query command line tool'
    )
    parser.add_argument('--version', action='version', version=get_version())
    args = parser.parse_args()
    print(args)
