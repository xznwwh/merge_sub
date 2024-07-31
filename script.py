import requests

def fetch_subscription(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def filter_trojan_nodes(content):
    lines = content.splitlines()
    filtered_lines = [line for line in lines if 'trojan://' in line]
    return filtered_lines

def filter_vmess_nodes(content):
    lines = content.splitlines()
    filtered_lines = [line for line in lines if 'vmess://' in line]
    return filtered_lines

def main():
    url1 = 'https://raw.githubusercontent.com/Huibq/TrojanLinks/master/links/trojan'
    url2 = 'https://raw.githubusercontent.com/Ruk1ng001/freeSub/main/v2ray'

    content1 = fetch_subscription(url1)
    content2 = fetch_subscription(url2)

    print(f"Content from {url1}:\n{content1}")
    print(f"Content from {url2}:\n{content2}")

    filtered_trojan_nodes = filter_trojan_nodes(content1)
    filtered_vmess_nodes = filter_vmess_nodes(content2)

    print(f"Filtered trojan nodes from {url1}: {filtered_trojan_nodes}")
    print(f"Filtered vmess nodes from {url2}: {filtered_vmess_nodes}")

    combined_nodes = filtered_trojan_nodes + filtered_vmess_nodes

    with open('combined_subscription.txt', 'w') as f:
        for node in combined_nodes:
            f.write(node + '\n')

    print(f"Combined nodes: {combined_nodes}")

if __name__ == '__main__':
    main()
