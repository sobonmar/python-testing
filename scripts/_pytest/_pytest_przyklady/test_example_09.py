# Wbudowane fikstury pytest - tmp_path
CONTENT = "content"


def test_create_file(tmp_path):
    """Test tmp_path fixture - creates temporary directory with file"""

    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT, encoding="utf-8")

    assert p.read_text(encoding="utf-8") == CONTENT
    assert len(list(tmp_path.iterdir())) == 1
