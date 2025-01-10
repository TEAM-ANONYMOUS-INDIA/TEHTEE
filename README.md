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

Features:

