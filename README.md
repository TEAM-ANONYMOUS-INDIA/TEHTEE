Here is the updated README.md file with the image centered at the top, GitHub details included, and a stylish presentation of the full tutorial:

# Web Application Security Tools - Penetration Testing

<p align="center">
  <a href="https://ibb.co/7Q0QXS9">
    <img src="https://i.ibb.co/MfJfsgX/Screenshot-20250111-000245-Termux.jpg" alt="Screenshot-20250111-000245-Termux" border="0">
  </a>
</p>

Welcome to the **Web Application Security Tools** repository! This collection of tools is designed to help with penetration testing and vulnerability scanning of web applications. It includes a variety of tools that focus on different aspects of web security, such as WAF bypass, XSS testing, SQL injection, and directory brute-forcing.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Tools Overview](#tools-overview)
  - [WAF Bypass Tester](#waf-bypass-tester)
  - [XSS Vulnerability Scanner](#xss-vulnerability-scanner)
  - [Web Directory Brute Forcer](#web-directory-brute-forcer)
  - [Blind SQL Injection Tester (Time-Based)](#blind-sql-injection-tester-time-based)
  - [Open Redirect Detector](#open-redirect-detector)
  - [URL Shortener Resolver](#url-shortener-resolver)
- [Usage](#usage)
- [Important Notes](#important-notes)
- [Disclaimer](#disclaimer)
- [GitHub Repository](#github-repository)

## Introduction

This script contains a collection of tools aimed at assessing the security of web applications. It is **intended for ethical penetration testing** with **explicit permission**. These tools help to identify common vulnerabilities in web applications such as **WAF bypass**, **XSS**, **SQL injection**, **open redirects**, and more.

**Note**: Always obtain **explicit authorization** from the website or web application owner before performing any penetration testing.

## Installation

To use these tools, follow these steps:

1. **Clone the repository** (if applicable) or simply download the Python script.

   ```bash
   git clone https://github.com/TEAM-ANONYMOUS-INDIA/TEHTEE.git
   cd TEHTEE
   python3 TEHTEE.py

2. Install the required dependencies:

This project requires requests and colorama libraries for HTTP requests and colorful console output.

pip install requests colorama



Tools Overview

WAF Bypass Tester

This tool attempts to bypass Web Application Firewalls (WAF) by injecting various payloads into URL parameters.

Features:

Tries multiple payloads to see if the WAF allows any of them through.

Can be used to assess the robustness of WAF defenses.


XSS Vulnerability Scanner

This tool detects Cross-Site Scripting (XSS) vulnerabilities in web applications by injecting common XSS payloads.

Features:

Tests for reflected XSS, stored XSS, and DOM-based XSS.

Supports advanced payloads like image-based XSS and JavaScript-based XSS.


Web Directory Brute Forcer

This tool attempts to discover hidden directories and files on a web server by brute-forcing common directory names.

Features:

Uses a wordlist of common directory names such as admin, login, backup, and more.

Helps identify sensitive directories that could lead to security issues.


Blind SQL Injection Tester (Time-Based)

This tool is designed to detect Blind SQL Injection vulnerabilities using time-based payloads.

### Features:

Tries time-based SQL injection payloads to check if the server delays responses based on the injected queries.


Open Redirect Detector

This tool detects Open Redirect vulnerabilities by injecting potential redirect URLs into parameters.

### Features:

Tests if an application redirects users to malicious external websites.


URL Shortener Resolver

This tool resolves shortened URLs to their destination, helping to identify potential redirects to malicious websites.

### Features:

Resolves shortened URLs and checks for open redirects.


# Usage

Once you have the script installed, you can run it by executing the Python file in your terminal.

Running the Script:

#### python3 TEHTEE.py

When the script starts, you'll be presented with the following menu:

## Choose a tool to run:
1. Web Application Firewall (WAF) Bypass Tester
2. XSS Vulnerability Scanner
3. Web Directory Brute Forcer
4. Blind SQL Injection Tester (Time-Based)
5. Open Redirect Detector
6. URL Shortener Resolver
0. Exit

Select a Tool:

Enter the number of the tool you want to run.

For each tool, the script will ask you to enter the target URL or any relevant input needed for the attack.


# Example:

Enter the URL to test for XSS: http://example.com

The script will then attempt to find vulnerabilities based on the selected tool.

Example of How to Use

### $ python3 TEHTEE.py

Choose a tool to run:
1. Web Application Firewall (WAF) Bypass Tester
2. XSS Vulnerability Scanner
3. Web Directory Brute Forcer
4. Blind SQL Injection Tester (Time-Based)
5. Open Redirect Detector
6. URL Shortener Resolver
0. Exit
> 2  # XSS Vulnerability Scanner

Enter the URL to test for XSS: http://example.com
Testing for XSS vulnerabilities on http://example.com...

[INFO] Testing for reflected XSS...
[INFO] Testing for stored XSS...
[INFO] Testing for DOM-based XSS...

Important Notes:

Ensure that you have explicit permission to test the website or web application.

These tools are designed for educational purposes and should only be used in a legal and ethical manner.

The script is not foolproof and might not catch all vulnerabilities, so it should be used alongside other security tools.


#### Disclaimer

TEAM ANONYMOUS INDIA and contributors are not responsible for any misuse of this tool. Use these tools responsibly and ensure you have proper authorization before testing any website or web application. Unauthorized access to computer systems is illegal and unethical.

By using these tools, you agree to follow all applicable laws and regulations.

GitHub Repository

You can find the source code and further updates at our official GitHub repository:

TEHTEE - Web Application Security Tools


---

Made by TEAM ANONYMOUS INDIA
