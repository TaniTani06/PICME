def next_seq(seq):
    new_seq = ''
    for i in range(len(seq)):
        if seq[i] == 'L':
            new_seq = new_seq + 'LS'
        if seq[i] == 'S':
            new_seq = new_seq + 'L'
    seq = new_seq
    return seq

   
def f(x):
    seq = 'L'
    while x>len(seq):
        seq = next_seq(seq)
    
    #print (seq)
    return (seq[x-1])



#print(f(15))
