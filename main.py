#!/usr/bin/python3
import argparse
import json
import requests
import ipaddress
from tabulate import tabulate

shodan_url = "https://internetdb.shodan.io/"

parser = argparse.ArgumentParser(description='Python script to get information about IP-addresses from Shodan.io')


def run_ip_list(ip_list, export):
    try:
        with open(ip_list, 'r') as file:
            lines = ip_list.readlines()
        lines = [line.strip() for line in lines]
        print(lines)
    except Exception as e:
        print(e)


def check_ip_adres(ip_str):
    return ipaddress.ip_address(ip_str)


def check_ip_private(ip_str):
    return ipaddress.ip_address(ip_str).is_private


def run_ip(ip_str, export):
    if check_ip_adres(ip_str):
        if not check_ip_private(ip_str):
            r = requests.get(shodan_url + ip_str)
            data = json.loads(r.text)
            build_table(data)
            check_export(export)
        else:
            print(f"Enter a valid external IP-address.\nThe IP-address {ip_str} is in the range of A, B and "
                  f"C-networks and are considered private")
    else:
        print("Enter a valid IP-address. Examples 15.86.189.44, 2001:0db8:85a3:0000:0000:8a2e:0370:7334")


def check_export(export):
    if export == "txt":
        export_text()
    elif export == "md":
        export_markdown()
    elif export == "csv":
        export_csv()
    elif export == "pdf":
        export_pdf()
    else:
        pass


def build_table(data):
    platte_dict = flatten_dict(data)
    tabel_data = [[key, str(value)] for key, value in platte_dict.items()]
    print(tabulate(tabel_data, headers=["Key", "Value"], tablefmt="grid"))


def export_text():
    print("export to text")


def export_markdown():
    pass


def export_csv():
    pass


def export_pdf():
    pass


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
parser.add_argument("-ip", help="Add manual IP-addresses")
parser.add_argument("-l", "--list", help="Run a list of IP-addresses")
parser.add_argument("-e", "--export", choices=['txt', 'md', 'csv', 'pdf'], help='Export to various formats Text, '
                                                                                'Markdown, CSV, PDF')

args = parser.parse_args()

if args.ip:
    ip_str = args.ip
    export = args.export
    run_ip(ip_str, export)
elif args.list:
    ip_list = args.list
    export = args.export
    run_ip_list(ip_list, export)
else:
    parser.print_help()
