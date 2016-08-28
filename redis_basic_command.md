## 安装

- wget http://labfile.oss.aliyuncs.com/files0422/redis-2.8.9.tar.gz

- tar xvfz redis-2.8.9.tar.gz

- cd redis-2.8.9

- make

- make install

## 测试安装

- make test


## Redis启动

#### 将可执行文件放置在$PATH环境目录下，便于以后执行程序时可以不用输入完整的路径

- cp redis-server /usr/local/bin

- cp redis-cli /usr/local/bin

- redis-server

## 查看Redis

- ps -ef | grep redis

## 通过启动命令检查Redis服务器状态

- netstat -nlt|grep 6397

## 启动Redis-client

- redis-cli


