
cd server
dnc . -v -sp ../distributor
cd ..

@REM # Compule distributor
cd distributor
dnc . -sp ../server -v
dnc learning/UCB.dn
dnc RemoteDist.dn
dnc RemoteList.dn
dnc ./monitoring -sp ../server -v
dnc ./util  -v
dnc ./proxy -v


cd ..

@REM  Compile client
cd client
dnc . -v
cd ..

cd readn
dnc . -v
cd ../readn-writen
dnc . -v
cd ../writen
dnc . -v
cd ../constant
dnc . -v
cd ../step
dnc . -v

cd ..