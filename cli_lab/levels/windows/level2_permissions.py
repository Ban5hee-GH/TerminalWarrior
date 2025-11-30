# FILE: level2_permissions.py (REVISED)
import time
from .utils import (
    clear_screen,
    print_header,
    print_objectives,
    print_success,
    generic_cmd_handler,
    CURRENT_DIR,
)


def run_level():
    title = "LEVEL 2: PERMISSIONS & OWNERSHIP"
    objectives = [
        "The 'secret.txt' file is locked. Find a way to read it.",
        "You must reset ownership and view permissions to gain access."
    ]
    hint = "Try 'takeown /f secret.txt' then 'icacls secret.txt /grant User:(F)'"
    
    print_header(title)
    print_objectives(objectives, hint)

    permission_granted = False

    while True:
        try:
            prompt = f"{CURRENT_DIR}> "
            user_input = input(prompt).strip().lower()
            parts = user_input.split()
            cmd = parts[0] if parts else ""
            arg1 = parts[1] if len(parts) > 1 else ""
            
            # Check shared commands
            common = generic_cmd_handler(cmd, arg1)
            if common == "EXIT": return False
            if common: continue
            
            # Level 2 Specific Logic (Permissions)
            if cmd == "icacls" or cmd == "takeown" or cmd == "attrib":
                if "secret.txt" in user_input and not permission_granted:
                    print(f"Executing: {user_input}")
                    print("SUCCESS: File ownership and permissions updated for secret.txt.")
                    permission_granted = True
                else:
                    print("SYNTAX: Command executed. No further changes needed.")

            elif cmd == "type" or cmd == "cat":
                if arg1 == "secret.txt":
                    if permission_granted:
                        print("\n[CONTENT OF SECRET.TXT]")
                        print("-" * 30)
                        print("Next Challenge Clue: The key to Level 3 is in the system logs.")
                        print("-" * 30)
                        time.sleep(1)
                        print_success("Access Granted! Level 2 Complete.")
                        return True
                    else:
                        print("Access Denied: You do not have permission to view this file.")
                else:
                    print(f"The system cannot find the file specified: {arg1}")
            
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False
