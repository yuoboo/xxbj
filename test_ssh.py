
from pexpect import pxssh
import getpass


def test_ssh():
    try:
        s = pxssh.pxssh()
        hostname = '10.133.147.176'
        username = 'root'
        password = getpass.getpass('password: ')
        s.login(hostname, username, password)
        s.sendline('uptime')  # run a command
        s.prompt()  # match the prompt
        print s.before  # print everything before the prompt.
        s.sendline('ls -l')
        s.prompt()
        print s.before
        s.sendline('df')
        s.prompt()
        print s.before
        s.logout()
    except pxssh.ExceptionPxssh, e:
        print "pxssh failed on login."
        print str(e)


if __name__ == '__main__':
    test_ssh()
    print 'this is over'
