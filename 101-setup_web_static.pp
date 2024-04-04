# 101-setup_web_static.pp

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the /data/web_static/releases/test/ directory exists
file { '/data/web_static/releases/test/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
  require => Package['nginx'],
}

# Ensure the /data/web_static/shared/ directory exists
file { '/data/web_static/shared/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
  require => File['/data/web_static/releases/test/'],
}

# Create a fake HTML file to test your Nginx configuration
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
  require => File['/data/web_static/releases/test/'],
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  require => File['/data/web_static/releases/test/index.html'],
}

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
exec { 'update_nginx_config':
  command => "/bin/sed -i '/^\\tlocation \\/\\//a \\t\\tlocation /hbnb_static/ {\\n\\t\\t\\talias /data/web_static/current/;\\n\\t\\t\\tautoindex off;\\n\\t\\t}' /etc/nginx/sites-available/default",
  path    => ["/bin", "/usr/bin"],
}

# Ensure nginx is running
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Exec['update_nginx_config'],
  require   => Package['nginx'],
}
