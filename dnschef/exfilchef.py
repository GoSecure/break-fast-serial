from binascii import unhexlify
import string

def qname_handler(qname):

    subdomain = qname.split(".")[0]
    if(all(c in string.hexdigits for c in subdomain)):
        data = unhexlify(subdomain)
    	print data.split(":")

execfile('dnschef.py')