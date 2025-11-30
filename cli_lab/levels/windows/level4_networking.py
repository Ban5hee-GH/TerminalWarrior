# FILE: level4_networking.py
import time
from .utils import (
    clear_screen,
    print_header,
    print_objectives,
    print_success,
    generic_cmd_handler,
    CURRENT_DIR,
)


TARGET_IP = "172.16.1.50"
SERVICE_PORT = "8080"

def run_level():
    title = "LEVEL 4: NETWORKING CHALLENGE"
    objectives = [
        f"A new target IP was located: {TARGET_IP}. Check its connectivity.",
        "Scan the target for open services using 'netstat'."
    ]
    hint = f"First, 'ping {TARGET_IP}', then check local connections with 'netstat -an'."
    
    print_header(title)
    print_objectives(objectives, hint)

    while True:
        try:
            prompt = f"{CURRENT_DIR}> "
            user_input = input(prompt).strip().lower()
            parts = user_input.split()
            cmd = parts[0] if parts else ""
            arg = parts[1] if len(parts) > 1 else ""

            common = generic_cmd_handler(cmd, arg)
            if common == "EXIT": return False
            if common: continue

            # Level 4 Specific Logic (Networking)
            if cmd == "ping":
                if arg == TARGET_IP:
                    print(f"\nPinging {TARGET_IP}...")
                    print(f"Reply from {TARGET_IP}: bytes=32 time=5ms TTL=64")
                    print("Ping statistics: Sent = 4, Received = 4, Lost = 0 (0% loss)\n")
                else:
                    print(f"Host {arg} unreachable.")
            
            elif cmd == "tracert":
                if arg == TARGET_IP:
                    print(f"\nTracing route to {TARGET_IP}...")
                    print(" 1    <1 ms    <1 ms    <1 ms  192.168.1.1")
                    print(f" 2   10 ms    10 ms    11 ms  {TARGET_IP}")
                    print("Trace complete.")
                else:
                    print("Unable to resolve target.")

            elif cmd == "netstat":
                # Win condition is using netstat -an to find the service
                if "-an" in user_input:
                    print("\nActive Connections:")
                    print("  Proto  Local Address          Foreign Address        State")
                    print(f"  TCP    127.0.0.1:23           0.0.0.0:0              LISTENING")
                    print(f"  TCP    127.0.0.1:{SERVICE_PORT}         {TARGET_IP}:{SERVICE_PORT}          ESTABLISHED") # <-- Target found
                    print("  TCP    192.168.1.100:443      68.12.34.56:80         TIME_WAIT")
                    
                    time.sleep(1)
                    print_success(f"Hidden service found established on port {SERVICE_PORT}! Level 4 Complete.")
                    return True
                else:
                    print("Use 'netstat -an' to view all active connections.")

            elif cmd == "curl":
                print("curl: Command not implemented in this simulator.")

            else:
                print(f"'{cmd}' is not recognized.")

        except KeyboardInterrupt:
            return False
