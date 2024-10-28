KAEZAL (Social Engineering Toolkit) Documentation
Overview

KAEZAL is a Python-based GUI application designed for cybersecurity research and ethical hacking. It provides five powerful tools aimed at:

    Simulating phishing attacks
    Testing security vulnerabilities
    Training professionals in penetration testing

The toolkit leverages Python libraries like Flask and Tkinter for a seamless user interface and integrates technologies such as Ngrok, Cloudflared, Servio, LocalXpose, PHP, and Linux to create a robust and scalable solution.
Tools and Features
1. Camphisher

Camphisher captures webcam shots from a target by using phishing techniques to gain webcam access. Here’s how it works:

    Objective: Capture snapshots through a phishing page.
    Process:
        A phishing page prompts the target for webcam access.
        Upon approval, the snapshots are captured and transmitted back to the researcher.
    Technologies Used: Flask for backend communication, Python libraries for data handling.

2. Phisher

Phisher is the primary tool for credential harvesting through phishing pages. Key details include:

    Objective: Capture sensitive credentials like usernames and passwords.
    Process:
        Realistic-looking phishing pages are hosted locally.
        Targets are lured into entering credentials.
        Captured data is securely stored for analysis.
    Technologies Used: Flask for hosting, Ngrok/Cloudflared for web exposure.

3. FindUser

FindUser identifies a target's geographical location using captured IP addresses. Here's a breakdown:

    Objective: Determine the target’s exact location.
    Process:
        IP addresses are captured through interaction with phishing pages.
        Python libraries track location and present the details to the researcher.
    Technologies Used: PHP for backend processing, Python for IP tracking.

4. QR Code Attack

QR Code Attack uses QR codes for a targeted phishing approach. Details include:

    Objective: Create QR codes linking to phishing pages for mobile devices.
    Process:
        QR codes are generated linking to pre-configured phishing pages.
        Targets scan the code and are redirected to the phishing site.
    Technologies Used: Python libraries for QR code generation, Flask for backend.

5. URL Masking Tool

The URL Masking Tool cloaks phishing page URLs to enhance credibility. Key aspects are:

    Objective: Make phishing links look more trustworthy.
    Process:
        Original phishing URLs are masked.
        The tool presents a convincing URL, increasing the likelihood of interaction.
    Technologies Used: Flask for URL generation, LocalXpose/Servio for web exposure.

Technologies and Development Tools
Core Technologies

    Python: The primary programming language.
    Flask: Backend server management for handling web pages.
    Tkinter: GUI creation and user interface management.

Networking Tools

    Ngrok: Tunneling tool for exposing local servers to the web.
    Cloudflared: Alternative tunneling service for secure connections.
    Servio/LocalXpose: Local web hosting tools for remote testing.

Backend Tools

    PHP: Used for data processing and handling.
    Linux: Preferred OS for stability and security during deployment.

Ethical Use and Security

This toolkit is strictly for ethical hacking and cybersecurity research. It helps professionals:

    Understand potential vulnerabilities
    Train in a controlled and secure environment

Legal Notice: Always obtain explicit permission before conducting tests. Unauthorized use may lead to legal consequences.
Installation and Setup

    Requirements
        Python 3.x
        Flask library
        Tkinter (built-in with Python)
        Ngrok/Cloudflared/LocalXpose
        PHP
        Linux environment (recommended)

    Installation Steps
        Install Python and necessary libraries:

        bash

sudo apt-get install python3 python3-pip
pip install flask

Set up tunneling tools:

    Ngrok: Download Ngrok
    Cloudflared: Install via terminal using:

    bash

        sudo apt install cloudflared

Running the Application

    Clone the repository:

    bash

git clone <repository-url>

Launch the GUI:

bash

        python3 KAEZAL.py

        Choose the tool from the GUI and follow on-screen instructions.

User Guide
Launching the Tools

    Open the GUI.
    Select the desired tool from the menu:
        Camphisher: Initiates webcam capture.
        Phisher: Starts a phishing page to capture credentials.
        FindUser: Tracks location using the captured IP.
        QR Code Attack: Generates a phishing QR code.
        URL Masking Tool: Masks a URL for phishing.

Using the Tools

    Camphisher: Follow prompts to send a phishing link to the target.
    Phisher: Monitor the backend for captured data.
    FindUser: View location results in the interface.
    QR Code Attack: Distribute the QR code to the target.
    URL Masking Tool: Generate and test the masked URL.
