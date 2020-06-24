#!/usr/bin/env python3

from invoke import task


@task
def clean(c):
    c.run("rm -rf build")
    c.run("rm -rf dnd_tray.egg-info")
    c.run("rm -rf dist")


@task(clean)
def build(c):
    c.run("python setup.py build")


@task(clean)
def build_wheel(c):
    c.run("python setup.py bdist_wheel")


@task(build_wheel)
def publish(c, test_release=True):
    if test_release:
        c.run("twine upload -r testpypi dist/*")
    c.run("twine upload dist/*")
