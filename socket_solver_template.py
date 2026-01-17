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
        receive_text=io.recvuntil(text).decode() #数式部を取り出す処理が必要
        io.sendline(four_operations(receive_text).encode())

def four_operations(formula):
    return str(eval(formula))

main()