#!/usr/bin/perl

use strict;
use POSIX qw(strftime);
use DBI;
use POSIX qw(setuid); 
POSIX::setuid(0); 

my $tmpdir        = "/tmp";
my $backup_main = '/home/kali/htb/nunchucks/webbackup';
my $now = strftime("%Y-%m-%d-%s", localtime);
my $tmpbdir = "$tmpdir/backup_$now";

sub printlog
{
    print "[", strftime("%D %T", localtime), "] $_[0]\n";
}

sub archive
{
    printlog "Archiving...";
    system("/usr/bin/tar -zcf $tmpbdir/backup_$now.tar $backup_main/* 2>/dev/null");
    printlog "Backup complete in $tmpbdir/backup_$now.tar";
}

if ($> != 0) {
    die "You must run this script as root.\n";
}

printlog "Backup starts, tmpbdir: $tmpbdir";
mkdir($tmpbdir);
&archive;
printlog "Moving $tmpbdir/backup_$now to $backup_main";
system("/usr/bin/mv $tmpbdir/backup_$now.tar $backup_main");
printlog "Removing temporary directory";
rmdir($tmpbdir);
printlog "Completed";

