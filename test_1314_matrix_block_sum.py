import code_1314_matrix_block_sum as c

def test_example_1():
    s = c.Solution()
    result = s.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1)
    assert  result == [[12,21,16],[27,45,33],[24,39,28]]

def test_example_2():
    s = c.Solution()
    result = s.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 2)
    assert result == [[45,45,45],[45,45,45],[45,45,45]]