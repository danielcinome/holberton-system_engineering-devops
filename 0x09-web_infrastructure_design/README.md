# Web infrastructure design
![N|Solid](https://www.holbertonschool.com/holberton-logo.png)
--
## Background Context

#### 0. Simple web stack
##### LAMP stack
-   1 server
-   1 web server (Nginx)
-   1 application server
-   1 application files (your code base)
-   1 database (MySQL)
-   1 domain name  `foobar.com`  configured with a  `www`  record that points to your server IP  `8.8.8.8`
Before developing a big and complex web application, we will build the front end step-by-step.
#### 1. Distributed web infrastructure
-   2 servers
-   1 web server (Nginx)
-   1 application server
-   1 load-balancer (HAproxy)
-   1 set of application files (your code base)
-   1 database (MySQL)
#### 2. Secured and monitored web infrastructure
-   3 firewalls
-   1 SSL certificate to serve  `www.foobar.com`  over HTTPS
-   3 monitoring clients (data collector for Sumologic or other monitoring services)
#### 3. Scale up
-   1 server
-   1 load-balancer (HAproxy) configured as cluster with the other one
-   Split components (web server, application server, database) with their own server

