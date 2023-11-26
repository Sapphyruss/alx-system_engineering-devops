# set up client SSH configuration file

file_line {'/etc/ssh/ssh_config':
path => '/etc/ssh/ssh_config',
line => '
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
        ',
}
