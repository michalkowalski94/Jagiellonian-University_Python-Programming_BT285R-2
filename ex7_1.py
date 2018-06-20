#From NC_000072.6.gb export and display CDS using regular expressions
#Display must be in list of tuples
import re
def genbankPAIRS(filename = "NC_000072.6.gb"):
    """This function returns a pair of CDS in one tuple appended in list"""
    genbank = open(filename).read()
    gb_00 = re.sub("\s+", "", genbank)
    gb_01 = re.findall("(?<=CDSjoin\().*(?=\)/gene)", gb_00)
    gb_02 = re.findall("[0-9]{4}\.\.[0-9]{4}", gb_01[0])
    gb_03 = [tuple(int(y) for y in x.split("..")) for x in gb_02]
    return gb_03

def genbankCDS(filename = "NC_000072.6.gb"):
    """This function returns whole CDS line from *.gb file
    in one tuple appended in list"""
    genbank = open(filename).read()
    gb_00 = re.sub("\s+","", genbank)
    gb_01 = re.findall("CDSjoin.(.*)./gene",gb_00,re.DOTALL)
    gb_02 = str(gb_01[0])
    gb_03 = gb_02.split("gene")
    gb_04 = [tuple(re.findall("([0-9]{4}\.\.[0-9]{4})",gb_03[x])) for x in range(len(gb_03)) if len(re.findall("([0-9]{4}\.\.[0-9]{4})",gb_03[x]))>0]
    return gb_04

