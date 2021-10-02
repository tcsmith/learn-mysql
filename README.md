# python project to hack and learn about MySQL

## Docker

### Running the MySQL server and client with Docker

Create a network for the server to use. See: https://github.com/docker-library/mysql/issues/644#issuecomment-664107416 

    $ docker network create mysql-net

Optionally if you want persistence, create a volume 

    $ docker volume create learn-mysql

Run the server and expose the ports 

    $ docker run --network mysql-net -p 3306:3306 -p 33060:33060  -e MYSQL_ROOT_PASSWORD=learn --name learn-mysql-server --rm -d mysql:5.7

    If you want persistence be sure to mount the volume by adding the following option when starting the server

        -v learn-mysql:/var/lib/mysql

Connect a commandline mysql client 

    $ docker run --network mysql-net -it --rm --name learn-mysql-client mysql:5.7 mysql -hlearn-mysql-server -uroot -p

### Importing the sample data

Copy the example data 

    $ docker cp sql/mysqlsampledatabase.sql learn-mysql-client:/tmp

In the mysql client 

    $ source /tmp/mysqlsampledatabase.sql


### Docker compose 

The docker compose file creates a volume for database persistence

Start the server

    $ docker-compose up -d

Start the client 

    $ docker run --network learn-mysql_learn-mysql -it --rm --name learn-mysql-client mysql:5.7 mysql -hlearn-mysql_mysql_1 -uroot -p



## Sample database and learning

Following along with the MySQL tutorial here: https://www.mysqltutorial.org/
Get the sample database: https://www.mysqltutorial.org/mysql-sample-database.aspx
