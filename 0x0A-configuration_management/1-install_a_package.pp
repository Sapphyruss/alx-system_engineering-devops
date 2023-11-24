# 1-install_a_package.pp

package { 'python3-pip':
  ensure => present,
}

package { 'flask':
  ensure   => '2.1.0',
  version  => 'Werkzeug 2.1.1',
  name     => 'flask',
  provider => 'pip3',
  require  => package['python3-pip'],
}
