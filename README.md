# python-real-time-application


#python referance code 

https://docs.docker.com/language/python/build-images/








create database databasename;

use databsename;

show tables;

select * from flasktab;

IMP creating for inside of database:-
===================================
create table flasktab (name VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL, company VARCHAR(100) NOT NULL);

mysql -h database.cd6r8d9nxxja.us-east-1.rds.amazonaws.com -u admin -p


Docker file:-
-----------
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]





flask 

flask mysql









 339  python3 app.py       ----------------->v.imp
  340  python app.py
  341  pip2 list
  342  python3 app.py
  343  pip3 install flask
  344  python3 app.py
  345  pip3 install flaskext
  346  pip3 install flaskext --user
  347  cat app.py
  348  pip3 install mysqlclient
  349  python3 app.py
  350  pip3 install flask-mysql
  351  python3 app.py
  352  pip3 freeze >requirements.txt
  353  ls
  354  docker build -t dockerfile .
  355  vi Dockerfile
  356  docker build -t dockerfile .
  357  ls
  358  vi Dockerfile
  359  cat requirements.txt
  360  docker build -t myapp .
  361  vi requirements.txt
  362  docker build -t myapp .
  363  docker images
  364  docker run -d -p 5000:5000 myapp
  365  docker ps
  366  docker exec -it 45415c655d03 bash
  367  docker run -p 5000:5000 myapp
  368  docker run -p 4562:5000 myapp
  369  mysql -h database.cd6r8d9nxxja.us-east-1.rds.amazonaws.com -u admin -p
  370  docker pull mysql
  371  history







