import socket,argparse
from datetime import datetime

MAX_BYTES=65535


def server(port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1",port))
    print("listening at {}".format(sock.getsockname()))

    while True:
        data,address=sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print("the {} is saying ....{!r}".format(address,text))
        print("your data was {} bytes long".format(len(text)))

def client(port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    text ='the tiem is {}'.format(datetime.now())
    data= text.encode('ascii')
    sock.sendto(data,("127.0.0.1",port))
    print("the os assigned me the address {}".format(sock.getsockname()))
    data,address=sock.recvfrom(MAX_BYTES)
    text=data.decode('ascii')
    print('the server replied....{}'.format(text))


if __name__=='__main__':
    choices={'client':client,'server':server}
    parser=argparse.ArgumentParser(description="send and receive UDP locally")
    parser.add_argument('role',choices=choices,help='which role to play')
    parser.add_argument('-p',metavar='PORT',type=int, default=1060,help='udp port(default 1060)')


    args=parser.parse_args()
    function=choices[args.role]
    function(args.p)
