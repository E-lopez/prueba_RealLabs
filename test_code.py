import sequences_calculator as calc

def test_seqs_1():
    res_count, *_ = calc.sequence_to_one(3)
    assert res_count == 8

def test_seqs_2():
    res_count, *_ = calc.sequence_to_one(7)
    assert res_count == 17

def test_max_legth_1():
    res = calc.find_sequences(1000)
    assert res == 179

def test_max_legth_2():
    res = calc.find_sequences(10000)
    assert res == 262
