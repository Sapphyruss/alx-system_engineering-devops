#configure the server using puppet

package {'nginx':
ensure => 'latest',
}

file {'/var/www/html/index.html':
ensure  => 'present',
path    => '/var/www/html/index.html',
content => 'Hello World!',
}

file {'/var/www/html/404.html':
ensure  => 'present',
path    => '/var/www/html/404.html',
content => "Ceci n'est pas une page",
}

file {'/etc/nginx/sites-available/default':
ensure => 'present',
path   => '/etc/nginx/sites-available/default',
}

exec {'sed':
command => "/bin/sed -i '/listen 80 default_server;/a \\
\\
    location /redirect_me {\\
    return 301 https://github.com/Mennatalla-Khougha; \\
    } \\
\\
    error_page 404 /404.html; \\
    location =/404.html { \\
    root /var/www/html; \\
    internal; \\
    }' /etc/nginx/sites-available/default",
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
