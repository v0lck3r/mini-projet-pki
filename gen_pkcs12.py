#!/usr/bin/env python3
#Authors : Omar AOUAJ & Oussama RAHALI

from OpenSSL import crypto
import argparse
from getpass import getpass

def args_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('--in', help='Certificate file path')
	parser.add_argument('--out',  help='pkcs12 output file path')
	parser.add_argument('--inkey', help='Private key')
	return parser.parse_args()
args = vars(args_parser())
arg = args_parser()
cert_file = args['in']
pkcs12_out_file = args['out']
key_file = args['inkey']


with open(key_file, "r") as input_file:
	input_file_text = input_file.read()
	key = crypto.load_privatekey(crypto.FILETYPE_PEM,input_file_text)
with open(cert_file, "r") as cer_input_file:
	cer_input_file_text = cer_input_file.read()
	cert=crypto.load_certificate(crypto.FILETYPE_PEM,cer_input_file_text)

p12 = crypto.PKCS12()
p12.set_certificate(cert)
p12.set_privatekey(key)
while 1:
	passphrase = getpass("Entrer Export password: ")
	confirmpass = getpass("Verifying - Enter Export password: ")
	if passphrase == confirmpass :
		break

f = open(pkcs12_out_file, "wb")
f.write(p12.export(passphrase = bytes(passphrase, encoding = 'utf-8')))
f.close()
print("Success")