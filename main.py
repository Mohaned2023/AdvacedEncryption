from os import system,path
try :
    from cryptography.fernet import Fernet
    from argparse            import ArgumentParser
except :
    print("Installing...")
    system(f"pip install -r {__file__.replace('main.py','')}requirements.txt")

try :
    from src.encode import encode
    from src.decode import decode
except:
    print("\033[0;31mOh!, There is a problem with the tool files...!!\033[0m")

def main(en:bool,message:str=None, key:str=None, encode_message:str=None) -> None :
    if en :
        key, en = encode(
            Fernet=Fernet,
            message=message.encode()
        )
        print(f"\033[0;34mYour message is : (\033[0;32m{en}\033[0;34m)\033[0m")
        print(f"\033[0;34mYour key is : (\033[0;32m{key}\033[0;34m)\033[0m")
    else :
        de:str = decode(
            Fernet=Fernet, 
            key=key.encode(),
            en=encode_message.encode()
        )
        if de != "ERROR" :
            print(f"\033[0;34mThe message is : (\033[0;32m{de}\033[0;34m)\033[0m")
        else : 
            print ("\033[0;31mERROR: Key or Encode-Message Error...!!\033[0m")

if __name__ == "__main__" :
    preser:ArgumentParser = ArgumentParser()
    preser.add_argument(
        '-en',
        '--encode',
        help="\033[0;34mBoolean Value if you need to encrypt a message. -> true or false\033[0m",
        required=True,
        type=str
    )
    preser.add_argument(
        '-m',
        '--message',
        help="\033[0;34mSet the message which you want to encrypt.\033[0m",
        type=str
    )
    preser.add_argument(
        '-k', '--key', 
        help="\033[0;34mSet The Key For The Decrypt.\033[0m",
        type=str
    )
    preser.add_argument(
        '-em',
        '--encode-message',
        help="\033[0;34mSet The Encrypt-Message For The Decrypt.\033[0m",
        type=str
    )
    arge = preser.parse_args()
    if arge.encode == "true" and arge.message :
        main(
            message=arge.message, 
            en=True,
        )
    elif arge.encode == "false" and arge.key and arge.encode_message :
        main( 
            encode_message=arge.encode_message,
            key=arge.key,
            en=False
        )
    else : 
        print ("\033[0;31mPlease read the documentation for using...!!\033[0m")
        print ("\t\033[0;31mRead the documentation: \033[0;32mhttps://github.com/Mohaned2023/AdvacedEncryption\033[0m\n\n")
        system(f"python {__file__} --help")