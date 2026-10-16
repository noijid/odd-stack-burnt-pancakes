# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:06:03 2026

@author: naoi0002
"""

def pangen(n):
    """ outputs the stack -In """
    return  [-i for i in range(1,n+1)]


def flip(arr: list, k: int) -> tuple:
    """ flips the first k pancake of the stack """
    arr[:k] =  [-x for x in arr[:k][::-1]]
    

def small_values(n):
    """ output the sequences for small values of n """
    liseq =[
        [], #n=0
        [1], # n=1
        [2, 1, 2, 1], # n=2
        [3, 2, 3, 2, 3, 2], # n=3
        [4, 3, 4, 3, 4, 3, 4, 3], # n=4
        [5, 4, 5, 4, 5, 4, 5, 4, 5, 4], # n=5
        [6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5], # n=6
        [7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6], # n=7
        [8, 6, 2, 8, 5, 7, 3, 5, 8, 5, 3, 7, 5, 2, 6], # n=8
        [9, 8, 7, 4, 2, 6, 2, 8, 5, 2, 7, 3, 9, 5, 2, 7, 3], # n=9
        [10, 8, 4, 2, 6, 9, 6, 2, 4, 8, 4, 10, 3, 9, 6, 2, 4, 7], # n=10
        [11, 8, 5, 9, 3, 7, 10, 8, 2, 6, 9, 4, 7, 11, 6, 3, 10, 3, 5], # n=11
        [12, 2, 5, 11, 5, 2, 9, 2, 12, 7, 11, 6, 3, 10, 2, 6, 11, 6, 3, 8, 5], # n=12
        [13, 6, 3, 12, 3, 7, 13, 8, 5, 11, 5, 9, 12, 7, 10, 5, 3, 9, 4, 11, 6, 9], # n=13
        [14, 7, 3, 13, 4, 7, 14, 10, 7, 12, 7, 9, 13, 10, 3, 7, 12, 10, 2, 6, 11, 6, 9], # n=14
        [15, 10, 4, 6, 14, 6, 4, 10, 15, 10, 4, 6, 14, 6, 4, 10, 15, 10, 4, 6, 14, 6, 4, 10], # n=15
        [16, 10, 4, 6, 15, 7, 4, 11, 16, 11, 5, 7, 15, 6, 4, 10, 16, 11, 4, 7, 8, 7, 15, 6, 4, 11], # n=16
        [17, 10, 4, 6, 16, 8, 4, 12, 17, 12, 13, 12, 5, 7, 16, 7, 5, 11, 17, 12, 5, 8, 9, 8, 16, 6, 4, 12], # n=17
        [18, 10, 6, 14, 12, 17, 7, 10, 18, 14, 11, 3, 8, 12, 6, 16, 6, 12, 3, 15, 11, 17, 14, 9, 16, 11, 13, 8, 11], #n=18
        [19, 10, 4, 6, 18, 10, 4, 7, 14, 19, 14, 7, 4, 10, 18, 6, 4, 10, 19, 14, 4, 9, 11, 8, 18, 8, 11, 9, 4, 14], # n=19
        [20, 10, 4, 6, 19, 11, 4, 7, 15, 20, 15, 16, 15, 7, 4, 10, 19, 7, 5, 11, 20, 15, 5, 10, 12, 9, 19, 8, 11, 9, 4, 15], # n=20
        [21, 16, 6, 18, 13, 5, 8, 5, 17, 10, 14, 19, 10, 6, 18, 15, 10, 20, 16, 7, 19, 14, 4, 7, 17, 21, 14, 8, 4, 11, 20, 3, 7], # n=21
        [22, 9, 7, 18, 4, 15, 21, 8, 13, 9, 16, 22, 9, 10, 9, 11, 18, 5, 12, 4, 9, 13, 7, 20, 15, 5, 12, 10, 19, 21, 16, 9, 18, 6, 16], #n=22
        [23, 14, 8, 18, 14, 6, 12, 16, 22, 10, 8, 14, 23, 18, 8, 14, 10, 6, 22, 6, 10, 14, 8, 18, 23, 14, 8, 10, 22, 16, 12, 6, 14, 18, 8, 14], #n=23
        [24, 9, 7, 19, 5, 16, 23, 9, 15, 11, 18, 24, 10, 12, 20, 5, 15, 5, 8, 19, 17, 5, 10, 14, 7, 22, 17, 6, 13, 10, 21, 23, 18, 11, 20, 6, 18], #n=24
        [25, 10, 20, 4, 13, 17, 10, 24, 12, 15, 9, 4, 11, 17, 20, 25, 16, 4, 12, 24, 10, 4, 20, 6, 13, 9, 25, 18, 15, 7, 4, 10, 22, 10, 24, 6, 20, 4, 10], #n=25
        [26, 11, 9, 2, 21, 5, 16, 25, 11, 17, 13, 2, 20, 26, 12, 14, 22, 5, 17, 7, 10, 21, 19, 7, 2, 12, 16, 9, 24, 17, 6, 13, 10, 23, 25, 18, 11, 20, 6, 18], #n= 26
        [27, 22, 16, 10, 4, 6, 18, 26, 6, 4, 22, 6, 4, 10, 27, 10, 4, 6, 22, 4, 6, 26, 18, 16, 22, 12, 4, 16, 27, 18, 12, 14, 22, 6, 4, 18, 4, 6, 26, 18, 16, 22], #n = 27   
        [28, 9, 2, 17, 10, 6, 12, 20, 10, 24, 8, 27, 21, 14, 2, 7, 17, 6, 26, 12, 5, 24, 16, 20, 15, 2, 9, 18, 14, 28, 19, 14, 6, 22, 6, 14, 27, 9, 22, 5, 20, 25, 12], #n=28
        [29, 20, 4, 10, 26, 14, 4, 22, 28, 18, 6, 4, 24, 10, 14, 29, 18, 20, 12, 4, 6, 24, 16, 26, 16, 4, 18, 28, 8, 20, 29, 16, 12, 24, 4, 16, 14, 8, 4, 18, 20, 28, 6, 4, 14] , # n = 29
        [30, 9, 17, 2, 11, 13, 25, 27, 8, 24, 10, 19, 17, 28, 13, 11, 15, 12, 2, 24, 2, 26, 19, 29, 21, 26, 11, 2, 16, 12, 22, 13, 30, 9, 26, 2, 10, 29, 10, 15, 11, 26, 2, 9, 12, 19], # n = 30
        [31, 18, 12, 24, 20, 26, 22, 6, 12, 14, 18, 24, 30, 14, 12, 18, 31, 26, 12, 22, 16, 12, 10, 6, 30, 6, 10, 12, 16, 22, 12, 26, 31, 18, 12, 14, 30, 24, 18, 14, 12, 6, 22, 26, 20, 24, 12, 18] , # n = 31
        [32, 11, 20, 17, 2, 29, 7, 31, 14, 17, 10, 28, 7, 14, 9, 16, 32, 10, 26, 9, 19, 21, 13, 31, 27, 11, 8, 24, 8, 19, 17, 2, 22, 25, 8, 28, 13, 15, 12, 30, 24, 16, 8, 11, 9, 20, 2, 27, 9]] #32
    return liseq[n]

def seq33(n):
    """ The flipping sequence provided for n = 9 mod 12 in the article """
    s = (n-33)//12
    W1 = [n, n-5, n-29]
    W2 = []
    for i in range(s):
        W2 += [n - 35 -12*i, n-41-12*i]
    W3 = []
    for i in range(s):
        W3+= [6 +12*i]
    W4 = [n-19, n-1, 16, 8, n-7, n-17, n-13, 6, n-3, 14, 6, 12, 4, n-13]    
    W5 =[]
    for i in range(s):
        W5 += [6, 4, n-35-12*i]
    W6 = [n]
    A1 = [28, 8, 16]
    A2 = []
    for i in range(s):
        A2 += [40 +12*i, 4, 6]
    A3 = [n - 1]
    A4 =[]
    for i in range(s):
        A4 += [n - 9 -6*i, n - 11 - 12*i, n-5 - 6*i]
    A5 = [(n-1)//2 -2, 6, (n-1)//2 +12, 6, (n-1)//2+4, 4, (n-1)//2 +8, 12, 4, (n-1)//2 +14, 4, (n-1)//2]
    B1 = [n, 2*n//3 +6]
    B2 = []
    for i in range(s):
        B2 += [2*n//3 - 8*i, 2*n//3 +2 -8*i, 2*n//3 +10 +4*i, 6 +12*i, 4 +12*i, 2*n//3 +6 +4*i ]    
    B3 = [4, 18, 22, 16, n-1, n-15, 10, n-5, n-17, n-29, n-11, 8, n-3, 6, n-15]
    seq = W1, W2, W3, W4, W5, W6, A1, A2, A3, A4, A5, B1, B2, B3
    return seq

def test_seq(pan,seq, verbose = False):
    """ applys the sequence of flip seq to the stack pan. if Verbose = True, display all the intermeiates states of the stack """
    for i in seq:
        if verbose:
            print(pan,"\n flip : ", i)
        flip(pan,i)
    if verbose:
        print(pan, "\n")


def display_seq(pan,seq):
    """ Display all the flips together with the step in which they are """
    W1, W2, W3, W4, W5, W6, A1, A2, A3, A4, A5, B1, B2, B3 = seq
    print("Step W1")
    test_seq(pan, W1, True)    
    print("Step W2")
    test_seq(pan, W2, True) 
    print("Step W3")
    test_seq(pan, W3, True) 
    print("Step W4")
    test_seq(pan, W4, True) 
    print("Step W5")
    test_seq(pan, W5, True) 
    print("Step W6")
    test_seq(pan, W6, True) 
    print("Step A1")
    test_seq(pan, A1, True) 
    print("Step A2")
    test_seq(pan, A2, True) 
    print("Step A3")
    test_seq(pan, A3, True) 
    print("Step A4")
    test_seq(pan, A4, True) 
    print("Step A5")
    test_seq(pan, A5, True) 
    print("Step B1")
    test_seq(pan, B1, True) 
    print("Step B2")
    test_seq(pan, B2, True) 
    print("Step B3")
    test_seq(pan, B3, True)     
    
    
    
def add3flips(seq0,x):
    """ Given a flipping sequence for -In and a pancake x that satisfy the hypothesis 
    of Lemma 15, computes a flipping sequence for -I_{n+2} using 3 more flips """
    n = seq0[0][0]
    pan = pangen(n)
    seqtot = []
    count = 0
    for seq in seq0:
        seq2 = []
        for k in seq:
            if x in pan[:k+1] or -x in pan[:k+1]:
                seq2.append(k+2)
            else :
                seq2.append(k)
            flip(pan,k)
            if pan[0] == x and (count == 0 or count == 2):
                count +=1
                seq2.append(2)
            elif pan[0] == -x and count == 1:
                count +=1
                seq2.append(2)
        seqtot.append(seq2)
    return seqtot
    


def compute_seq(seq0, n, r):
    """ case disjunction on the value of n mod 12 to apply the good values to the sequence"""
    if r == 9:
        return seq0
    seq1 = add3flips(seq0, n-4)    
    if r == 11:
        return seq1
    seq2 = add3flips(seq1, n-8)
    if r == 1:
        return seq2
    seq3 = add3flips(seq2, n-10)
    if r == 3:
        return seq3
    seq4 = add3flips(seq3, n-16)
    if r == 5:
        return seq4
    seq5 = add3flips(seq4, n-18)
    return seq5

def main(n):
    if n < 33:
        return small_values(n)
    if n %2 == 0:
        print("The largest even value we can handle is 32")
        return None
    r = n%12
    #The next if/else computes the largest integer n0 = 9 mod 12 lower than n
    if r >= 9:
        n0 = 12 * (n//12) +9
    else :
        n0 = 12 * (n//12) -3 
    pan = pangen(n0) 
    seq0 = seq33(n0) #We first compute the value for n0
    seq = compute_seq(seq0, n0, r) #And we apply Lemma 15 the good number of times
    seq_tot = []
    pan = pangen(n)
    for i in seq:
        seq_tot += i
    print("flipping sequence:\n",seq_tot,'\n')
    print("number of flips:33", len(seq_tot),'\n')
    display_seq(pan, seq)

if __name__ == "__main__":
    n = int(input("Enter the value of n :\n"))
    main(n)

    

    
    
    
    
    
    
    
    
    
    