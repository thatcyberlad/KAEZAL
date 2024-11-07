                                    ![Screenshot 2024-10-28 140931](https://github.com/user-attachments/assets/4199ded4-c188-4ba4-92b6-374cc3fba1ca)

KAEZAL: A Social Engineering Toolkit

KAEZAL is a Python-based Linux toolkit developed for cybersecurity research and ethical hacking. Designed for educational and ethical penetration testing, KAEZAL offers six powerful tools that allow users to:

    Simulate phishing attacks
    Test security vulnerabilities
    Train professionals in penetration testing techniques

The toolkit integrates popular technologies such as Ngrok, Cloudflared, Servio, LocalXpose, PHP, and Linux, creating a robust and scalable security solution.
Tools and Features
1. Camphisher

Camphisher is a tool for capturing webcam images from targets using phishing tactics.

    Objective: Capture webcam snapshots through a phishing page.
    Process:
        Sends a phishing page prompting the target for webcam access.
        Captures and transmits images back to the researcher upon approval.
    Technologies Used: Flask for backend communication, Python libraries for data handling.

2. Phisher

Phisher focuses on credential harvesting via phishing pages.

    Objective: Capture sensitive information like usernames and passwords.
    Process:
        Hosts realistic-looking phishing pages locally.
        Collects entered credentials securely for analysis.
    Technologies Used: Flask for hosting, Ngrok/Cloudflared for web exposure.

3. FindUser

FindUser identifies a target's geographical location based on IP address.

    Objective: Pinpoint the target’s location using IP.
    Process:
        Collects IP addresses through phishing page interactions.
        Tracks location using Python libraries, presenting details to the researcher.
    Technologies Used: PHP for backend, Python for IP tracking.

4. QR Code Attack

QR Code Attack targets mobile devices by directing users to phishing pages via QR codes.

    Objective: Generate phishing QR codes for mobile phishing.
    Process:
        Creates QR codes linking to configured phishing pages.
        Redirects scanned users to phishing sites.
    Technologies Used: Python libraries for QR code generation, Flask for backend.

5. URL Masking Tool

URL Masking Tool cloaks phishing links to increase trustworthiness.

    Objective: Make phishing URLs look more credible.
    Process:
        Masks original URLs to appear legitimate.
    Technologies Used: Flask for URL generation, LocalXpose/Servio for web exposure.

6. Backdoor Injection Tool

Backdoor Injection Tool embeds remote access trojans into common file formats (JPG, PDF, DOCX).

    Objective: Embed backdoors into popular file formats for remote access.
    Technologies Used: Python for backdoor injection and manipulation.

Technologies and Development Tools

Core Technologies

    Python: Primary programming language.
    PHP: Backend server management.

Networking Tools

    Ngrok: Exposes local servers to the web.
    Cloudflared: Alternative tunneling for secure connections.
    Servio/LocalXpose: Local web hosting for remote access.

Backend Tools

    PHP: Data processing and handling.
    Linux: Recommended OS for stability and security.

Ethical Use and Security

This toolkit is intended strictly for ethical hacking and cybersecurity research. KAEZAL supports professionals in understanding vulnerabilities in a safe and controlled environment.

Legal Notice: Obtain explicit permission before conducting tests. Unauthorized use is illegal and may lead to severe consequences.
Installation and Setup

Requirements

    Python 3.x
    Flask library
    Tkinter (built-in with Python)
    Ngrok, Cloudflared, LocalXpose
    PHP
    Linux environment (recommended)

Installation Steps

    Install Python and necessary libraries:

sudo apt-get install python3 python3-pip
pip install flask

Set up tunneling tools:

    Ngrok: Download and install Ngrok
    Cloudflared: Install via terminal:

    sudo apt install cloudflared

Clone the repository:

git clone <repository-url>

Launch the GUI:

    python3 KAEZAL.py

User Guide

Launching Tools

    Select the desired tool from the GUI:
        Camphisher: Initiates webcam capture.
        Phisher: Starts a phishing page to capture credentials.
        FindUser: Tracks location using captured IP.
        QR Code Attack: Generates phishing QR codes.
        URL Masking Tool: Masks phishing URLs for credibility.
        Backdoor Injection Tool: Embeds backdoors into files.

Using the Tools

    Camphisher: Follow prompts to send a phishing link to the target.
    Phisher: Monitor the backend for captured data.
    FindUser: View location results in the interface.
    QR Code Attack: Distribute the QR code to the target.
    URL Masking Tool: Generate and test the masked URL.
    Backdoor Injection Tool: Embed backdoor in popular file formats.
