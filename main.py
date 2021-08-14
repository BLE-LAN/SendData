import subprocess
import argparse
import requests
import json


_URL = ''


def parse_args():
    parser = argparse.ArgumentParser(description='Run the ADV Scanner and send the output to the ListADV web')
    parser.add_argument(
        'jwt', type=str, help="token to ",
    )
    parser.add_argument(
        '--scanner', '-s', type=str, help="AdvScanner path", default='.\\AdvScanner.exe'
    )
    parser.add_argument(
        '--scantime', '-st', type=int, help="time to scan in milliseconds", default=(40*1000)
    )
    return parser.parse_args()


def run_scanner(scanner_path, scan_time, ouput_path):
    return subprocess.run([scanner_path, '-s', str(scan_time), '-o', ouput_path])#, stdout=subprocess.DEVNULL)


def adv_file_to_json(adv_path):

    json_str = '{"devices": ['

    with open(adv_path) as f:
        for line in f:
            json_str += line[:-1] + ', '

    return json.loads(json_str[:-2] + ']}')


def api_add(jwt, body):
    headers = {
        'Authorization': 'Bearer ' + jwt
    }
    r = requests.post(_URL, json=body, headers=headers)

    return r.status_code


if __name__ == '__main__':
    args = parse_args()

    path_partitions = args.scanner.rpartition("\\")
    adv_file_path = path_partitions[0] + "\\ble.txt"

    run_scanner(args.scanner, args.scantime, adv_file_path)

    adv_json = adv_file_to_json(adv_file_path)

    api_add(args.jwt, adv_json)
