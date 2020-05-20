#repair apache error 500
exec { 'repair error':
  provider => shell,
  command  => 'sed -i "s+require_once( ABSPATH . WPINC . \'/class-wp-locale.phpp\' );+require_once\
( ABSPATH . WPINC . \'/class-wp-locale.php\' );+g" /var/www/html/wp-settings.php',
}
