i repair apache error 500
exec { 'error':
  command => 'sed -i "s+require_once( ABSPATH . WPINC . \
  '/class-wp-locale.phpp\' );+require_once( ABSPATH . WPINC . \
  '/class-wp-locale.php\' );+g" /var/www/html/wp-settings.php',
}
