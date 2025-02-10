import requests

def lookup_ip(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"  # API URL to get IP info
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        print(f"IP Address: {data['ip']}")
        print(f"Location: {data['city']}, {data['region']}, {data['country']}")
        print(f"Org: {data['org']}")
        
        # Check if 'hostname' key exists in the response data
        if 'hostname' in data:
            print(f"Hostname: {data['hostname']}")
        else:
            print("Hostname: Not available")
    else:
        print("Could not retrieve information for this IP address.")

if __name__ == "__main__":
    ip = input("Enter the IP address to lookup: ")
    lookup_ip(ip)
