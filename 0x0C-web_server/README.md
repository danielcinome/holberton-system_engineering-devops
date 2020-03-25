# Web server
![N|Solid](https://www.holbertonschool.com/holberton-logo.png)
--
_For this project, students are expected to look at these concepts:_

-   _[DNS](https://intranet.hbtn.io/concepts/12)_
-   _[Web Server](https://intranet.hbtn.io/concepts/17)_
-   _[CI/CD](https://intranet.hbtn.io/concepts/43)_
-   _[Docker](https://intranet.hbtn.io/concepts/65)_
-   _[Web stack debugging](https://intranet.hbtn.io/concepts/68)_
-   _[DevOps](https://intranet.hbtn.io/concepts/124)_
-   _[System Administration](https://intranet.hbtn.io/concepts/125)_
-   _[Site Reliability Engineering](https://intranet.hbtn.io/concepts/126)_

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png)

## Background Context

In this project, some of the tasks will be graded on 2 aspects:

1.  Is your  `web-01`  server configured according to requirements
2.  Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file  `/tmp/test`  containing the string  `hello world`  and modify the configuration of Nginx to listen on port  `8080`  instead of  `80`, I can use  `emacs`  on my server to create the file and to modify the Nginx configuration file  `/etc/nginx/sites-enabled/default`.

But my answer file would contain:

```
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu

```

As you can tell, I am not using  `emacs`  to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an  [SRE](https://intranet.hbtn.io/rltoken/Hjv9yJQtW6X7VRa2ByMeEg "SRE"), that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the  `root`  user, you do not need to use the  `sudo`  command.

A good Software Engineer is a  [lazy Software Engineer](https://intranet.hbtn.io/rltoken/y1MX-uAX-0a4bgXfH3uweQ "lazy Software Engineer").  ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg)

Tips: to test your answer Bash script, feel free to reproduce the checker environment:

-   start an  `ubuntu:16.04`  Docker container
-   run your script on it
-   see how it behaves

Check out the Docker concept page for more info about how to manipulate containers.

