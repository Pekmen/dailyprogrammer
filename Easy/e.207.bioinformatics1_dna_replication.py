#!/usr/bin/env python3

##
#  [Easy] #207
#
#  Bioinformatics 1: DNA Replication
#
#  http://www.reddit.com/r/dailyprogrammer/comments/2zyipu/20150323_challenge_207_easy_bioinformatics_1_dna/
##


def translate(trip):
  for k in codons:
    if (trip in codons[k]):
      return k;

pairs = {"A" : "T", "T" : "A", "G" : "C", "C" : "G"};
codons = {
    "Phe": ["TTT", "TTC"],
    "Leu": ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"],
    "Ile": ["ATT", "ATC", "ATA"],
    "Met": ["ATG"],     
    "Val": ["GTT", "GTC", "GTA", "GTG"],
    "Ser": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
    "Pro": ["CCT", "CCC", "CCA", "CCG"],
    "Thr": ["ACT", "ACC", "ACA", "ACG"],
    "Ala": ["GCT", "GCC", "GCA", "GCG"],
    "Tyr": ["TAT", "TAC"],
    "STOP": ["TAA", "TAG", "TGA"],
    "His": ["CAT", "CAC"],
    "Gln": ["CAA", "CAG"],
    "Asn": ["AAT", "AAC"],
    "Lys": ["AAA", "AAG"],
    "Asp": ["GAT", "GAC"],
    "Glu": ["GAA", "GAG"],
    "Cys": ["TGT", "TGC"],
    "Trp": ["TGG"],
    "Arg": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "Gly": ["GGT", "GGC", "GGA", "GGG"]
}

strand1 = (input(">").split());
strand2 = [pairs[i] for i in strand1 if i != ' '];
trips = [''.join(strand1[i : i+3]) for i in range(0, len(strand1), 3)];
trans_seq = [translate(trip) for trip in trips];

print (' '.join(strand1));
print (' '.join(strand2));
print (' '.join(trans_seq));