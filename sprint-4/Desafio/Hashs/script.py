import hashlib


def gerarHash(entrada):
    sha1 = hashlib.sha1()
    sha1.update(entrada.encode('utf-8'))
    return sha1.hexdigest()


entrada = input()
codificado = gerarHash(entrada)
print(codificado)