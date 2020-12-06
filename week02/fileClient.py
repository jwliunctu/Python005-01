import socket
import os
import sys

host = "localhost"
port = 6666
filename = input("Please input full file path (ex. ../Week02.pdf):")
if not os.path.isfile(filename):
        print(f"[!] {filename} does not exist!")
        sys.exit()


# 檔案大小
size = os.path.getsize(filename)

s = socket.socket()
print(f"[+] Connecting to {host}:{port}")
try:
    s.connect((host, port))
except Exception as e:
    print(e)
    sys.exit()

print("[+] Connected.")
s.send(f"{filename}:::{size}".encode()) #傳送: {檔案}:::{檔案大小}

# 發送文件
with open(filename, "rb") as f:
    s.sendall(f.read())

s.close()