# Learn-MySQL

A project to get learned on MySQL, now using MariaDB, Flyway for the migrations, and Python to access the DB programmitcally

## Docker

Using docker compose to run a MariaDB server.
Initial data data is done via flyway as are subsequent migration

The docker compose file creates a volume for database persistence.
It can optionally be deleted when stopping the DB.


### Initial Run

Start the database server

    $ docker-compose up learn-mysql -d

Start the database client 

    $ docker run --network learn-mysql_learn-mysql -it --rm --name learn-mysql-client mariadb:10.3 mysql -hlearn-mysql_learn-mysql_1 -uroot -plearn

Create the classicmodels database 

    MariaDB [(none)]> CREATE DATABASE classicmodels;

Run flyway to create and fill the tables 

    $ docker-compose up learn-mysql-flyway
    

### Subsequent Runs

Stopping the server 

    $ docker-compose down

This stops the server but keeps the persistent storage volume.
To remove the volume and start fresh do: 

    $ docker-compose down --volumes


## Sample database and learning

Following along with the MySQL tutorial here: https://www.mysqltutorial.org/
Get the sample database: https://www.mysqltutorial.org/mysql-sample-database.aspx
