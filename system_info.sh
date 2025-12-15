#!/bin/bash

echo "=== System Information ==="
echo "OS: $(uname -s)"
echo "Kernel Version: $(uname -r)"
echo

echo "=== Running Processes ==="
ps aux | head -10
echo

echo "=== Disk Usage ==="
df -h
echo

echo "=== Current User Information ==="
echo "Username: $(whoami)"
echo "Home Directory: $HOME"
echo