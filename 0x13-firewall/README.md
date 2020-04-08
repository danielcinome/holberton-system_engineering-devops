# Firewall
![N|Solid](https://www.holbertonschool.com/holberton-logo.png)
--
![N|Solid](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png)

## Background Context
As explained in the  [web stack debugging guide](https://intranet.hbtn.io/rltoken/IbBjSeDqQbEbeom47M0e9g "web stack debugging guide"),  `telnet`  is a very good tool to check if sockets are open with  `telnet IP PORT`. For example, if you want to check if port 22 is open on  `web-02`:

```
sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is '^]'.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
sylvain@ubuntu$
```
**Be very careful with firewall rules! For instance, if you ever deny port  `22/TCP`  and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.**

