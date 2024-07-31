import requests

def fetch_subscription(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def filter_nodes(content):
    lines = content.splitlines()
    filtered_lines = [line for line in lines if '://' in line and 'port' not in line]
    return filtered_lines

def main():
    url1 = 'https://raw.staticdn.net/Huibq/TrojanLinks/master/links/trojan'
    url2 = 'https://raw.githubusercontent.com/Ruk1ng001/freeSub/main/v2ray'

    content1 = fetch_subscription(url1)
    content2 = fetch_subscription(url2)

    filtered_nodes1 = filter_nodes(content1)
    filtered_nodes2 = filter_nodes(content2)

    combined_nodes = filtered_nodes1 + filtered_nodes2

    with open('combined_subscription.txt', 'w') as f:
        for node in combined_nodes:
            f.write(node + '\n')

if __name__ == '__main__':
    main()
