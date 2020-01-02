import io
import re
from setuptools import setup, find_packages


def get_version_from_changelog():
    try:
        with io.open('debian/changelog', encoding='utf8') as stream:
            return re.search(r'\((.+)\)', next(stream)).group(1)
    except IOError:
        print('No debian/changelog file found, using: 0.0.1 as version')
        return '0.0.1'


setup(
    name='puppet_forge_query',
    description='Puppet's Forge query command line tool',
    long_description=io.open('README.md').read(),
    long_description_content_type='text/markdown',
    version=get_version_from_changelog(),
    include_package_data=True,
    author='Federico Fapitalle',
    author_email='federico.fapitalle@avature.net',
    url='https://gitlab.xcade.net/federico.fapitalle/puppet_forge_query',
    install_requires=io.open('requirements.txt').read().splitlines(),
    license='Propietary',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'puppet_forge_query = puppet_forge_query.cli:main',
        ]
    },
    classifiers=(
        'Private :: Do not Upload',  # Prevents uploading to pypi
    ),
)
