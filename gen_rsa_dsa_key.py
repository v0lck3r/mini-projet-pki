#!/usr/bin/env python3
#Authors : Omar AOUAJ & Oussama RAHALI

#Génération de la clé privée

from OpenSSL import crypto
import argparse


def args_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('--size', help='size')
	parser.add_argument('--out',  help='Ouput file path')
	parser.add_argument('--type',  help='1- RSA | 2- DSA (e.g. --type 2')
	return parser.parse_args()

args = vars(args_parser())
arg = args_parser()
size = args['size']
out_file = args['out']
type = args['type']

pkey = crypto.PKey()
if arg.type == "1":
	pkey.generate_key(crypto.TYPE_RSA, int(size))
elif arg.type == '2':
	pkey.generate_key(crypto.TYPE_DSA, int(size))
open(out_file, "wb").write(crypto.dump_privatekey(crypto.FILETYPE_PEM, pkey))