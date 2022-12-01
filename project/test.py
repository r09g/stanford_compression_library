from dataclasses import dataclass
from project.huffman_adaptive_coder import huffman_adaptive_node, huffman_adaptive_tree
from bitarray import bitarray


def _build_tree():
    tree = huffman_adaptive_tree()
    p = tree.root
    p.weight = 8
    p.left_child = huffman_adaptive_node(parent=p, weight=3)
    p.right_child = huffman_adaptive_node(parent=p, weight=5)
    p = p.right_child
    p.left_child = huffman_adaptive_node(parent=p, weight=2, value='a')
    p.right_child = huffman_adaptive_node(parent=p, weight=3, value='b')
    p = p.parent.left_child
    p.left_child = huffman_adaptive_node(parent=p, weight=1)
    p.right_child = huffman_adaptive_node(parent=p, weight=2, value=' ')
    p = p.left_child
    p.left_child = huffman_adaptive_node(parent=p, weight=0)
    tree.nyt = p.left_child
    p.right_child = huffman_adaptive_node(parent=p, weight=1, value='c')
    
    tree._update_implicit_order()
    tree._update_codebook(tree.root)
    return tree
    
def test_swap_nodes():
    # visually observe whether swapping is correct
    tree = _build_tree()
    tree.print_tree()
    tree.root.right_child.swap_nodes(tree.root.left_child)
    tree._update_implicit_order()
    tree.print_tree()
    
    tree.root.swap_nodes(tree.root)
    tree._update_implicit_order()
    tree.print_tree()
    
    tree.root.left_child.left_child.swap_nodes(tree.root.right_child.left_child.right_child)
    tree._update_implicit_order()
    tree.print_tree()
    
def test_find_symbol():
    tree = _build_tree()
    node = tree._find_symbol('a')
    print(node.value == 'a' and node.weight == 2)
    node = tree._find_symbol('b')
    print(node.value == 'b' and node.weight == 3)
    node = tree._find_symbol('c')
    print(node.value == 'c' and node.weight == 1)    
    node = tree._find_symbol(' ')
    print(node.value == ' ' and node.weight == 2)
    node = tree._find_symbol('x')
    print(node.value == None and node.weight == 0)
    
def test_encode_symbol():
    string = "aa bbb c"
    tree = huffman_adaptive_tree()
    for i in string:
        tree.encode_symbol(i)
    tree.print_tree()
    
    string = "e eae de eabe eae dcf"
    tree = huffman_adaptive_tree()
    for i in string:
        tree.encode_symbol(i)
    tree.print_tree()

def test_encdec():
    # string = "aa bbb c"
    string = "e eae de eabe eae dcf"
    tx = huffman_adaptive_tree()
    encoded_bitarray = bitarray()
    for i in string:
        encoded_bitarray += tx.encode_symbol(i)
    tx.print_tree()
    print(encoded_bitarray)
    
    print()
    symbols = ""
    rx = huffman_adaptive_tree()
    while(len(encoded_bitarray) > 0):
        symbol, num_bits = rx.decode_symbol(encoded_bitarray)
        symbols += symbol
        encoded_bitarray = encoded_bitarray[num_bits:]
    print(symbols)
    print(string == symbols)
    
if __name__ == "__main__":
    test_encdec()
    





