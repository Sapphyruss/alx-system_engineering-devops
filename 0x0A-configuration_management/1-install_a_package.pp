class { 'python':
  version => 'system',
}

package { 'python3-pip':
  ensure => present,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin:/bin',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['install_flask'],
}
