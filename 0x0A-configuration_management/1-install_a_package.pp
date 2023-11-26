# 1-install_a_package.pp

package { 'python3-pip':
  ensure => present,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.1.1',
  path    => '/usr/local/bin:/usr/bin:/bin',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0" && /usr/bin/pip3 show Werkzeug | grep -q "Version: 2.1.1"',
  require => Package['python3-pip'],
}
