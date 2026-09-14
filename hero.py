import os
import json

def show_disclaimer():
    print("\n" + "="*56)
    print("\033[1;31m                 [!] SECURITY & LEGAL DISCLAIMER\033[0m")
    print("="*56)
    print("\033[1;37m This tool is built strictly for local educational and testing purposes.")
    print(" It does not interact with official game servers, bypass bans globally,")
    print(" or hack any secure systems. Unauthorized use is prohibited.\033[0m")
    print("="*56)
    
    choice = input("\033[1;33m Do you agree to the terms and conditions? (y/n): \033[0m").strip().lower()
    if choice != 'y':
        print("\033[1;31m[-] Access denied. You must agree to proceed.\033[0m")
        exit()

def auth_system():
    print("\n" + "="*56)
    print("\033[1;35m               AUTHENTICATION PORTAL\033[0m")
    print("="*56)
    print(" \033[1;33m[1]\033[0m Register New Account")
    print(" \033[1;33m[2]\033[0m Login to Tool")
    print("="*56)
    
    auth_choice = input("\033[1;36m[?] Select an option (1-2): \033[0m").strip()
    
    if auth_choice == "1":
        print("\n--- [Registration] ---")
        username = input("Enter a new username: ").strip()
        password = input("Enter a new password: ").strip()
        
        credentials = {"username": username, "password": password}
        with open("user_auth.json", "w") as f:
            json.dump(credentials, f)
        
        print("\033[1;32m[+] Registration successful! Please login now.\033[0m")
        auth_system()
        
    elif auth_choice == "2":
        print("\n--- [Login] ---")
        if not os.path.exists("user_auth.json"):
            print("\033[1;31m[-] No registered account found! Please register first.\033[0m")
            auth_system()
            return
            
        with open("user_auth.json", "r") as f:
            saved_creds = json.load(f)
            
        input_user = input("Enter username: ").strip()
        input_pass = input("Enter password: ").strip()
        
        if input_user == saved_creds["username"] and input_pass == saved_creds["password"]:
            print("\033[1;32m[+] Login successful! Welcome to the main menu.\033[0m")
        else:
            print("\033[1;31m[-] Invalid credentials! Access denied.\033[0m")
            exit()
    else:
        print("\033[1;31m[-] Invalid choice. Exiting...\033[0m")
        exit()

def print_menu():
    print("\n" + "="*56)
    print("\033[1;35m        UNBAN TOOL (FREE FIRE ID CLONE V3)\033[0m")
    print("="*56)
    print(" \033[1;33m[1]\033[0m Paste Access Token")
    print(" \033[1;33m[2]\033[0m Unban Free Fire ID (Process & Generate Files)")
    print(" \033[1;33m[3]\033[0m Code Paste Error Fix (File)")
    print(" \033[1;33m[4]\033[0m Exit")
    print("="*56)

