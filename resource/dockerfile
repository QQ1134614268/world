###### https://blog.51cto.com/7424593/1759993  https://blog.csdn.net/hanlicun/article/details/79049598

FROM centos-6-x86_64

MAINTAINER huangming <741616710@qq.com>

#Install openssh

RUN yum install -y openssh-server

RUN mkdir /root/.ssh

COPY ./authorized_keys /root/.ssh/authorized_keys

RUN sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config

#Install MySQL

RUN yum install -y gcc gcc-c++ make automake

COPY ./cmake-3.4.3.tar.gz .

RUN mkdir -p /usr/local/cmake

RUN tar zxf cmake-3.4.3.tar.gz

RUN cd cmake-3.4.3 && ./bootstrap && make && make install

RUN groupadd mysql; useradd -r -g mysql mysql

RUN mkdir /usr/local/mysql; mkdir /data/mysql/db -p

RUN yum install gcc gcc-c++ ncurses-devel bison bison-devel -y

COPY ./mysql-5.6.29.tar.gz .

RUN tar zxf mysql-5.6.29.tar.gz

RUN cd mysql-5.6.29 && cmake . -DCMAKE_INSTALL_PREFIX=/usr/local/mysql -DMYSQL_DATADIR=/data/mysql/db -DSYSCONFDIR=/etc -DMYSQL_TCP_PORT=3306 -DMYSQL_UNIX_ADDR=/var/lib/mysql/mysql.sock -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_MYISAM_STORAGE_ENGINE=1 -DENABLED_LOCAL_INFILE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DDEFAULT_CHARSET=utf8 -DEXTRA_CHARSETS=all -DDEFAULT_COLLATION=utf8_general_ci -DWITH-MYSQLD-LDFLAGS=-all-static -DWITH-CLIENT-LD-FLAGS=-all-static -DWITH_DEBUG=0 && gmake && gmake install

RUN chown -R root:mysql /usr/local/mysql/ && chown -R mysql:mysql /data/mysql/db/

RUN cd /mysql-5.6.29/scripts && chmod 755 mysql_install_db.sh

RUN /mysql-5.6.29/scripts/mysql_install_db.sh --basedir=/usr/local/mysql --datadir=/data/mysql/db --no-defaults --user=mysql

RUN cd /mysql-5.6.29/support-files/ && cp my-default.cnf /etc/my.cnf && cp mysql.server /etc/init.d/mysqld

RUN chmod 755 /etc/init.d/mysqld && chkconfig mysqld on

RUN echo -e '#!/bin/bash\nexport PATH=$PATH:/usr/local/mysql/bin' >/etc/profile.d/mysql.sh

RUN source /etc/profile

#Install Nginx

RUN yum install zlib pcre pcre-devel openssl openssl-devel -y

RUN useradd -s /sbin/nologin nginx

COPY ./nginx-1.8.1.tar.gz .

RUN mkdir /usr/local/nginx

RUN tar zxf nginx-1.8.1.tar.gz

RUN cd /nginx-1.8.1/ && ./configure --prefix=/usr/local/nginx --user=nginx --group=nginx --sbin-path=/usr/sbin/nginx --conf-path=/etc/nginx/nginx.conf --with-http_stub_status_module --with-http_ssl_module --with-http_gzip_static_module --with-pcre --with-http_realip_module --with-http_sub_module && make && make install

RUN nginx -t

#Install php package dependency

RUN rpm -ivh http://mirrors.opencas.cn/epel/6/i386/epel-release-6-8.noarch.rpm

RUN yum -y install libpng-devel libtool libxslt-devel png bzip2 bzip2-devel libxml2-devel libXpm-devel curl-devel libmcrypt expat libxslt freetype freetype-devel libmcrypt-devel autoconf libpng zlib-devel zlib



COPY ./libiconv-1.14.tar.gz .

RUN mkdir /usr/local/libiconv  && tar zxf libiconv-1.14.tar.gz

RUN cd /libiconv-1.14 && ./configure --prefix=/usr/local/libiconv && make && make install && cd /

COPY ./jpegsrc.v6b.tar.gz .

RUN mkdir /usr/local/jpeg6 && mkdir /usr/local/jpeg6/{bin,lib,include,man} && mkdir /usr/local/jpeg6/man/man1

RUN tar zxf jpegsrc.v6b.tar.gz

RUN cp -r /usr/share/libtool/config/config.sub /jpeg-6b && cp /usr/share/libtool/config/config.guess /jpeg-6b

RUN cd /jpeg-6b && ./configure --prefix=/usr/local/jpeg6 --enable-shared --enable-static && make && make install && cd /

COPY ./libgd-2.1.1.tar.bz2 .

RUN mkdir /usr/local/libgd2 && tar jxf libgd-2.1.1.tar.bz2

RUN cd /libgd-2.1.1 && ./configure --prefix=/usr/local/libgd2 --with-zlib --with-jpeg=/usr/local/jpeg6 --with-png --with-freetype && make && make install && cd /

#Install php

RUN useradd -s /sbin/nologin php-fpm

COPY ./php-5.6.20.tar.bz2 .

RUN tar xjf php-5.6.20.tar.bz2

RUN cd /php-5.6.20 && ./configure --prefix=/usr/local/php --with-config-file-path=/usr/local/php/etc --enable-fpm --with-fpm-user=php-fpm --with-fpm-group=php-fpm --with-mysql=/usr/local/mysql --with-mysqli=/usr/local/mysql/bin/mysql_config --with-freetype-dir --with-jpeg-dir=/usr/local/jpeg6 --with-mcrypt --with-gd=/usr/local/libgd2 --with-iconv-dir=/usr/local/libiconv --with-png-dir --with-zlib --with-libxml-dir --with-curl --with-mhash --with-openssl --with-pear --enable-soap --enable-gd-native-ttf --enable-mbstring --enable-exif --enable-sockets --with-gettext --enable-ftp --disable-ipv6 --enable-bcmath --enable-shmop --enable-sysvsem --with-pcre-dir && make && make install

RUN cp /php-5.6.20/php.ini-production /usr/local/php/etc/php.ini

RUN cp /php-5.6.20/sapi/fpm/init.d.php-fpm /etc/init.d/php-fpm && chmod 755 /etc/init.d/php-fpm

RUN cp /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf

RUN /usr/local/php/sbin/php-fpm -t

#Install JDK

COPY ./jdk-8u65-linux-x64.rpm .

RUN rpm -ivh jdk-8u65-linux-x64.rpm

RUN echo -e 'export JAVA_HOME=/usr/java/latest\nexport PATH=$JAVA_HOME/bin:$PATH' > /etc/profile.d/java.sh

RUN . /etc/profile.d/java.sh

#Install Tomcat

COPY ./apache-tomcat-8.0.33.tar.gz .

RUN tar zxf apache-tomcat-8.0.33.tar.gz -C /usr/local/

RUN cd /usr/local/ && ln -sv apache-tomcat-8.0.33 tomcat

RUN echo -e 'export CATALNA_HOME=/usr/local/tomcat\nexport PATH=$CATALNA_HOME/bin:$PATH' > /etc/profile.d/tomcat.sh

RUN source /etc/profile

RUN cd / && rm -rf jdk-8u65-linux-x64.rpm mysql-5.6.29* jpeg* libgd* php-5.6.20* nginx-1.8.1* libiconv-1.14* cmake-3.4.3* apache-tomcat-8.0.33*



EXPOSE 80 8080 3306 22