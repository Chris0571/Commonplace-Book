#!/bin/bash
#realizzato gentilmente da G.

cd $HOME

sudo apt update
sudo apt upgrade -y

sudo apt install build-essential cpputest libpcap-dev libpcre3-dev libnet1-dev zlib1g-dev luajit hwloc libdumbnet-dev bison flex libmnl-dev uuid-dev liblzma-dev openssl autotools-dev libssl-dev pkg-config libhwloc-dev cmake libsqlite3-dev  libunwind-dev libcmocka-dev libnetfilter-queue-dev libluajit-5.1-dev libfl-dev -y

mkdir ${HOME}/snort_src
cd ${HOME}/snort_src

git clone https://github.com/snort3/libdaq.git
cd libdaq
./bootstrap
./configure
make
sudo make install

cd ${HOME}/snort_src
wget https://github.com/gperftools/gperftools/releases/download/gperftools-2.9.1/gperftools-2.9.1.tar.gz
tar xzf gperftools-2.9.1.tar.gz
cd gperftools-2.9.1/
./configure
make
sudo make install

cd ${HOME}/snort_src
wget [https://github.com/snort3/snort3/archive/refs/heads/master.zip] https://github.com/snort3/snort3/archive/refs/heads/master.zip
unzip master.zip
cd snort3-master
./configure_cmake.sh --prefix=/usr/local --enable-tcmalloc
cd build
make
sudo make install
sudo ldconfig

snort -V
