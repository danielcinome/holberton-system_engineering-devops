# Add a custom HTTP header with Puppet
exec { 'Puppet HTTP':
command => "apt-get update && apt-get -y install nginx"
command => "echo -e 'Holberton School' > /var/www/html/index.html"
command => "sed -i '/sendfile on;/a add_header X-Served-By $hostname;' /etc/nginx/nginx.conf && service nginx start",
provider => 'shell',
}