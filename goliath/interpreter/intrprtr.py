#!/usr/bin/env python
# coding=utf-8


import re


html = {"header1": "<h1>{}</h1>",
        "header2": "<h2>{}</h2>",
        "header3": "<h3>{}</h3>",
        "header4": "<h4>{}</h4>",
        "header5": "<h5>{}</h5>",
        "header6": "<h6>{}</h6>",
        "bold": "<strong>{}</strong>"}


md_re = {"header": u'[\#]'}


def symbol_feeder(content):
    """docstring for symbol_feederx
    """
    symbols = re.findall(md_re["header"], content)
    if len(symbols) > 1:
        parsed_content = content.strip("".join(symbols))
    parsed_content = content.strip(symbols[0])
    return (symbols, parsed_content)


def markpreter(content):
    if symbol_feeder(content):
        # check if no errors occur
        symbol_target = symbol_feeder(content)
        tag = symbol_target[0]
        content = symbol_target[1]
        if "#" in tag and len(tag) is 1:
            html_tag = html["header1"]
        elif "#" in tag and  len(tag) is 2:
            html_tag = html["header2"]
        elif "#" in tag and  len(tag) is 3:
            html_tag = html["header3"]
        elif "#" in tag and len(tag) is 4:
            html_tag = html["header4"]
        elif "#" in tag and  len(tag) is 5:
            html_tag = html["header5"]
        elif "#" in tag and  len(tag) is 6:
            html_tag = html["header6"]
        return html_tag.format(content)


def runtest():
    test = ["#h1", "##2", "###3", "####4", "#!@!@!", "#!@@#!"]

    for tag in test:
        print tag, " --> ", markpreter(tag)


if __name__ == '__main__':
    runtest()
