# 1-install_a_package.pp

package { 'python3-pip':
  ensure => present,
}

package { ['Flask', 'Werkzeug']:
  ensure   => '2.1.0,2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

