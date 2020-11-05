# IP Generator
# :) Vexvain :)
import sys, socket
from sys import argv
from sys import exit
from os import system
from time import sleep
from random import randint

class Opts(object):
    def __init__(self):
        super(Opts, self).__init__()
        self.port = None
        self.outfile = None
        self.past_hosts = []
        
    def check_port(self, host):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout((0.01))
        try:
            sock.connect((host, self.port))
            sock.close()
            return True
        except:
            return False
        
    def rand_ip(self):
        final = None
        while(True):
            found = 0
            i1 = randint(1, 254)
            i2 = randint(1, 254)
            i3 = randint(1, 254)
            i4 = randint(1, 254)
            final = "%d.%d.%d.%d" % (i1, i2, i3, i4)
            for ok in self.past_hosts: # Check to see if we've already tried this host
                if(ok == final):
                    found = 1
                    break
            if(found == 1):
                continue
            else:
                if(final):
                    if(self.check_port(final) == True):
                        self.past_hosts.append(final)
                break
        if(final):
            return final
            
    def make_ips(self, amountofips):
        amountofips = int(amountofips)
        for x in range(0, amountofips):
            new_hosttttt = self.rand_ip()
            cmd = "echo '%s:%d' >> %s" % (new_hosttttt, self.port, self.outfile)
            system(cmd)
            print("[\x1b[35m+\x1b[37m] Found host on port(\x1b[33m{}\x1b[37m) -> \x1b[36m{}\x1b[37m".format(self.port, new_hosttttt))
             
def main():
    print("[\x1b[34m+\x1b[37m]-| IP generating script |-[\x1b[34m+\x1b[37m]")
    argc = len(argv)
    if(argc < 4 or argc > 4):
        exit("[\x1b[31m?\x1b[37m] Usage: python "+argv[0]+" <port> <amount of ips to find> <output file>")
        
    sleep(2)
    nport = argv[1]
    amteyepees = argv[2]
    outfile = argv[3]
    
    opt = Opts()
    opt.port = int(nport)
    opt.outfile = outfile
    opt.make_ips(amteyepees)
    
if(__name__ == "__main__"):
    main()
