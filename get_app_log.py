import requests
import json

RPC_URL = "http://localhost:50012"

def get_app_log(tx_hash: str):
    payload = {
        "jsonrpc": "2.0",
        "method": "getapplicationlog",
        "params": [tx_hash],
        "id": 1
    }
    r = requests.post(RPC_URL, json=payload)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    tx_hash = "0x783331b8382705289e00fa7f2c77d54f8fabb52aff76728ce28e830f204c9d00"
    log = get_app_log(tx_hash)
    print(json.dumps(log, indent=2))