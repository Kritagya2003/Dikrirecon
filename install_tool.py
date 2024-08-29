import os
import subprocess
import sys

def command_exists(command):
    """Check if a command exists on the system."""
    return subprocess.call(f"type {command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

def install_package(package_name, install_command):
    """Install a package if not already installed."""
    if not command_exists(package_name):
        print(f"[*] Installing {package_name}...")
        subprocess.call(install_command, shell=True)
    else:
        print(f"[*] {package_name} is already installed.")

def main():
    # Update package lists
    subprocess.call("sudo apt update", shell=True)

    # List of tools to install
    tools = [
        ("amass", "sudo apt install -y amass"),
        ("sublist3r", "sudo apt install -y sublist3r"),  # Adjust installation as needed
        ("subfinder", "GO111MODULE=on go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"),
        ("assetfinder", "GO111MODULE=on go install -v github.com/tomnomnom/assetfinder@latest"),
        ("findomain", "wget https://github.com/Findomain/Findomain/releases/latest/download/findomain-linux.zip -O findomain.zip && unzip findomain.zip && chmod +x findomain && sudo mv findomain /usr/local/bin/"),
        ("masscan", "sudo apt install -y masscan"),
        ("naabu", "GO111MODULE=on go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest"),
        ("whatweb", "sudo apt install -y whatweb"),
        ("nikto", "sudo apt install -y nikto"),
        ("zap", "sudo apt install -y zaproxy"),  # OWASP ZAP
        ("testssl.sh", "git clone --depth 1 https://github.com/drwetter/testssl.sh.git && cd testssl.sh && sudo ln -s $(pwd)/testssl.sh /usr/local/bin/testssl"),
        ("sslyze", "pip install sslyze"),
        ("gowitness", "GO111MODULE=on go install -v github.com/sensepost/gowitness@latest"),
        ("dnsenum", "sudo apt install -y dnsenum"),
        ("dnsrecon", "pip install dnsrecon"),
        ("gobuster", "GO111MODULE=on go install -v github.com/OJ/gobuster@latest"),
        ("ffuf", "GO111MODULE=on go install -v github.com/ffuf/ffuf@latest")
    ]

    # Install each tool
    for package_name, install_command in tools:
        install_package(package_name, install_command)

    # Additional Python tools
    print("[*] Installing Python tools via pip...")
    subprocess.call("pip install -r requirements.txt", shell=True)

    print("[*] All tools are installed and ready to use.")

if __name__ == "__main__":
    main()
