from TinyStatistician import TinyStatistician


def test_tiny_statistician__mean():
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    assert tstat.mean(a) == 82.4


def test_tiny_statistician__median():
    tstat = TinyStatistician()

    a = [1, 42, 300, 10, 59]
    assert tstat.median(a) == 42

    b = [8, 7, 5, 4, 2, 1]
    assert tstat.median(b) == 4.5


def test_tiny_statistician__quartile():
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    assert tstat.quartile(a, 25) == 10.0
    assert tstat.quartile(a, 75) == 59.0


def test_tiny_statistician__var():
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    assert tstat.var(a) == 12279.439999999999


def test_tiny_statistician__std():
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    assert tstat.std(a) == 110.81263465868862
