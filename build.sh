#!/bin/bash
pyinstaller -F --add-data "./include:." bas.py 
echo "--------------"
echo "output in: $(pwd)/dist" 
