#!/usr/bin/env python3

from setuptools import setup


setup(name='dnd-tray',
      version='0.1',
      description='Simple tray icon to disable/enable dunst notification',
      url='https://github.com/gorosz/dnd-tray.git',
      author='Gergely Orosz',
      author_email='gergelyo@protonmail.com',
      license='MIT',
      packages=['dnd_tray'],
      install_requires=[
          'pyside2',
      ],
      scripts=['bin/dnd-tray'],
      include_package_data=True,
      python_requires=">=3.6",
      zip_safe=False)
