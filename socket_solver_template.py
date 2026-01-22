from pwn import *
import re

# 各種設定
context.log_level = 'debug'
host="127.0.0.1"
port=9999
io=remote(host, port)
text="Question:"

def main():
    while True:
        io.recvuntil(text)
        clean_formula=io.recvline().decode().strip()
        io.sendline(four_operations(clean_formula).encode())

def four_operations(formula):
    return str(eval(formula))

main()