from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from io import BytesIO

class Criptografia:
    
   
    def criaChaves(self):
       
        #cria chave
        key = RSA.generate(2048)
        #gerando chave pub e priv
        private_key= key.export_key()
        public_key= key.publickey().export_key()
        #criando dicionario
        chaves={"private":private_key, "public":public_key}
        return chaves

    def criptografar(self, pub, texto):
        #Variaveis
        lista=[]
        crip=''
        texto=str(texto)
        #Importando chave RSA
        chave_rsa_pub=RSA.import_key(pub)
        session=get_random_bytes(16)
        
        #encriptando chave RSA
        chave_rsa= PKCS1_OAEP.new(chave_rsa_pub)
        enc_ses=chave_rsa.encrypt(session)
        
        #encriptando dados com
        chavAes = AES.new(session, AES.MODE_EAX)
        text, tag = chavAes.encrypt_and_digest(texto.encode("utf8"))
        [lista.append(x) for x in(enc_ses, chavAes.nonce, tag, text)]
        crip=b''.join(lista)

        return crip
    
    def descriptografar(self, priv, texto):
        chave_rsa= RSA.import_key(priv)
        entrada=BytesIO(texto)

        chave_priv ,nonce, tag, text=\
            [entrada.read(x) for x in(chave_rsa.size_in_bytes(),16,16,-1)]

        #Descriptografando chave RSA
        cipher_rsa = PKCS1_OAEP.new(chave_rsa)
        session_key = cipher_rsa.decrypt(chave_priv)

        # Descriptografando dados com AES
        chave_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        descrip = chave_aes.decrypt_and_verify(text, tag)
        
        return descrip.decode("utf-8")
        

