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

def try_base32(text):
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

def is_readable_text(s):
    if not s:
        return False
    return s.isprintable()

def magic_decode(input_text):
    results={}
    decoders = {
        "Base64": try_base64,
        "Base32": try_base32,
        "URL": try_url,
        "Hex": try_hex,
        "ROT13": try_rot13,
    }

    for name, func in decoders.items():
        decoded=func(input_text)
        if decoded and is_readable_text(decoded):
            results[name]=decoded
    return results


input_str="SGVsbG8gV29ybGQ="
decoded_text=magic_decode(input_str)
print(f"デコード結果：{decoded_text}")

for i in decoded_text.values():
    print(f"再帰デコード：{magic_decode(i)}")