# python project to hack and learn about MySQL

## Running the MySQL server and client

Create as network for the server to use. See: https://github.com/docker-library/mysql/issues/644#issuecomment-664107416 

    $ docker network create mysql-net

Run the server 

    $ docker run --network mysql-net -p 3306:3306 -p 33060:33060  -e MYSQL_ROOT_PASSWORD=learn --name learn-mysql-server --rm -d mysql:5.7

Connect a commandline mysql client 

    $ docker run --network mysql-net -it --rm mysql:5.7 mysql -hlearn-mysql-server -uroot -p

## Sample database and learning

Following along with the MySQL tutorial here: https://www.mysqltutorial.org/
Get the sample database: https://www.mysqltutorial.org/mysql-sample-database.aspx
