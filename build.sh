#!/bin/bash
pyinstaller -F bas.py
echo "--------------"
echo "output in: $(pwd)/dist" 
