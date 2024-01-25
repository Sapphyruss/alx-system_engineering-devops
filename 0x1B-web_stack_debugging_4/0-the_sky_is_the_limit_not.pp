# resolve limit of traffic 

# Increase ulimit of the default file
exec { 'fix-nginx-limit':
    command => 'sed -i "s/15/1024/" /etc/default/nginx',,
    path    => '/bin/:/usr/local/bin',
}

# Restart Nginx
exec { 'nginx-restart':
  command => '/usr/sbin/service nginx restart',
  path    => '/etc/init.d/'
  require => Exec['fix-nginx-limit'],
}
