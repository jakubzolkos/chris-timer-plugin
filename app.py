#!/usr/bin/env python

from pathlib import Path
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter
from chris_plugin import chris_plugin
from functools import wraps
import time


__version__ = '1.0.0'

DISPLAY_TITLE = r"""
ChRIS Timer Plugin
"""


parser = ArgumentParser(
    description='A test ChRIS plugin that print the execution time of the main script.',
    formatter_class=ArgumentDefaultsHelpFormatter
)


def timer(func):
    @wraps(func)
    def wrapper(a, b):
        start_time = time.time()
        retval = func(a, b)
        print("the function ends in ", time.time()-start_time, "secs")
        return retval
    return wrapper


# The main function of this *ChRIS* plugin is denoted by this ``@chris_plugin`` "decorator."
# Some metadata about the plugin is specified here. There is more metadata specified in setup.py.
#
# documentation: https://fnndsc.github.io/chris_plugin/chris_plugin.html#chris_plugin
@chris_plugin(
    parser=parser,
    title='ChRIS Timer',
    category='',
    min_memory_limit='100Mi',
    min_cpu_limit='1000m',
    min_gpu_limit=0
)
@timer
def main(options: Namespace, outputdir: Path):
    """
    :param options: non-positional arguments parsed by the parser given to @chris_plugin
    :param outputdir: directory where to write output files
    """

    print(DISPLAY_TITLE)
    for i in range(10000000):
        continue


if __name__ == '__main__':
    main()
