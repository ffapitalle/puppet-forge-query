from __future__ import print_function
from puppet_forge_query.forge import Forge
from puppet_forge_query.forgeresult import ForgeResult

import argparse
import pkg_resources


def get_version():
    return '%(prog)s ' + \
        pkg_resources.get_distribution('puppet_forge_query').version


def main():
    parser = argparse.ArgumentParser(
        description='Puppet\'s Forge query command line tool'
    )
    parser.add_argument('--version', action='version', version=get_version())

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-m', '--module', help='complete module name')
    group.add_argument('-s', '--search', help='search terms')

    parser.add_argument('--latest',
                        action='store_true',
                        help='print latest version of module')
    args = parser.parse_args()

    forge = Forge()
    if args.module:
        resp = forge.query_module(args.module)
        ForgeResult.module_description(resp, args.latest)

    if args.search:
        resp = forge.search_terms(args.search)
        ForgeResult.module_list(resp['results'], args.latest)
