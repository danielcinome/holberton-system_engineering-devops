i repair apache error 500
exec { 'error':
  provider => shell,
  command => 'sed 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php'
}
