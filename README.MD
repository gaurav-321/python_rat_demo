# Remote Control Python Script

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)

This Python script provides functionalities for remote control and monitoring of systems. It includes features for keylogging, remote command execution, file transfer, and more.

Please note that this script should be used responsibly and only within legal and ethical boundaries. Unauthorized use of this script may violate privacy and security standards.

## Features

- Keylogging: Capture and log key presses on the target system.
- Remote Command Execution: Execute command-line commands on the target system remotely.
- File Transfer: Upload and download files to/from the target system.
- Screenshot Capture: Capture screenshots from the target system.
- Keylogger Email Reporting: Start and stop a keylogger and send captured logs via email.

## Prerequisites

- Python 3.x
- Required Python packages: `smtplib`, `socket`, `subprocess`, `threading`, `PIL`, `win32con`, `win32gui`, `pynput`

## Usage

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/your-username/remote-control-python.git

2. Navigate to the repository directory.
    ```bash
    cd remote-control-python
3. Modify the script's configuration:

    Set the SERVER_HOST and SERVER_PORT variables to match your server's IP address and port.
    
    Configure email settings (if using keylogger email reporting).
    
4. Run the server script on your control machine:

    ```bash
    python server.py
5. Run the client script on the target machine:
    ```bash 
    python client.py
Follow the commands provided by the server script to control the target system remotely.
## Disclaimer
This script is provided for educational and research purposes only. The author is not responsible for any misuse, damage, or legal consequences resulting from the use of this script. Use at your own risk.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
