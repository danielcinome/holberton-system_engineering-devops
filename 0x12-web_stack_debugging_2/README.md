# Web stack debugging #2
![N|Solid](https://www.holbertonschool.com/holberton-logo.png)
--
![N|Solid](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/287/withgreatpower-holberton.png)

## Background Context
The user  `root`  is, on Linux, the superuser. It can do anything it wants, thats a good and bad thing. A good practice is that one should never be logged in the  `root`  user, as if you fat finger a command and for example run  `rm -rf /`, there is no comeback. Thats why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the  `root`  user can do, just need to use a specific command that you need to discover.

For the containers that you are given in this project as well as the checker, everything is run under the  `root`  user, which has the ability to run anything as another user.
### Task 0
```
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeonelese www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
```
### Task 1
```
root@ab6f4542747e:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
root@ab6f4542747e:~#
root@ab6f4542747e:~# nc -z 0 8080 ; echo $?
0
root@ab6f4542747e:~#
```

