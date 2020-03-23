# Configuration management
![N|Solid](https://www.holbertonschool.com/holberton-logo.png)
--
## Note on Versioning

Your Ubuntu 14.04 VM should have Puppet 3.4 preinstalled.

You do  **not**  need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

The linked documentation is to Puppet 3.8 because the 3.4 documentation has been archived and is therefore more challenging to navigate. If you would like to upgrade anyway,  [click here](https://intranet.hbtn.io/rltoken/EsVXllVK3mhoPLW_XUlxVA "click here")  (this will not affect how your code is checked).  [Puppet 5 Docs](https://intranet.hbtn.io/rltoken/_xOod_Lzz8WKTbhpG5SWLQ "Puppet 5 Docs")

### Install  `puppet-lint`

```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```
#### Task 2
Using Puppet, create a manifest that kills a process named `killmenow`.
```
root@d391259bf577:/# cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
done

root@d391259bf577:/# ./killmenow
```
