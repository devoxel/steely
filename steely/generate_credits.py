#!/usr/bin/env python3


import os
import imp
from utils import list_plugins


def get_plugin_name(plugin):
    return plugin.__name__.rstrip('.py')


def is_multi_author(authors):
    valid_types = (list, tuple)
    return any(isinstance(authors, type) for type in valid_types)


def get_plugin_author(plugin):
    author_s = plugin.__author__
    if is_multi_author(author_s):
        return ', '.join(author_s)
    return author_s


def get_authors():
    for plugin in list_plugins():
        yield get_plugin_name(plugin), \
              get_plugin_author(plugin)


if __name__ == '__main__':
    print(*get_authors(), sep='\n')
