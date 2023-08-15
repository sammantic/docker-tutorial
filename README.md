# docker-tutorial

Run MYSQL and PHPMYADMIN on two separate container

- Run Mysql:
  
docker run --name mysqltest1 -p 3306:3306 --network test_network -e MYSQL_ROOT_PASSWORD=root -d mysql

- Run Phpmyadmin:

 docker run --name myphptest2 -p 8081:80 --network test_network -e PMA_HOST=mysqltest1 -e PMA_PORT=3306 -d phpmyadmin
