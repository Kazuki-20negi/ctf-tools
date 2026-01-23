import base64
import binascii
import urllib.parse
import codecs

def try_base64(text):
    try:
        text+="="*((4-len(text)%4)%4)
        return base64.b64decode(text).decode("utf-8")
    except:
        return None

def tyr_base32(text):
    try:
        return base64.b32decode(text).decode("utf-8")
    except:
        return None
    
def try_rot13(text):
    return codecs.decode(text,"rot_13")

def try_url(text):
    try:
        decoded=urllib.parse.unquote(text)
        if text==decoded:
            return None
    except:
        return None

def try_hex(text):
    try:
        clean_text=text.replace(" ","").replace("\n", "")
        return bytes.fromhex(clean_text).decode("utf-8")
    except:
        return None




def magic_decode(input_text):
