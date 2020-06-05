#socket with selector mudules for handling multiple connection at a time

import selectors,socket
sel = selectors.DefaultSelector()

lsock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
lsock.bind(("127.0.0.1",1114))
lsock.listen()

print("listineing on ")

lsock.setblocking(False)

#registor the socket with selectors
sel.register(lscok,selectors.EVENT_READ,data=None)



#creating a event loop....
while True:
    events = sel.select(timeout=None)
    for key,mask in events:
        """If key.data is None, then we know it’s from the listening socket and we need to accept() the connection.
        We’ll call our own accept() wrapper function to get the new socket object and register it with the selector.
        We’ll look at it in a moment."""
        if key.data is None:
            accept_wrapper(key.fileobj)
        else:
            service_connection(key,mask)


def accept_wrapper(sock):
    conn,addr=sock.accept()
    print("accepted connection from",addr)
    conn.setblocking(False)
    data=types.SimpleNamespace(addr=addr,inb=b'',outb=b'')
    events=selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn,events,data=data)


def service_connection(key,mask):
    sock=key.fileobj
    data=key.data

    if mask & selector.EVENT_READ:
        recv_data=sock.recv(1024)
        if recv_data:
            data.outb+=recv_data
        else:
            print("closing connection t0",data.addr)
            sel.unregister(sock)
            sock.close()

    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print("echoing",repr(data.outb),'to',data.addr)
            sent=sock.send(data.outb)
            data.outb=data.outb[sent:]


message =[b'Message 1 form client.',b'Message 2 from client']


def start_conections(host,port,num_conns):
    server_addr=(host,port)
    for i in range(0,num_conns):
        connid=i+1
        print("staring connection",connid,'to',server_addr)
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events=selector.EVENT_READ | selector.EVENT_WRITE
        data=types.SimpleNamespace(connid=connid,msg_total=sum(len(m) for m in message),recv_total=0,message=list(message), outb=b'')

        sel.register(so
