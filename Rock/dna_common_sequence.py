#!/usr/bin/env checkio --domain=py run dna-common-sequence

# Deoxyribonucleic acid is a molecule that encodes    the genetic instructions used in the development and functioning of all known living organisms and many viruses.    A DNA molecule consists of two strands that wrap around each other to resemble a twisted ladder whose sides, made of    sugar and phosphate molecules, are connected by rungs of nitrogen-containing chemicals called bases.    Each strand is a linear arrangement of repeating similar units called nucleotides.    Each nucleotide is composed of a nitrogen-containing nucleobase—either    guanine (G), adenine (A), thymine (T), or cytosine (C).    The particular order of the bases arranged along the sugar-phosphate backbone is called the DNA    sequence; the sequence specifies the exact genetic instructions required to create a particular organism with its    own unique traits.
# 
# For this mission, we want to compare DNA strands and find the longest common base subsequence in the two strands.Subsequences are not required to occupy consecutive positions within the original sequences and letters can        be        placed at varying distances between each other.These strands can be represented as strings consisting    of the    letters "ACGT". For example the longest common sequence for strands "ACGTC" and "TTACTC" is "ACTC".
# 
# You are given two strand descriptions and you should find the longest common subsequence (not the substring). If we    find several “longest” sequences with equal length, then return each of them as a string where these sequence are    written inlexicographical orderseparated by commas. For example, for "CGCTA" and "TACCG" we found    three sequences    "CG", CC and "TA", so the result is "CC,CG,TA". If the given sequences don't have a common sequence then return an empty    string.
# 
# Input:Two arguments. Base sequences as strings.
# 
# Output:The common longest sequence or sequences as a string.
# 
# 
# Precondition:
# all(0 < len(seq) ≤ 64 and all(x in "ACGT" for x in seq) for seq in args)
# 
# 
# END_DESC

def common(first, second):
    return ""

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert common("ACGTC", "TTACTC") == "ACTC", "One"
    assert common("CGCTA", "TACCG") == "CC,CG,TA", "Two"
    assert common("GCTT", "AAAAA") == "", "None"