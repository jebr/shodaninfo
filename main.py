#!/usr/bin/python3
import argparse
import json
import requests
import ipaddress
from tabulate import tabulate

shodan_url = "https://internetdb.shodan.io/"

parser = argparse.ArgumentParser(description='Python script to get information about IP-addresses from Shodan.io')


def get_ip_list(ip_list):
    try:
        with open(ip_list, 'r') as file:
            lines = ip_list.readlines()
        lines = [line.strip() for line in lines]
    except Exception as e:
        print(e)


def check_ip_adres(ip_str):
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False


def run_ip(ip_address):
    if check_ip_adres(ip_address):
        r = requests.get(shodan_url + ip_address)
        data = json.loads(r.text)
        platte_dict = flatten_dict(data)
        tabel_data = [[key, str(value)] for key, value in platte_dict.items()]
        print(tabulate(tabel_data, headers=["Key", "Value"], tablefmt="grid"))
    else:
        print("Input a valid IP-address. Examples 15.86.189.44, 2001:0db8:85a3:0000:0000:8a2e:0370:7334")


def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


# Optional arguments
parser.add_argument("--ip", help="Run a singe IP-address")
parser.add_argument("--list", help="Run a list trough Shodan.io")

args = parser.parse_args()

if args.ip:

    ip_address = args.ip
    run_ip(ip_address)
# elif args.list:
#     get_ip_list()
else:
    parser.print_help()