def main():
    show_disclaimer()
    auth_system()
    
    access_token = ""
    
    while True:
        print_menu()
        choice = input("\n\033[1;36m[?] Select an option (1-4): \033[0m").strip()
        
        if choice == "1":
            print("\n" + "-"*56)
            print("\033[1;32m--- [1] Access Token Setup ---\033[0m")
            print("-"*56)
            token_input = input("\033[1;37mEnter your Account Access Token (Google/Guest): \033[0m").strip()
            
            if token_input:
                confirm = input("\n\033[1;33m[?] Are you sure you want to save this token? (y/n): \033[0m").strip().lower()
                
                if confirm == 'y':
                    access_token = token_input
                    print("\n\033[1;32m[+] Success: Token saved securely in local memory!\033[0m")
                elif confirm == 'n':
                    print("\n\033[1;31m[-] Action Cancelled: Token was not saved. Returning to menu...\033[0m")
                else:
                    print("\n\033[1;31m[-] Invalid input. Operation aborted.\033[0m")
            else:
                print("\n\033[1;31m[-] Error: Token cannot be empty.\033[0m")
                
        elif choice == "2":
            print("\n" + "-"*56)
            print("\033[1;32m--- [2] Unban Free Fire ID (Processing) ---\033[0m")
            print("-"*56)
            if not access_token:
                print("\n\033[1;31m[-] Warning: No access token found! Please complete Option 1 first.\033[0m")
                continue
            
            print("\n\033[1;34m[*] Processing access token locally...\033[0m")
            print("\033[1;34m[*] Generating config files and codes...\033[0m")
            
            config_code = "{\n    \"status\": \"unban_test_active\",\n    \"token_ref\": \"" + access_token[:10] + "...\",\n    \"safe_mode\": true\n}"
            
            file_data = {
                "token": access_token,
                "config_code": config_code,
                "target": "FreeFireMax_Local"
            }
            
            download_path = "/storage/emulated/0/Download"
            
            try:
                if not os.path.exists(download_path):
                    os.makedirs(download_path, exist_ok=True)
                
                code_file_name = os.path.join(download_path, "ff_generated_code.txt")
                with open(code_file_name, "w") as f:
                    f.write(config_code)
                
                config_file_name = os.path.join(download_path, "local_config.json")
                with open(config_file_name, "w") as f:
                    json.dump(file_data, f, indent=4)
                
                print(f"\n\033[1;32m[+] Success! Files saved in Download Folder:\033[0m")
                print(f"    - Code File: \033[1;36m{code_file_name}\033[0m")
                print(f"    - Config File: \033[1;36m{config_file_name}\033[0m")
                
                print("\n" + "-"*56)
                print("\033[1;33m[!] INSTRUCTIONS & GUIDELINES:\033[0m")
                print("-"*56)
                print("1. Open 'ff_generated_code.txt' from Download folder and copy the code.")
                print("2. Open 'local_config.json', paste the copied code inside it, and save.")
                print("3. Move/Paste the final file to:")
                print("   \033[1;35mAndroid/data/com.dts.freefiremax/files/\033[0m")
                
                print("\n" + "="*56)
                print("\033[1;31m[!] DISCLAIMER:\033[0m")
                print("="*56)
                print("\033[1;37mThis tool is built strictly for local testing and learning purposes.")
                print("It cannot unban accounts from official game servers.")
                print("It only creates a visual local state/clone on your device.\033[0m")
                print("="*56)
                
            except Exception as e:
                print(f"\n\033[1;31m[-] Error generating files: {e}\033[0m")
                
        elif choice == "3":
            print("\n" + "-"*56)
            print("\033[1;32m--- [3] Code Paste Error Fix (File) ---\033[0m")
            print("-"*56)
            print("\n\033[1;33m[!] Why does paste error happen?\033[0m")
            print("\033[1;37mAndroid security restrictions on versions 11/12/13+ block third-party apps")
            print("from writing or pasting files directly into the 'Android/data/' folder (Access Denied).\033[0m")
            
            print("\n\033[1;32m[+] Step-by-Step Fix Guide:\033[0m")
            print("\033[1;37m1. Install \033[1;36mZArchiver\033[0m or \033[1;36mMiXplorer\033[0m and \033[1;36mShizuku\033[0m from the Play Store.")
            print("2. Enable 'Wireless Debugging' in your phone's Developer Options.")
            print("3. Pair and start the Shizuku service using wireless debugging.")
            print("4. Open your file manager app and grant it Shizuku root/system access permission.")
            print("5. Now navigate to Download, copy your config file, and paste it smoothly")
            print("   into \033[1;35mAndroid/data/com.dts.freefiremax/files/\033[0m without any errors.\033[0m")
            
        elif choice == "4":
            print("\n\033[1;32mExiting tool. Stay safe and secure!\033[0m")
            break
        else:
            print("\n\033[1;31m[-] Invalid choice. Please select between 1 to 4.\033[0m")

if __name__ == "__main__":
    main()
