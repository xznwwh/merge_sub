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

def filter_trojan_nodes(content):
    lines = content.splitlines()
    filtered_lines = [line for line in lines if 'trojan://' in line]
    return filtered_lines

def decode_vmess_nodes(content):
    lines = content.splitlines()
    decoded_vmess_nodes = []
    for line in lines:
        if 'vmess://' in line:
            base64_content = line.replace('vmess://', '')
            decoded_str = decode_base64(base64_content)
            if decoded_str:
                try:
                    node_info = json.loads(decoded_str)
                    node_info_str = json.dumps(node_info, ensure_ascii=False)
                    decoded_vmess_nodes.append(node_info_str)
                except json.JSONDecodeError as e:
                    print(f"Failed to parse JSON: {e}")
    return decoded_vmess_nodes

def replace_content(content):
    content = content.replace("Github搜索TrojanLinks", "由盒子在互联网上收集")
    content = content.replace("😈github.com/Ruk1ng001", "由盒子在互联网上收集")
    return content

def main():
    url1 = 'https://raw.githubusercontent.com/Huibq/TrojanLinks/master/links/trojan'
    url2 = 'https://raw.githubusercontent.com/Ruk1ng001/freeSub/main/v2ray'

    # Fetch content from both URLs
    content1 = fetch_subscription(url1)
    content2 = fetch_subscription(url2)

    # Decode Base64 encoded Trojan nodes
    decoded_trojan_content = decode_base64(content1)
    
    # Print contents for debugging
    print(f"Decoded Trojan content from {url1}:\n{decoded_trojan_content}")
    print(f"Content from {url2}:\n{content2}")

    # Replace specified strings in the Trojan content
    replaced_trojan_content = replace_content(decoded_trojan_content)

    # Decode and replace specified strings in the V2Ray content
    decoded_vmess_nodes = decode_vmess_nodes(content2)
    replaced_vmess_nodes = [replace_content(node) for node in decoded_vmess_nodes]

    # Combine nodes
    combined_nodes = replaced_trojan_content.splitlines() + replaced_vmess_nodes

    # Write combined nodes to file
    with open('combined_subscription.txt', 'w') as f:
        for node in combined_nodes:
            f.write(node + '\n')

    # Print combined nodes for debugging
    print(f"Combined nodes: {combined_nodes}")

if __name__ == '__main__':
    main()
