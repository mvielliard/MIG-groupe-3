#IMPRIMER TABLEAU LaTeX
import numpy as np

caption = "blub blub piche"

les_donnees = np.array([786.80636957, 786.80636957, 816.03509052, 822.75140039, 771.24184073,
 771.24184073, 783.65599688, 765.14509119, 716.11957722, 713.38368831,
 750.21578962, 759.12035013, 738.58471317, 756.13462893, 786.80636957,
 809.40068641, 839.90946643, 786.80636957, 768.18439342, 771.24184073,
 793.164375,   727.22204082, 768.18439342, 707.95873698, 713.38368831,
 774.31757782, 699.9366064, 611.20772128, 768.18439342, 699.9366064,
 707.95873698, 713.38368831, 774.31757782, 699.9366064,  611.20772128,
 768.18439342, 699.9366064])

def tableau_LaTeX(les_donnees, caption):

    les_donnees *= 100
    les_donnees = np.floor(les_donnees)
    les_donnees /= 100

    nb_colonnes = len(les_donnees)//10
    if len(les_donnees)%10 > 0:
        nb_colonnes += 1


    #CONSTRUCTION DU CODE LATEX

    LaTeX = "\\begin{table}[H]\n"\
            "\\centering\n\n"\
            "\\renewcommand{\\arraystretch}{1.25}"\
            "\\begin{tabular}{"

    for i in range(nb_colonnes):
        LaTeX += "c r @{\\hspace{0.8cm}}\n"

    LaTeX = LaTeX[:-18]
    LaTeX += "}\n"
    LaTeX += "\\hline\n"

    for i in range(nb_colonnes):
        LaTeX += "\\textbf{n°} & \\textbf{Dureté} &"

    LaTeX = LaTeX[:-1]


    LaTeX += "\n\\hline\n"


    for i in range(10):
        n = 0
        for j in range(len(les_donnees)):
            if j%10 == i:
                LaTeX += str(10*n + j%10 + 1)
                LaTeX += " & "
                LaTeX += str(les_donnees[j])
                LaTeX += " & "
                n += 1
        

        LaTeX = LaTeX[:-2]
        LaTeX += "\\\\ \n"

    LaTeX += "\n\\hline\n"

    LaTeX += "\\end{table}\n"\
            "\\caption{" + caption + "}\n"\
            "\\end{tabular}"

    #ABSOLUTE CINEMA

    print("--- LE CODE LATEX ---")
    print("\n")
    print(LaTeX)
    print("\n")
    print("--- --- --- --- ---")