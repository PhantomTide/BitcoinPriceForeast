# -*- coding: utf-8 -*-

"""
main.py
"""

from scrapy import cmdline


def main():
    """
    main()
    :return:
    """
    cmdline.execute("scrapy crawl chainnode_spider".split())


if __name__ == '__main__':
    main()
