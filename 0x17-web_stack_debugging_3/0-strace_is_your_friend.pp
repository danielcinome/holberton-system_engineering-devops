# repair apache error 500
exec { 'error':
  command => 'sed 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php'
}
