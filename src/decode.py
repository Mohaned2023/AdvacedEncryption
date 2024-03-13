def decode(Fernet,key:bytes, en:bytes) -> str :
    try :
        cypher:Fernet = Fernet(key)
        de:bytes = cypher.decrypt(en)
        return de.decode()
    except :
        return "ERROR"