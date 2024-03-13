def encode(Fernet, message:bytes) -> tuple[str] :
    key:bytes = Fernet.generate_key() 
    cypher:Fernet = Fernet(key)
    en:bytes = cypher.encrypt(message)
    return ( key.decode() , en.decode())