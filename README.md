# crypto-tools

A collection of tools created for the cryptography course at RUB. If you would like to contribute, feel free to do so!
*PLEASE NOTE: These tools are not intended for secure encryption of files. The implementations are just for educational purposes.*

## Usage

`crypto-wizard [OPTIONS] [-i [INPUT]] [-o [OUTPUT]] [MODE]`

Examples:

- `crypto-wizard.py --order-calc 5 73` - OUTPUT: `[INFO]:    Final Result is: 72`

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose
  -q, --quiet
  -i [INPUT], --input [INPUT]
                        Input, can be stdin or a file.
  -o [OUTPUT], --output [OUTPUT]
                        Output, can be stdout or a file.
  --eea EXTENDED_EUCLID EXTENDED_EUCLID, --extended-euclid EXTENDED_EUCLID EXTENDED_EUCLID
                        Extended Euclidean Algorithm.
  --order-calc ORDER_CALC ORDER_CALC
                        Calculates the order of a number in a group

## ROADMAP

These tools are on the roadmap to being included:

- [X] Euclidean Algorithm
- [X] Extended Euclidean Algorithm
- [ ] Square and Multiply
- [ ] Euler's Phi Function
- [ ] Prime Factorization
- [X] Order calculator
- [ ] DES encrypt & decrypt
- [ ] AES encrypt & decrypt
- [ ] RSA functionality
- [ ] Diffie-Hellman key exchanges
- [ ] Elgamal encryption
- [ ] ECC tooling
- [ ] MD5
- [ ] SHA-1 and SHA-256
- [ ] stream ciphers
- [ ] LFSRs
- [ ] historic ciphers (e.g. ROT13)
