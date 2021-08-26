import subprocess
import argparse
import requests
import json
from time import sleep


_URL_BASE = 'https://nyaboron.pythonanywhere.com/'

_OUTFILE_NAME = "\\adv_list.txt"

_ADD_URL = 'api/adddevices'


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
    return subprocess.run([scanner_path, '/scantime', str(scan_time), '/fileoutput', ouput_path], stdout=subprocess.DEVNULL)


def adv_file_to_json(adv_path):

    json_str = '{"devices": ['

    line_count = 0

    with open(adv_path) as f:
        for line in f:
            line_count += 1
            json_str += line[:-1] + ', '

    print('Number of Advertisements: ' + str(line_count))

    return json.loads(json_str[:-2] + ']}')


def api_add(jwt, body):
    headers = {
        'Authorization': 'Bearer ' + jwt
    }
    r = requests.post(_URL_BASE + _ADD_URL, json=body, headers=headers)

    print('Response status code: ' + str(r.status_code) + '\n')


if __name__ == '__main__':
    args = parse_args()

    path_partitions = args.scanner.rpartition("\\")
    adv_file_path = path_partitions[0] + _OUTFILE_NAME

    while 1:
        run_scanner(args.scanner, args.scantime, adv_file_path)
        adv_json = adv_file_to_json(adv_file_path)
        api_add(args.jwt, adv_json)
        sleep(10)
