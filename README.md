# SubEnum
## Day 0 [1 Jan 2022]
Basic python based subdomain bruteforce tool, part of Python for cybersecurity project.

## Requirements
>pip3 install requests

## Usage
```usage
usage: subenum.py -d <target.com> [options]

optional arguments:
  -h , --help       Show usage and help options
  -d , --domain     Target domain
  -w , --wordlist   Path to wordlist to bruteforce
  -o , --output     Filename to save. (Default: <subdomain>.txt)
  --about           Print about information
```

Linux:
>python3 subenum.py -d example.com -w subdomain.txt

Windows:
>python subenum.py -d example.com -w subdomain.txt

By default output will be saved as **example-com.txt**

Feel free to [open and issue](https://github.com/0xRyuk/SubEnum/issues) if you face bugs or errors in this tool.

## To do list
- [ ] Threading.

## Twitter [0xRyuk](https://twitter.com/0xRyuk)

Credits : subdomain.txt list from [SecLists](https://github.com/danielmiessler/SecLists)