#!/bin/bash
# {
    sed 's/\\-/*/g' | 
    # sed -E 's/([A-Za-z]+)~([a-zA-Z0-9]+)~/$\1_\{\2\}$/g' |
    sed 's/7\\>/              \- 7>/g' | 
    sed 's/6\\>/            \- 6>/g' | 
    sed 's/5\\>/          \- 5>/g' | 
    sed 's/4\\>/        \- 4>/g' | 
    sed 's/3\\>/      \- 3>/g'| 
    sed 's/2\\>/    \- 2>/g'| 
    sed 's/1\\>/\- 1>/g' | 
    sed -E 's/(\[[0-9]+\])/\[\1\](#2-References)/g'
    # sed 's/clause\s(([0-9]\.)+[0-9])/clause\s\1()
    # sed 's/\[\[0-9]]/\[[\d](#References)\]/g'
#  } > 38321-ver1.md # change variable with subscript to latex format
##\b[A-Z]{2,}\b   ## regex for abbreviations
