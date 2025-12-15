#!/bin/bash
echo "Files in the current directory with their sizes:"
echo "---------------------------------------------"
ls -lh | grep "^-" | awk '{print $5 " " $9}'