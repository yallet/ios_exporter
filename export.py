import sys, binascii, base58
from bitcoin import *

if len(sys.argv) < 1:
    print 'Usage: %s "yallet backup phrase in quotes"' % sys.argv[0]
    sys.exit()

m = bip32_master_key(sys.argv[1])
print "private keys:"
for i in range(10): 
    node = bip32_ckd(m,i)
    priv = bip32_extract_key(node)
    #addr = pubtoaddr(bip32_extract_key(bip32_privtopub(node)))
    #print addr
    #print priv

    # get the compressed wif
    extended_key = '80' + priv
    first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
    second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
    final_key = extended_key+second_sha256[:8]
    wif = base58.b58encode(binascii.unhexlify(final_key))
    print (wif)
