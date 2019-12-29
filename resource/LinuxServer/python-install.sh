#!/bin/bash
#1.准备编译环境 centos7.5 时间: 2019.10.23

yum install gcc gcc-c++ -y
yum install zlib*
#2. 下载python3.5包
wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz
#3. 解压，编译
tar -xvf Python-3.7.5.tgz
cd Python-3.7.5
./configure --prefix=/usr/local/python3.7
make && make install
#4. 删除老的链接
rm -rf /usr/bin/python
ln -s /usr/local/python3.7/bin/python3.7 /usr/bin/python
ln -s /usr/local/python3.7/bin/pip3 /usr/bin/pip

#5. 更新yum相关设置 /usr/bin/yum : /usr/libexec/urlgrabber-ext-down 第一行改为  #!/usr/bin/python2
sed -i '1c #!/usr/bin/python2' /usr/bin/yum
sed -i '1c #!/usr/bin/python2' /usr/libexec/urlgrabber-ext-down
