#Apresentação#

import secrets
sorteio = []

for i in range (0,100):
    sorteio.append(i)

print(secrets.choice(sorteio))

'''secrets.randbelow()
secrets.choice(1,2,3,4,5,6,7,8,9,10)
secrets.randbits(8)
secrets.token_bytes(32)
secrets.token_hex(16)
secrets.token_urlsafe(16)'''