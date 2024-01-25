# increase ulimit.

# increase soft file limit
exec { 'update soft limit':
  command  => "sed -i 's/^holberton soft nofile.*/holberton soft nofile 8192/' /etc/security/limits.conf",
  provider => 'shell',
}

# Increase the hard limit 
exec { 'update hard limit':
  command  => "sed -i 's/^holberton hard nofile.*/holberton hard nofile 8192/' /etc/security/limits.conf",
  provider => 'shell',
}
