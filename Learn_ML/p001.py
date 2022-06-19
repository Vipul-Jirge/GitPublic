
def run(var1, var2):
    """Takes 2 lists, flips, adds & returns addition of flipped outputs

    Args:
        var1 (list(int)): _description_
        var2 (list(int)): _description_

    Returns:
        _type_: list(int)
    """
    var1 = [str(i) for i in var1]
    var1.reverse()
    var1 = int(''.join(var1))
    
    var2 = [str(i) for i in var2]
    var2.reverse()
    var2 = int(''.join(var2))
    
    output = var1 + var2
    output = list(str(output))
    output.reverse()
    return output

if __name__ == "__main__":
    l1 = [2,4,3]
    l2 = [5,6,4]
    print('run(l1,l2): ', run(l1,l2))
