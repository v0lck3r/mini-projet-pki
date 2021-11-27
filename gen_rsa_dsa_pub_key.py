#!/usr/bin/env python3
#Authors : Omar AOUAJ & Oussama RAHALI

#Génération de la clé pulique

from OpenSSL import crypto
import argparse


def args_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('--in', help='Private key')
	parser.add_argument('--out',  help='Ouput file path')
	return parser.parse_args()

args = vars(args_parser())
arg = args_parser()
in_file = args['in']
out_file = args['out']

with open(in_file, "r") as input_file:
	input_file_text = input_file.read()
	privkeyobject = crypto.load_privatekey(crypto.FILETYPE_PEM,input_file_text)
	open(out_file, "wb").write(crypto.dump_publickey(crypto.FILETYPE_PEM, privkeyobject))
