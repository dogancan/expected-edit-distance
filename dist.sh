#!/usr/bin/env bash

T=$1
X=$2
Y=$3

fstcompose $X $T | fstcompose - $Y | \
  fstencode --encode_labels - codex | fstdeterminize | \
  fstencode --decode --encode_reuse - codex | \
  fstmap --map_type=to_standard | fstmap --map_type=invert | \
  fstsynchronize | fstrmepsilon | \
  fstencode --encode_labels - codex2 | fstdeterminize | \
  fstmap --map_type=to_log | fstmap --map_type=invert | \
  fstshortestdistance --reverse | head -1 | awk '{print exp(-$2)}'

rm -f codex*
