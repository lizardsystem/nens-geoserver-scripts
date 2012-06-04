from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='nens-geoserver-scripts',
      version=version,
      description="Python scripts for Geoserver administration (copying from one server to another)",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='geoserver',
      author='Remco Gerlich',
      author_email='remco.gerlich@nelen-schuurmans.nl',
      url='http://www.nelen-schuurmans.nl',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
