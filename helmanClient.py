import socket

s = socket.socket()
s.connect(('localhost', 10001))
data = input("Введите g, p и a: ")
new_data = data.split(' ')
g = int(new_data[0])
p = int(new_data[1])
a = int(new_data[2])
A = pow(g, a) % p
new_data[2] = str(A)
data = ' '.join(new_data)
data = data.encode('utf-8')
s.send(data)

data = s.recv(1024)
B = int(data.decode('utf-8'))
K = pow(B, a) % p
s.close()

print("key is " + str(K))
input("всё")
