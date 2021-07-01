'''
Author: Michele Alladio
es: 
Translate RNA sequences into proteins.

RNA can be broken into three nucleotide sequences called codons, and then translated to a polypeptide like so:

RNA: "AUGUUUUCU" => translates to

Codons: "AUG", "UUU", "UCU" => which become a polypeptide with the following sequence =>

Protein: "Methionine", "Phenylalanine", "Serine"

There are 64 codons which in turn correspond to 20 amino acids; however, all of the codon sequences and resulting amino acids are not important in this exercise. If it works for one codon, the program should work for all of them. However, feel free to expand the list in the test suite to include them all.

There are also three terminating codons (also known as 'STOP' codons); if any of these codons are encountered (by the ribosome), all translation ends and the protein is terminated.

All subsequent codons after are ignored, like this:

RNA: "AUGUUUUCUUAAAUG" =>

Codons: "AUG", "UUU", "UCU", "UAA", "AUG" =>

Protein: "Methionine", "Phenylalanine", "Serine"

Note the stop codon "UAA" terminates the translation and the final methionine is not translated into the protein sequence.

Below are the codons and resulting Amino Acids needed for the exercise.

Codon	Protein
AUG	Methionine
UUU, UUC	Phenylalanine
UUA, UUG	Leucine
UCU, UCC, UCA, UCG	Serine
UAU, UAC	Tyrosine
UGU, UGC	Cysteine
UGG	Tryptophan
UAA, UAG, UGA	STOP
'''

proteinDict = { 'Methionine': ['AUG'],                      #dizionario usato per il riconoscimento delle proteine
                'Phenylalanine': ['UUU', 'UUC'],
                'Leucine': ['UUA', 'UUG'],
                'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
                'Tyrosine': ['UAU', 'UAC'],
                'Cysteine': ['UGU', 'UGC'],
                'Tryptophan': ['UGG'],
                'STOP': ['UAA', 'UAG', 'UGA']}

def RNA_To_protein(rna):
    cnt = 0 
    triplet = ''    #tripletta di caratteri es: UUC
    proteinList = []    #lista delle proteine presenti

    for character in rna:   
        cnt += 1
        triplet += character

        if cnt % 3 == 0:    #ogni 3 caratteri
            ok = False  #codone non presente
            for protein, codons in proteinDict.items():
                for codon in codons:
                    if triplet == codon:    #corrispondenza di un codone
                        ok = True   #codone presente
                        triplet = '' 
                        if protein not in proteinList and protein != 'STOP':    #se la proteina non è già presente ed è diversa da STOP
                            proteinList.append(protein)

            if ok == False: #se il codone non è presente
                print("RNA non valido")
                return
        
    return proteinList


def main():
    cnt = 0
    rna = input("Inserisci una sequenza valida di rna formata da codoni\nAUG	Methionine\nUUU, UUC	Phenylalanine\nUUA, UUG	Leucine\nUCU, UCC, UCA, UCG	Serine\nUAU, UAC	Tyrosine\nUGU, UGC	Cysteine\nUGG	Tryptophan\nUAA, UAG, UGA	STOP\nes: AUGUUUUCUUAAAUG\n").upper()

    for character in rna:
        if character != 'U' and character != 'A' and character != 'C' and character != 'G': #controllo dei caratteri
            print("RNA non valido")
            return
        else:
            cnt+=1
    
    if cnt % 3 != 0:    #controllo del numero di caratteri
        print("RNA non valido")
        return
    
    print(f"proteine contenute in {rna}: {RNA_To_protein(rna)}")


if __name__ == "__main__":
    main()