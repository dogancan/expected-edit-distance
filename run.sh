#!/usr/bin/env bash

cd test

# Generate and compile edit transducer
../vocab2edit.py < vocab | \
  fstcompile --arc_type=log --isymbols=syms --osymbols=syms > edit.fst

# Compile input automata
fstcompile --arc_type=log --acceptor --isymbols=syms x.txt | \
  fstpush --push_weights --remove_total_weight > x.fst
fstcompile --arc_type=log --acceptor --isymbols=syms y.txt | \
  fstpush --push_weights --remove_total_weight > y.fst

# compute distance
../dist.sh edit.fst x.fst y.fst
