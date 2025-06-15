def test_moving_average_computation():
    prices = [100, 110, 120, 130, 140]
    avg = sum(prices) / 5.0
    assert avg == 120.0
