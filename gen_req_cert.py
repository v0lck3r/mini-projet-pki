#!/usr/bin/env python3
#Authors : Omar AOUAJ & Oussama RAHALI

from OpenSSL import crypto
import argparse

def args_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('--key', help='Private key')
	parser.add_argument('--out',  help='Ouput file path')
	return parser.parse_args()
args = vars(args_parser())
arg = args_parser()
key_file = args['key']
out_file = args['out']
print("Openning the Key Please standby")
with open(key_file, "r") as input_file:
	input_file_text = input_file.read()
	key = crypto.load_privatekey(crypto.FILETYPE_PEM,input_file_text)

def generatecsr():
	c = input('Enter your country(ex. US): ')
	st = input("Enter your state(ex. Nevada): ")
	l = input("Enter your location(City): ")
	o = input("Enter your organization: ")
	ou = input("Enter your organizational unit(ex. IT): ")
	cn = input('Enter The Common name: ')
	req = crypto.X509Req()
	req.get_subject().CN = cn
	req.get_subject().C = c
	req.get_subject().ST = st
	req.get_subject().L = l
	req.get_subject().O = o
	req.get_subject().OU = ou
	req.set_pubkey(key)
	req.sign(key, "sha256")

	f = open(out_file, "wb")
	f.write(crypto.dump_certificate_request(crypto.FILETYPE_PEM, req))
	f.close()
	print("Success")

generatecsr()