#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created: Mon, 29 Jul 2013 12:23:47 -0400

"""
SYNOPSIS

    vocab2edit.py < vocab > edit.txt

DESCRIPTION

    Constructs a uniform cost edit fst in OpenFst textual format.

AUTHOR

    Dogan Can <dogancan@usc.edu>

VERSION

    0.1
"""

import sys


def read_vocab(ifile):
    vocab = []
    for line in ifile:
        vocab += [line.strip()]
    return vocab


def vocab2edit(vocab, ofile):
    # Ω*
    for v in vocab:
        print >> ofile, 0, 0, v, "ε"
        print >> ofile, 0, 0, "ε", v
        for w in vocab:
            print >> ofile, 0, 0, v, w
    # Ψ
    for v in vocab:
        print >> ofile, 0, 1, v, "ε"
        print >> ofile, 0, 1, "ε", v
        for w in vocab:
            if v != w:
                print >> ofile, 0, 1, v, w
            else:
                print >> ofile, 0, 1, v, w, 1000000
    # Ω*
    for v in vocab:
        print >> ofile, 1, 1, v, "ε"
        print >> ofile, 1, 1, "ε", v
        for w in vocab:
            print >> ofile, 1, 1, v, w
    print >> ofile, 1

if __name__ == '__main__':
    vocab = read_vocab(sys.stdin)
    vocab2edit(vocab, sys.stdout)
