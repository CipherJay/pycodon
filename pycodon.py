from tabulate import tabulate
from colorama import Fore, Style
from colorama import init
init(autoreset=True)

codon_table = {
    'TCA': 'Serine',
    'TCC': 'Serine',
    'TCG': 'Serine',
    'TCT': 'Serine',
    'TTC': 'Phenylalanine',
    'TTT': 'Phenylalanine',
    'TTA': 'Leucine',
    'TTG': 'Leucine',
    'TAC': 'Tyrosine',
    'TAT': 'Tyrosine',
    'TAA': 'Stop',
    'TAG': 'Stop',
    'TGC': 'Cysteine',
    'TGT': 'Cysteine',
    'TGA': 'Stop',
    'TGG': 'Tryptophan',
    'CTA': 'Leucine',
    'CTC': 'Leucine',
    'CTG': 'Leucine',
    'CTT': 'Leucine',
    'CCA': 'Proline',
    'CCC': 'Proline',
    'CCG': 'Proline',
    'CCT': 'Proline',
    'CAC': 'Histidine',
    'CAT': 'Histidine',
    'CAA': 'Glutamine',
    'CAG': 'Glutamine',
    'CGA': 'Arginine',
    'CGC': 'Arginine',
    'CGG': 'Arginine',
    'CGT': 'Arginine',
    'ATA': 'Isoleucine',
    'ATC': 'Isoleucine',
    'ATT': 'Isoleucine',
    'ATG': 'Methionine',
    'ACA': 'Threonine',
    'ACC': 'Threonine',
    'ACG': 'Threonine',
    'ACT': 'Threonine',
    'AAC': 'Asparagine',
    'AAT': 'Asparagine',
    'AAA': 'Lysine',
    'AAG': 'Lysine',
    'AGC': 'Serine',
    'AGT': 'Serine',
    'AGA': 'Arginine',
    'AGG': 'Arginine',
    'GTA': 'Valine',
    'GTC': 'Valine',
    'GTG': 'Valine',
    'GTT': 'Valine',
    'GCA': 'Alanine',
    'GCC': 'Alanine',
    'GCG': 'Alanine',
    'GCT': 'Alanine',
    'GAC': 'Aspartic Acid',
    'GAT': 'Aspartic Acid',
    'GAA': 'Glutamic Acid',
    'GAG': 'Glutamic Acid',
    'GGA': 'Glycine',
    'GGC': 'Glycine',
    'GGG': 'Glycine',
    'GGT': 'Glycine'
}

def identify_type(codon):
    if 'U' in codon:
        return f"{Fore.LIGHTBLUE_EX}mRNA{Style.RESET_ALL}"
    elif 'T' in codon:
        return f"{Fore.LIGHTWHITE_EX}DNA{Style.RESET_ALL}"
    else:
        return f"{Fore.LIGHTBLUE_EX}mRNA{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}/{Fore.LIGHTWHITE_EX}DNA{Style.RESET_ALL}"

def print_codon(codon):
    codon_type = identify_type(codon)
    codon_in_table = codon.replace('U', 'T')
    if codon_in_table in codon_table:
        amino_acid = f"{Fore.GREEN}{codon_table[codon_in_table]}{Style.RESET_ALL}"
        table_string = tabulate([[f"{Fore.RED}{codon}{Style.RESET_ALL}", amino_acid, codon_type]],
                                [f"{Fore.LIGHTBLACK_EX}Codon{Style.RESET_ALL}", 
                                 f"{Fore.LIGHTBLACK_EX}Amino Acid{Style.RESET_ALL}",
                                 f"{Fore.LIGHTBLACK_EX}Type{Style.RESET_ALL}"],
                                tablefmt="fancy_grid")
        print(table_string)
    else:
        print('')
        print(Fore.RED + "Error: Invalid codon entered" + Style.RESET_ALL)
        print(f"Codon {codon} not found in the table.")

def main():
    while True:
        print('')
        codon = input("Enter a codon or (q)uit: ").upper()
        if codon == 'Q':
            break
        print_codon(codon)

if __name__ == "__main__":
    main()
