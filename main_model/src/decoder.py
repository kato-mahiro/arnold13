from .const import *

def decoder(gene):
    gene_index=0
    weights_ih = [[0 for i in range(HIDDEN_NUMBER)]for j in range(INPUT_NUMBER)]
    weights_ho = [[0 for i in range(OUTPUT_NUMBER)] for j in range(HIDDEN_NUMBER)]
    weights_im = [[0 for i in range(MODURATORY_NUMBER)] for j in range(INPUT_NUMBER)]
    weights_mh = [[0 for i in range(HIDDEN_NUMBER)] for j in range(MODURATORY_NUMBER)]
    weights_em = [[0 for i in range(MODURATORY_NUMBER)] for j in range(ECHO_NUMBER)]
    for i in range(INPUT_NUMBER):
        for h in range(HIDDEN_NUMBER):
            weights_ih[i][h] = gene[gene_index]
            gene_index += 1
    for h in range(HIDDEN_NUMBER):
        for o in range(OUTPUT_NUMBER):
            weights_ho[h][o] = gene[gene_index]
            gene_index += 1
    for i in range(INPUT_NUMBER):
        for m in range(MODURATORY_NUMBER):
            weights_im[i][m] = gene[gene_index]
            gene_index += 1
    for m in range(MODURATORY_NUMBER):
        for h in range(HIDDEN_NUMBER):
            weights_mh[m][h] = gene[gene_index]
            gene_index += 1
    for e in range(ECHO_NUMBER):
        for m in range(MODURATORY_NUMBER):
            weights_em[e][m] = gene[gene_index]
            gene_index += 1
    return weights_ih,weights_ho,weights_im,weights_mh,weights_em

if __name__=='__main__':
    INPUT_NUMBER = 3
    HIDDEN_NUMBER = 2
    OUTPUT_NUMBER = 1
    ECHO_NUMBER = 3
    MODURATORY_NUMBER = 2
    n = INPUT_NUMBER*HIDDEN_NUMBER + HIDDEN_NUMBER*OUTPUT_NUMBER + INPUT_NUMBER*MODURATORY_NUMBER + MODURATORY_NUMBER*HIDDEN_NUMBER + ECHO_NUMBER*MODURATORY_NUMBER
    gene=list(range(n))
    print(gene)
    ih,ho,im,mh,em = decoder(gene)
    import numpy as np
    ih = np.array(ih)
    ho = np.array(ho)
    im = np.array(im)
    mh = np.array(mh)
    em = np.array(em)
    print(ih)
    print("---")
    print(ho)
    print("---")
    print(im)
    print("---")
    print(mh)
    print("---")
    print(em)
