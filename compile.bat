
cd server
dnc . -v -sp ../distributor
cd ..

@REM # Compule distributor
cd distributor
dnc . -sp ../server -v
dnc RemoteDist.dn
dnc RemoteList.dn
cd ..

@REM  Compile client
cd client
dnc . -v
cd ..