import CSP_6_03_Writing_to_files as HW

def test_write_file():
    HW.writeFile([1,2,3], "newFile1")
    with open("newFile1", "r") as file:
        assert file.readline(100) == "1\n"
        assert file.readline(100) == "2\n"
        assert file.readline(100) == "3\n"

def test_sort_names():
    HW.sortNames("inputNames","targetName")
    with open("targetName", "r") as file:
        assert file.readline(100) == "Hayden\n"
        assert file.readline(100) == "Jade\n"
        assert file.readline(100) == "Jessica\n"
        assert file.readline(100) == "Lindsey\n"

def test_high_score():
    with open("scores.txt", "w") as file:
        file.write("10\n20\n40\n50\n")
    assert HW.highScore(30) == 30
    assert HW.highScore(60) == 35