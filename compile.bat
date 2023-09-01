
cd server
dnc . -v -sp ../distributor
cd ..

@REM # Compule distributor
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

@REM  Compile client
cd client
dnc . -v
cd ..

@REM  Compile implementations
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

@REM  Compile utils
dnc ./utils -v