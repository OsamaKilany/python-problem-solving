

def DNA_strand(dna):
    return dna.translate(str.maketrans('ATCG', 'TAGC'))

    #     match i:
    #         case 'T': DNA.append('A')
    #         case 'A': DNA.append('T')
    #         case 'C': DNA.append('G')
    #         case 'G': DNA.append('C')
            
    # return ''.join(DNA)


print(DNA_strand("AATCG"))