import regex as re
from random import choices


# DNA = ["TTGCCA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
def genRandDna(n : int) -> list:
    return ["".join(choices("ACGT", k=n)) for i in range(n)]


def isMutant(dna : list) -> bool:
    concatDna = " ".join(dna)
    n = len(dna)
    regexList = [
        r"([ACGT])(\1{3})", # Lineas horizontales
        r"([ACGT])(.{" + str(n) + r"}\1){3,}", # Lineas verticales
        r"([ACGT])(.{" + str(n + 1) + r"}\1){3,}", # Lineas diagonales izq-der
        r"([ACGT])(.{" + str(n - 1) + r"}\1){3,}", # Lineas diagonales der-izq
    ]
    matchCounter = 0
    
    for regex in regexList:
        matches = re.findall(regex, concatDna, overlapped=True)
        if matches:
            matchCounter += len(matches)
        print(matches)
    
    if matchCounter >= 2:
        return True
    return False




if __name__ == "__main__":
    DNA = genRandDna(10)
    print(isMutant(DNA))
    for i in DNA:
        for j in i:
            print(f"{j} ", end="")
        print()