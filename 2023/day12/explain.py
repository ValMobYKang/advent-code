

def foo(string, block):
    string = string.lstrip('.')

    if string == '':
        return int(block == ())
    if block == ():
        return int(string.find('#') == -1)


    first_str = string[0]
    if first_str  == '#':
        first_block_idx = block[0]
        # before start -> if string is small: '##' [3] 
        if len(string) < first_block_idx:
            return 0
        # starting -> If dot in first block: '#..' [3,3]
        elif '.' in string[:first_block_idx]:
            return 0
        # end -> '###.' [3] should locate '.'
        elif string[first_block_idx] == '#':
            return 0
        # end -> The last block: '###' [3] 
        elif len(string) == first_block_idx:
            return int(len(block) == 1)
        else:
            # end-> next -> after first block must be dot, e.g. '###.###.' 3,3
            return foo(string[first_block_idx+1:], block[1:])  
    if first_str == '?':
        count1 = foo('#'+string[1:], block) 
        count2 = foo('.'+string[1:], block)
        return count1+count2

