import requests
import sys
import os
import argparse
import platform

# Script color configuration and about.
colors = True
machine = sys.platform
checkplatform = platform.platform()
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False
if checkplatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
    colors = True
    os.system('')
if not colors:
    N = R = W = G = Y = run = bad = good = info = que = ''
else:
    N = '\033[0m'
    W = '\033[1;37m' 
    B = '\033[1;34m' 
    M = '\033[1;35m' 
    R = '\033[1;31m' 
    G = '\033[1;32m' 
    Y = '\033[1;33m' 
    C = '\033[1;36m' 
    underline = "\033[4m"
    back = '\033[7;91m'
    info = '\033[93m[!]\033[0m'
    que = '\033[94m[?]\033[0m'
    bad = '\033[91m[-]\033[0m'
    good = '\033[92m[+]\033[0m'
    run = '\033[97m[~]\033[0m'

epilog=f"""
{Y}Github: {underline}{C}https://www.github.com/0xRyuk{N}
{Y}Version: {R}1.0{N}
"""
about =M+f"""
+───────────────────────+
| {C}Project{N}   : {G}Sub-enum{N} {M} |
| {C}License{N}   : {B}GNU GPL v3{N}{M}|
| {C}Author{N}    : {R}0xRyuk{N}    {M}|
| {C}Twitter{N}   : {R}0xRyuk{N}    {M}|
+───────────────────────+
"""+N+epilog

banner = R+r"""Sub%s-%sEnum
%s
"""%(W,Y,G+'\t{v1.0}'+N)

# Input parsing as command line arguments 
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, usage='subenum.py -d <target.com> [options]', epilog=epilog, add_help=False)

parser.add_argument_group('Options')
parser.add_argument('-h ', '--help', action='store_true', help='Show usage and help options')
parser.add_argument('-d', '--domain', dest='domain', metavar='', help='Target domain')
parser.add_argument('-w', '--wordlist', dest='wordlist', metavar='', help='Path to wordlist to bruteforce')
parser.add_argument('-o','--output', dest='output', metavar='', help='Filename to save. (Default: <subdomain>.txt)', )
parser.add_argument('--about', action='store_true', help='Print about information')

args = parser.parse_args()

domain = args.domain
wordlist = args.wordlist

if not domain and not args.about:
    print(banner)
    parser.print_help()
    sys.exit()
if args.about:
    print(banner)
    print(about)
    sys.exit()
if not wordlist:
    print('Please provide a wordlist file.')
    sys.exit()


if not args.output:
    filename = domain.replace('.','-')
    output = f'{filename}.txt'

# Core section
subdomains = []
def bruteforcer(domain, wordlist, output):
    try:
        with open(wordlist) as wordlist:
            sub_keywords = wordlist.read().splitlines()
        scheme = 'http'
        for sub in sub_keywords:
            sub = sub.replace('*.','')
            url = f'{scheme}://{sub}.{domain}'
            try:
                response = requests.get(url)

            except requests.ConnectionError:
                pass
            else:
                if response.status_code == 200:
                    print(f'{Y}[{W}Status {G}{response.status_code}{Y}]{N} {sub}.{domain}')
                elif response.status_code == 403:
                    print(f'{Y}[{W}Status {R}{response.status_code}{Y}]{N} {sub}.{domain}')
                elif response.status_code == (301 or 302):
                    print(f'{Y}[{W}Status {Y}{response.status_code}{Y}]{N} {sub}.{domain}')
                subdomains.append(f'{sub}.{domain}')
        save(output, subdomains)
    except KeyboardInterrupt:
            print(R,'Exiting..',N)
    
def save(output ,subdomains):
    with open(output,'w') as output_file:
        for subdomain in subdomains:
            output_file.writelines(f'{subdomain}\n')
    print(f'Results saved in \'{C}{output}{N}\'')

if __name__ == '__main__':
    print(banner)
    bruteforcer(domain, wordlist, output)