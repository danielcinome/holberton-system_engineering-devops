# HTTPS SSL
![N|Solid](https://www.holbertonschool.com/holberton-logo.png)
--
![N|Solid](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/FlhGPEK.png)

## Background Context
#### 1. World wide web
Requirements:

-   Add the subdomain  `www`  to your domain, point it to your  `lb-01`  IP (your domain name might be configured with default subdomains, feel free to remove them)
-   Add the subdomain  `lb-01`  to your domain, point it to your  `lb-01`  IP
-   Add the subdomain  `web-01`  to your domain, point it to your  `web-01`  IP
-   Add the subdomain  `web-02`  to your domain, point it to your  `web-02`  IP
-   Your Bash script must accept 2 arguments:
```./1-world_wide_web danielchinome.tech web-02```

#### 2. HAproxy SSL termination
Requirements:

-   HAproxy must be listening on port TCP 443
-   HAproxy must be accepting SSL traffic
-   HAproxy must serve encrypted traffic that will return the  `/`  of your web server
-   When querying the root of your domain name, the page returned must contain  `Holberton School`
-   Share your HAproxy config as an answer file (`/etc/haproxy/haproxy.cfg`)

