# Kill a process by name
exec { 'kill-killmenow':
    command => 'pkill killmenow',
    path    => '/usr/bin';
}
