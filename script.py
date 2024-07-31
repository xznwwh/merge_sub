import requests
import base64
import json

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

def encode_base64(content):
    try:
        encoded_bytes = base64.b64encode(content.encode('utf-8'))
        encoded_str = encoded_bytes.decode('utf-8')
        return encoded_str
    except Exception as e:
        print(f"Failed to encode Base64: {e}")
        return ""

def replace_content(content):
    content = content.replace("Github搜索TrojanLinks", "由盒子在互联网上收集")
    content = content.replace("😈github.com/Ruk1ng001", "由盒子在互联网上收集")
    return content

def filter_vmess_nodes(content):
    lines = content.splitlines()
    filtered_lines = [line for line in lines if 'vmess://' in line]
    return filtered_lines

def decode_vmess_nodes(nodes):
    decoded_nodes = []
    for node in nodes:
        if node.startswith('vmess://'):
            encoded_str = node[8:]
            decoded_str = decode_base64(encoded_str)
            decoded_nodes.append(decoded_str)
    return decoded_nodes

def encode_vmess_nodes(nodes):
    encoded_nodes = []
    for node in nodes:
        encoded_str = encode_base64(node)
        encoded_nodes.append(f'vmess://{encoded_str}')
    return encoded_nodes

def main():
    url1 = 'https://raw.githubusercontent.com/Huibq/TrojanLinks/master/links/trojan'
    url2 = 'https://raw.githubusercontent.com/Ruk1ng001/freeSub/main/v2ray'

    # Fetch content from both URLs
    content1 = fetch_subscription(url1)
    content2 = fetch_subscription(url2)

    # Decode Base64 encoded Trojan nodes
    decoded_trojan_content = decode_base64(content1)

    # Filter and decode V2Ray nodes
    filtered_vmess_nodes = filter_vmess_nodes(content2)
    decoded_vmess_nodes = decode_vmess_nodes(filtered_vmess_nodes)

    # Replace specified strings in the contents
    replaced_trojan_content = replace_content(decoded_trojan_content)
    replaced_vmess_nodes = [replace_content(node) for node in decoded_vmess_nodes]

    # Re-encode V2Ray nodes to Base64
    encoded_vmess_nodes = encode_vmess_nodes(replaced_vmess_nodes)

    # Combine nodes
    combined_nodes = replaced_trojan_content.splitlines() + encoded_vmess_nodes

    # Write combined nodes to file
    with open('combined_subscription.txt', 'w') as f:
        for node in combined_nodes:
            f.write(node + '\n')

    # Print combined nodes for debugging
    print(f"Combined nodes: {combined_nodes}")

if __name__ == '__main__':
    main()
