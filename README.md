# Aplicação de algoritmos Multi-Armed Bandits para sistemas auto-distribuídos 

## Para compilar o projeto:

### Servidor

Entre na pasta _server_ em um terminal e digite:

```
dnc . -v
```

### Distribuidor

Entre na pasta _distributor_ em um terminal e digite:

```
dnc . -sp ../server -v
```

### Cliente

Entre na pasta _client_ em um terminal e digite:

```
dnc . -v
```

## Para executar o distribuidor (local e remote):
O projeto permite a execução de três configurações de modificação de estado, representada nos comandos a seguir por `[MODE]``.
- Custo apenas de leitura `readn`
- Custo apenas de escrita `writen`
- Custo de leitura e escrita `readn-writen`


Abra três terminais na pasta _distributor_. Para utilizar a adaptação automática, no primeiro execute:

```
dana -sp "../server;../[MODE];../" App.o
```
Para a execução do modelo, é necessária a execução de um script em Python. Em `learning-distributor` execute `pip3 install -r requirements.txt` para a instalação das bibliotecas necessárias. Após isso, ao verificar que o servidor em Dana está em execução, execute:

```
python3 app.py
```

Caso deseje que a adaptação seja feita pela inserção de comandos no terminal, execute":
```
dana -sp "../server;../[MODE];../" App.o manual
```
A primeira composição do servidor que o Distribuidor monta é a versão local. Para distribuí-lo, digite help e escolhar qual opção de distribuir. Para tornar o servidor todo local novamente, digite local.

Em um segundo terminal digite:

```
dana -sp "../[MODE];../" RemoteDist.o
```

Em um terceiro terminal digite:

```
dana -sp "../[MODE];../" RemoteDist.o 8082 2011
```



