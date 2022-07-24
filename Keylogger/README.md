# Windows Keylogger

1. Required Installation (Run as admin):
   ```
   pip install pynput pyinstaller 
   ```

2. logger.py (Main file to run keylogger). This starts the keylogger process:
   ```
   python logger.py
   ```

3. You can convert .py to .exe using the command:
   ```
   pyinstaller logger.py --onefile --noconsole
   ```


