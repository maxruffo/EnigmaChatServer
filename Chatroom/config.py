import rsa
host = '127.0.0.1'                                                      #LocalHost
port = 8089   
pubKey, privKey = rsa.newkeys(512)
publicKey= pubKey 
privateKey= privKey