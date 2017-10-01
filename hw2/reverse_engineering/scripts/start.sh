# !/bin/bash

# For more information on dependencies and build instructions, see

# https://github.com/EZLippi/WebBench

apt-get install ctags && #

# download the source archive

git clone https://github.com/EZLippi/WebBench.git &&

cd WebBench &&

sudo make && sudo make install

