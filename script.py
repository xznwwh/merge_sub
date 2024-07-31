import requests
import base64

def fetch_subscription(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def decode_base64(content):
    try:
        decoded_bytes = base64.b64decode(content)
        decoded_str = decoded_bytes.decode('utf-8')
        return decoded_str
    except Exception as e:
        print(f"Failed to decode Base64: {e}")
        return ""

def filter_vmess_nodes(content):
    lines = content.splitlines()
    filtered_lines = [line for line in lines if 'vmess://' in line]
    return filtered_lines

def replace_strings(content, replacements):
    for old, new in replacements.items():
        content = content.replace(old, new)
    return content

def main():
    url1 = 'https://raw.githubusercontent.com/Huibq/TrojanLinks/master/links/trojan'
    url2 = 'https://raw.githubusercontent.com/Ruk1ng001/freeSub/main/v2ray'

    # Fetch content from both URLs
    content1 = fetch_subscription(url1)
    content2 = fetch_subscription(url2)

    # Decode Base64 encoded Trojan nodes
    decoded_trojan_content = decode_base64(content1)
    
    # Define replacements for Trojan and V2Ray nodes
    trojan_replacements = {
        'Github搜索TrojanLinks': ''
    }
    vmess_replacements = {
        '😈github.com/Ruk1ng001': '由盒子在互联网上收集'
    }

    # Replace strings in Trojan content
    replaced_trojan_content = replace_strings(decoded_trojan_content, trojan_replacements)
    
    # Replace strings in V2Ray content
    replaced_vmess_content = replace_strings(content2, vmess_replacements)

    # Print contents for debugging
    print(f"Replaced Trojan content:\n{replaced_trojan_content}")
    print(f"Replaced V2Ray content:\n{replaced_vmess_content}")

    # Filter V2Ray nodes
    filtered_vmess_nodes = filter_vmess_nodes(replaced_vmess_content)

    # Combine nodes
    combined_nodes = replaced_trojan_content.splitlines() + filtered_vmess_nodes

    # Write combined nodes to file
    with open('combined_subscription.txt', 'w') as f:
        for node in combined_nodes:
            f.write(node + '\n')

    # Print combined nodes for debugging
    print(f"Combined nodes: {combined_nodes}")

if __name__ == '__main__':
    main()
