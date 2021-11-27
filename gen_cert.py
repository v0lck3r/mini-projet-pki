#!/usr/bin/env python3
#Authors : Omar AOUAJ & Oussama RAHALI

from OpenSSL import crypto
import argparse

def args_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('--in', help='Certificate request file path')
	parser.add_argument('--out',  help='Certificate output file path')
	parser.add_argument('--signkey', help='Private key')
	parser.add_argument('--days',  help='Ouput file path')
	return parser.parse_args()
args = vars(args_parser())
arg = args_parser()
cert_req_file = args['in']
cert_out_file = args['out']
key_file = args['signkey']
days = args['days']
seconds = int(days)*24*3600
print("Openning the Key Please standby")
with open(key_file, "r") as input_file:
	input_file_text = input_file.read()
	key = crypto.load_privatekey(crypto.FILETYPE_PEM,input_file_text)
with open(cert_req_file, "r") as cer_req_input_file:
	cer_req_input_file_text = cer_req_input_file.read()
	csr=crypto.load_certificate_request(crypto.FILETYPE_PEM,cer_req_input_file_text)

cert = crypto.X509()
cert.get_subject().CN = csr.get_subject().CN
cert.get_subject().C = csr.get_subject().C
cert.get_subject().ST = csr.get_subject().ST
cert.get_subject().L = csr.get_subject().L
cert.get_subject().O = csr.get_subject().O
cert.get_subject().OU = csr.get_subject().OU
cert.set_serial_number(1000)
cert.gmtime_adj_notBefore(0)
cert.gmtime_adj_notAfter(int(seconds))
cert.set_issuer(cert.get_subject())
cert.set_pubkey(key)
cert.sign(key, "sha256")

f = open(cert_out_file, "wb")
f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
f.close()
print("Success")
