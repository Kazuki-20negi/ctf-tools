import socket
import random
import time

# 設定
HOST = '127.0.0.1'  # 自分自身 (localhost)
PORT = 9999         # 適当なポート番号

def generate_question():
    """ランダムな計算式と答えを生成する"""
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    op = random.choice(['+', '-', '*'])
    formula = f"{a} {op} {b}"
    answer = str(eval(formula))
    return formula, answer

def start_server():
    # ソケットの作成（IPv4, TCP）
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"[*] サーバーが起動しました。 {HOST}:{PORT} で待機中...")
        
        # クライアントからの接続を待つ
        conn, addr = s.accept()
        with conn:
            print(f"[*] 接続されました: {addr}")
            conn.sendall(b"Welcome to the Mock CTF Server!\n")
            time.sleep(0.5) # 通信のラグを少しシミュレート

            count = 0
            while True:
                # 10問正解したらフラグを出して終了
                if count >= 10:
                    conn.sendall(b"Congratulations! The flag is CTF{sample_flag}\n")
                    break

                formula, ans = generate_question()
                question_text = f"Question: {formula}\n"
                
                print(f"[Server] 送信: {question_text.strip()} (答え: {ans})")
                conn.sendall(question_text.encode())

                # クライアントからの返信を受信
                try:
                    data = conn.recv(1024).decode().strip()
                except:
                    break
                
                print(f"[Server] 受信: {data}")

                if data == ans:
                    conn.sendall(b"Correct!\n")
                    count += 1
                else:
                    conn.sendall(f"Wrong! The answer was {ans}. Bye.\n".encode())
                    break
            
            print("[*] 接続を終了します")

if __name__ == "__main__":
    start_server()