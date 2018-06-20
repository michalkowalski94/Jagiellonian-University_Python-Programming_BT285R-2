#From p450.fasta find all expressions that within terms of prosite regex pattern:
#[FW]-[SGNH]-x-[GD]-{F}-[RKHPT]-{P}-C-[LIVMFAP]-[GAD]
import re

text = open("p450.fasta").read()
text_list = text.split("\n")
pars_text = "".join(text_list)
findings = re.findall(r'[FW][SNGH].[GD][^F][RKHPT][^P]C[LIVFMAP][GAD]',pars_text)
print "Regular expressions which are matching pattern:"
for i in findings:
        print i
