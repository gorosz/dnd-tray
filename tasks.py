#!/usr/bin/env python3

from invoke import task


@task
def clean(c):
    c.run("rm -rf build")
    c.run("rm -rf dnd_tray.egg-info")


@task(clean)
def build(c):
    c.run("python setup.py build")
