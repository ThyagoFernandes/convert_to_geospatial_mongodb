# convert_to_geospatial_mongodb
Primeiro inicie o conteiner:
```
docker run -p 27017:27017 --name mongo1 -v /home/<nome_do_usuario>/<nome_da_pasta>/mongo:/data/ -d mongo
```
Após isso clone o repositório do dataset:
```
git clone https://github.com/gustavoleitao/mongo-dataset.git
```
Entre no container:
```
docker exec -it mongo1 bash
```
E execute:
```
mongoimport --db dataset --collection restaurants --drop --file /data/primer-dataset.json
```
Agora basta apenas executar o script
```python
python main.py 
```
Ou caso exista uma versão python 2.x e outra seja 3.x:
```python
python3 main.py 
```
