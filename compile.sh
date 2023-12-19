#! /bin/bash
dnc ./utils -v

cd server
dnc . -v -sp ../distributor
cd ..

cd distributor
dnc . -sp ../server -v
dnc Distributor.dn -sp ../server -v
dnc learning/UCB.dn
dnc RemoteDist.dn
dnc RemoteList.dn
dnc ./monitoring -sp ../server -v
dnc ./util  -v
dnc ./proxy -sp ../readn -v


cd ..

cd client
dnc . -v
cd ..

cd readn
dnc . -sp ../ -v
cd ../readn-writen
dnc . -sp ../ -v
cd ../writen
dnc . -sp ../ -v
cd ../constant
dnc . -sp ../ -v
cd ../step
dnc . -sp ../ -v
cd ..
