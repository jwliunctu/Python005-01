import socket
import os
import datetime

# 檢查上傳目錄
upload_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"upload/")
if not os.path.isdir(upload_dir):
    os.mkdir(upload_dir)
    print(f"[+] <{upload_dir}> was created!")

# 建立server
SERVER_HOST = "localhost"
SERVER_PORT = 6666

s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))

# 接受1個連接
s.listen(1)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

connect, address = s.accept()
print(f"[+] {address} is connected.")

# 接收文件信息
received = connect.recv(1024).decode()
print(f"[+] data received: {received}")
filename, size = received.split(":::")
print(f"[+] data size: {size} bytes")

# 上傳文件名加上時間戳記
d=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-")
filename = os.path.join(upload_dir, d+os.path.basename(filename))
print(f"[+] Location of destination file: {filename}")

# 寫入文件
with open(filename, "wb") as f:
    while True:
        data = connect.recv(1024)
        if not data:
            break
        f.write(data)
    connect.close()

s.close()