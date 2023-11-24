# 1-install_a_package.pp

package { 'python3-pip':
  ensure => present,
}

package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
