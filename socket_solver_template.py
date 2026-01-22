from pwn import *
import re

# 各種設定
context.log_level = 'debug'
host="example.com"
port=80
io=remote(host, port)
text="Question:"

def main():
    while True:
        receive_text=io.recvuntil(text).decode()
        clean_formula=re.sub(r"[^0-9+\-*/(). ]","",receive_text)
        io.sendline(four_operations(clean_formula).encode())

def four_operations(formula):
    return str(eval(formula))

main()