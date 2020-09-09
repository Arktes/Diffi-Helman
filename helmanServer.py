import socket

s = socket.socket()
s.bind(('', 10001))
s.listen(1)
c, a = s.accept()

print('connected: ' + str(a))

while True:
    data = c.recv(1024)
    data = data.decode('utf-8')
    if data:
        break
new_data = data.split(' ')
g = int(new_data[0])
p = int(new_data[1])
A = int(new_data[2])

b = int(input("Введите значение b: "))
B = pow(g, b) % p
c.send(str(B).encode('utf-8'))
c.close()

K = pow(A, b) % p


print("key is " + str(K))
input("всё")
