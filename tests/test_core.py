from contextlens import stats


def test_stats():
    result = stats("hello world\nnext")
    assert result["characters"] == 16
    assert result["words"] == 3
    assert result["lines"] == 2
