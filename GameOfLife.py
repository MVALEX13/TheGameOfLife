import numpy as np
import matplotlib.pyplot as plt
import imageio                                          # used to create a GIF

### Global variables
N = 100                                       # dimension of the board
NB_IT = 100                                 # number of iteration

# this randomly initialize the board with 1 and 0. p(X = 1) = 0.5
def InitializeBoard(n):
    Z = np.zeros((n+2, n+2), dtype=int)
    Z[1:-1, 1:-1] = np.random.randint(low=2, size=(n,n))
    return Z

# this randomly initialize the board with 1 and 0. p(X = 1) = 1/6
def InitializeBoardRare(n):
    Z = np.zeros((n+2, n+2), dtype=int)
    Z[1:-1, 1:-1] = np.random.randint(low=6, size=(n,n))
    Z[Z>1] = 0
    return Z



def ComputeNextState(Z_k):
    
    neighbours_NW = Z_k[0:-2,0:-2]                       # neighbours in the Nord-West diago
    neighbours_N = Z_k[0:-2,1:-1]                        # neighbours in the Nord side
    neighbours_NE = Z_k[0:-2,2:]                         # neighbours in the Nord-East diag

    neighbours_W = Z_k[1:-1,0:-2]                        # neighbours in the West side
    neighbours_E = Z_k[1:-1,2:]                          # neighbours in the East side

    neighbours_SW = Z_k[2:,0:-2]                         # neighbours in the Nord-West diago
    neighbours_S = Z_k[2:,1:-1]                          # neighbours in the Nord side
    neighbours_SE = Z_k[2:,2:]                           # neighbours in the Nord-East diag

    neighbours_sum_mat = (neighbours_NW + neighbours_N + neighbours_NE + 
                         neighbours_W                 + neighbours_E  + 
                         neighbours_SW + neighbours_S + neighbours_SE)

    
    mask = ((neighbours_sum_mat == 2) & (Z_k[1:-1,1:-1] == 1)) | (neighbours_sum_mat == 3)  
    Z_kp1 = np.zeros((N+2,N+2))              
    Z_kp1[1:-1,1:-1][mask] = 1
    
    return Z_kp1


def main():
    Z = InitializeBoardRare(N)

    ### plotting the board evolution and saving each frame in the img/ directory
    fig = plt.figure()
    im = plt.imshow(Z)
    for i in range(NB_IT):
        Z = ComputeNextState(Z)
        im = plt.imshow(Z)
        plt.pause(1)
        fig.suptitle(f'Game of life (it = {i})')
        plt.savefig(f'./img/img_{i}.png', transparent = False,  facecolor = 'white')
    
    ### creation of a GIF from all the frames
    frames = list()
    for i in range(NB_IT):
        image = imageio.v2.imread(f'./img/img_{i}.png')
        frames.append(image)
    
    imageio.mimsave('./GameOfLife.gif', # output gif
                frames,              # array of input frames
                fps = 8)             # optional: frames per second




if __name__ == "__main__":
    main()

