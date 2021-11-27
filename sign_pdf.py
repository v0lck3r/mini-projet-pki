#!/usr/bin/env python3
#Authors : Omar AOUAJ & Oussama RAHALI

from OpenSSL import crypto
import argparse
from PDFNetPython3.PDFNetPython import *
from getpass import getpass

def args_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('--in', help='PDF file path')
	parser.add_argument('--out',  help='Signed PDF file path')
	parser.add_argument('--inimg', help='signature image')
	parser.add_argument('--inp12', help='p12 file path')
	parser.add_argument('--outpfx', help='pfx file path')
	return parser.parse_args()
args = vars(args_parser())
arg = args_parser()
pdf_file = args['in']
signed_pdf_file = args['out']
img_file = args['inimg']
p12_file = args['inp12']
pfx_file = args['outpfx']
passphrase = getpass("Entrer Export password: ")
p12 = crypto.load_pkcs12(open(p12_file,'rb').read(), passphrase)

open(pfx_file, 'wb').write(p12.export())


PDFNet.Initialize("demo:1638019447865:7b6e02ca03000000002dbd876b294080df8352f3adc706f4400aea8f28")
pdf = PDFDoc(pdf_file)

signed_field = SignatureWidget.Create(pdf, Rect(330, 300, 430, 350), "AR")
pdf.GetPage(pdf.GetPageCount()).AnnotPushBack(signed_field)

approval_field = pdf.GetField("AR")
approval_sig_field = DigitalSignatureField(approval_field)
img = Image.Create(pdf.GetSDFDoc(), img_file)
SignatureWidget(approval_field.GetSDFObj()).CreateSignatureAppearance(img)
approval_sig_field.SignOnNextSave(pfx_file, '')
pdf.Save(signed_pdf_file, SDFDoc.e_incremental)

