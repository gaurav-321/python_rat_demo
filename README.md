# Keylogger and System Monitoring Tools

## Summary of Python Files

1. **keylogger.py**
   - **Purpose**: Captures keyboard input.
   - **Dependencies**: `pynput.keyboard`
   - **Output**: Logs keystrokes to a file.

2. **mouse_logger.py**
   - **Purpose**: Captures mouse movements and clicks.
   - **Dependencies**: `pynput.mouse`, `tkinter`
   - **Output**: Logs mouse events (position, clicks) to a file.

3. **screenshot.py**
   - **Purpose**: Takes screenshots of the screen.
   - **Dependencies**: `Pillow`, `pyautogui`
   - **Output**: Saves screenshot images.

4. **video_recorder.py**
   - **Purpose**: Records the screen and audio.
   - **Dependencies**: `mss`, `sounddevice`, `scipy.io.wavfile`
   - **Output**: Saves video and audio recordings.

5. **webcam_capture.py**
   - **Purpose**: Captures frames from a webcam.
   - **Dependencies**: `opencv-python`
   - **Output**: Saves frames as images or videos.

6. **clipboard_monitor.py**
   - **Purpose**: Monitors clipboard changes.
   - **Dependencies**: `pyperclip`
   - **Output**: Logs clipboard content to a file.

7. **system_info.py**
   - **Purpose**: Retrieves system information.
   - **Dependencies**: `platform`, `psutil`
   - **Output**: Prints system details (OS, CPU, memory).

8. **file_browser.py**
   - **Purpose**: Browses and lists files in a directory.
   - **Dependencies**: `os`, `shutil`
   - **Output**: Lists file paths.

9. **network_sniffer.py**
   - **Purpose**: Captures network traffic.
   - **Dependencies**: `scapy`
   - **Output**: Logs network packets to a file.

10. **process_monitor.py**
    - **Purpose**: Monitors running processes.
    - **Dependencies**: `psutil`
    - **Output**: Lists process details (PID, name).

## Features

- Captures keyboard and mouse events
- Screenshots the screen
- Records video and audio
- Captures webcam footage
- Monitors clipboard changes
- Retrieves system information
- Lists files in directories
- Captures network traffic
- Monitors running processes

## Installation

To use these scripts, you need to have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install pynput Pillow pyautogui mss sounddevice scipy opencv-python pyperclip platform psutil scapy
```

## Usage

Each script is designed to perform a specific task. Here’s how you can run them:

1. **keylogger.py**
   ```bash
   python keylogger.py
   ```

2. **mouse_logger.py**
   ```bash
   python mouse_logger.py
   ```

3. **screenshot.py**
   ```bash
   python screenshot.py
   ```

4. **video_recorder.py**
   ```bash
   python video_recorder.py
   ```

5. **webcam_capture.py**
   ```bash
   python webcam_capture.py
   ```

6. **clipboard_monitor.py**
   ```bash
   python clipboard_monitor.py
   ```

7. **system_info.py**
   ```bash
   python system_info.py
   ```

8. **file_browser.py**
   ```bash
   python file_browser.py
   ```

9. **network_sniffer.py**
   ```bash
   python network_sniffer.py
   ```

10. **process_monitor.py**
    ```bash
    python process_monitor.py
    ```

## Security Considerations

Each script is designed to perform a specific task that could be useful for system monitoring, automation, or malicious purposes. To use these scripts safely:

1. **Understand the Purpose**: Ensure you understand what each script does before running it.
2. **Limit Privileges**: Run scripts with minimal privileges to reduce potential damage.
3. **Monitor Activity**: Keep an eye on the output and behavior of the scripts while they are running.
4. **Remove or Disable**: After use, remove or disable the scripts to prevent unauthorized access.

## Conclusion

These Python scripts provide a range of functionalities for system monitoring and automation. Each script is designed with specific dependencies and outputs, making them useful for various purposes. However, it's crucial to use these scripts responsibly and within legal boundaries.