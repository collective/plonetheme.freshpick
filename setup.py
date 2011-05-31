from setuptools import setup, find_packages
import os

version = '0.1.0'

setup(name='plonetheme.freshpick',
      version=version,
      description="An installable Diazo theme for Plone 4.1",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Alex Clark',
      author_email='aclark@aclark.net',
      url='https://github.com/collective/plonetheme.freshpick',
      license='Creative Commons Attribution-ShareAlike 3.0 Unported License.',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
