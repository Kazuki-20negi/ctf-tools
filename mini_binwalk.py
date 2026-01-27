import os
import sys

SIGNATURES = { #マジックナンバー
    'ZIP': b'\x50\x4B\x03\x04',      # PK..
    'PNG': b'\x89PNG\r\n\x1a\n',     # .PNG....
    'PDF': b'%PDF-',                 # %PDF-
    'GIF': b'GIF89a',                # GIF89a
}

target_file="test.jpg"

with open(target_file, "rb") as f:
    data=f.read()

for file_type, magic_bytes in SIGNATURES.items():
    offset=0
    while True:
        found_index= data.find(magic_bytes,offset)
        if found_index==-1:
            break
        if found_index>0:
            print(f"{file_type}ヘッダを発見")
            finded_data=data[found_index:]
            output_name=f"hidden.{file_type.lower()}"
            with open(output_name, "wb") as out_file:
                out_file.write(finded_data)
                print(f"{output_name}を保存しました")