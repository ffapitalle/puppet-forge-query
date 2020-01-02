# puppet-forge-query

Puppet's Forge query command line tool

## Command line

puppet-forge-query comes with a command line interface. See help for more information:

See `puppet_forge_query --help`

## Install

Install the debian package using:

    apt-get install puppet_forge_query

## Development

From the root of the application directory, create a python environment,
install the application in development mode along with its dependencies and
run it locally:

    virtualenv env
    . env/bin/activate
    pip install --upgrade pip
    pip install -e . -r requirements.txt -r dev-requirements.txt

Tests can be run using *tox* (recommended):

    pip install tox
    tox

Or directly by calling *py.test*:

    python -m pytest
