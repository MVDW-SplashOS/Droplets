#!/bin/bash
pyinstaller -F --add-data "./include:." bas.py 
pyinstaller -F --add-data "./include:." bas_service.py 
echo "--------------"
echo "output in: $(pwd)/dist" 
