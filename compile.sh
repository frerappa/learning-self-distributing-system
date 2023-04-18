# Compile server

cd server
dnc . -v -sp ../distributor
cd ..

# Compule distributor
cd distributor
dnc . -sp ../server -v
cd ..

# Compile client
cd client
dnc . -v
cd ..