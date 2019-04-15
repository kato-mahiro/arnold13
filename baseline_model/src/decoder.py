from .const import *

def decoder(gene):
    gene_index=0
    weights_ih = [[0 for i in range(HIDDEN_LAYER_NUMBER)]for j in range(INPUT_NUMBER)]
    weights_ho = [[0 for i in range(OUTPUT_NUMBER)] for j in range(HIDDEN_LAYER_NUMBER)]
    for i in range(INPUT_NUMBER):
        for h in range(HIDDEN_LAYER_NUMBER):
            weights_ih[i][h] = gene[gene_index]
            gene_index += 1
    for h in range(HIDDEN_LAYER_NUMBER):
        for o in range(OUTPUT_NUMBER):
            weights_ho[h][o] = gene[gene_index]
            gene_index += 1
    return weights_ih,weights_ho

if __name__=='__main__':
    INPUT_NUMBER = 3
    HIDDEN_LAYER_NUMBER = 2
    OUTPUT_NUMBER = 1
    gene=[1,2,3,4,5,6,7,8]
    ih,ho = decoder(gene)
    print(ih)
    print(ho)
    import numpy as np
    ih = np.array(ih)
    ho = np.array(ho)
    print(ih)
    print(ho)
