import re


DNA = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]


def isMutant(dna : list) -> bool:
    concatDna = "".join(dna)
    regexList = [
        r".*[ACGT]{4}.*", # Lineas horizontales
        r"(.*)([ACGT])(.{5}\2){3,}(.*)", # Lineas verticales
        r"(.*)([ACGT])(.{6}\2){3,}(.*)", # Lineas diagonales izq-der
        r"(.*)([ACGT])(.{4}\2){3,}(.*)", # Lineas diagonales der-izq
    ]
    matchCounter = 0
    
    for regex in regexList:
        if re.match(regex, concatDna):
            matchCounter += 1
    
    if matchCounter >= 2:
        return True
    return False




if __name__ == "__main__":
    print(isMutant(DNA))