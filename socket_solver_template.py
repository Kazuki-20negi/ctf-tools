from pwn import *
import re

# 各種設定
host="example.com"
port=80
io=remote(host, port)
text="Question:"

def main():
    while True:
        receive_text=io.recvuntil(text).decode()
        io.sendline(four_operations(receive_text).encode())

def four_operations(formula):
    return str(eval(formula))
