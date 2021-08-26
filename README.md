## SendData

Little Python 3 script to run the [AdvScanner](https://github.com/BLE-LAN/AdvScanner) and 
send the output to the  [ListADV](https://github.com/BLE-LAN/ListADV) web.

## Dependencies

* requests

## Usage

The AdvScanner out path is the same that de .exe, by default the filename is 'adv_list.txt'.

````
positional arguments:
  jwt                   token needed to api auth

optional arguments:
  -h, --help            show this help message and exit
  --scanner SCANNER, -s SCANNER
                        AdvScanner path
  --scantime SCANTIME, -st SCANTIME
                        time to scan in seconds
````






