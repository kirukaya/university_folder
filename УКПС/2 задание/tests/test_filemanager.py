import os
import shutil
import pytest

filePath = "test.txt" 
dirPath = "test"  

@pytest.fixture
def wiam():
    if "File_Manager" not in dirPath:
        print("Выход за пределы рабочей папки")
    else:
        print("/Users/Игорь/File_Manager/test")
        return True


# создать папку

@pytest.fixture
def mkdr():
    if "File_Manager" not in dirPath:
        print("Невозможно создать папку")
    else:
        os.mkdir(dirPath)
        return True


# удалить папку

@pytest.fixture
def dldr():
    if "File_Manager" not in dirPath:
        print("Невозможно создать папку")
    else:
        os.rmdir(dirPath)
        return True


# создать файл

@pytest.fixture
def mkfl():
    file = open(filePath, "w+")
    file.close()
    return True


# записать в файл

@pytest.fixture
def wrtfl():
    try:
        line = "It's test line! :)"
        f = open(filePath, "a")
        f.write(line)
        f.close()
        return True
    except FileExistsError:
        print("file does not exist")


# показать содержимое файла

@pytest.fixture
def shw():
    try:
        file = open(filePath, "r")
        print(file.read())
        file.close()
        return True
    except FileExistsError:
        print("file does not exists")

# скопировать файл

@pytest.fixture
def cpfl():
    try:
        fullNewPath = "test_new.txt"
        shutil.copyfile(filePath, fullNewPath)
        return True
    except FileExistsError:
        print("file does not exist")


# переименовать файл

@pytest.fixture
def rnmfl():
    try:
        fullNewPath = "test_.txt"
        os.rename(filePath, fullNewPath)
        return True
    except FileNotFoundError:
        print("file does not exist")


# переместить файл

@pytest.fixture
def mvfl():
    try:
        fullNewPath = "test_new.txt"
        fullNewPath2 = "test_new_new.txt"
        shutil.copyfile(fullNewPath, fullNewPath2)
        os.remove(fullNewPath)
        return True
    except FileNotFoundError:
        print("file does not exist")


# удалить файл

@pytest.fixture
def dlfl():
    try:
        filePath = "test_.txt"
        os.remove(filePath)
        return True
    except FileExistsError:
        print("file does not exist")

# выполняю тесты

def test_wiam(wiam):
    assert (wiam == True)


def test_mkdr(mkdr):
    assert (mkdr == True)


def test_mkfl(mkfl):
    assert (mkfl == True)


def test_wrtfl(wrtfl):
    assert (wrtfl == True)


def test_shw(shw):
    assert (shw == True)


def test_cpfl(cpfl):
    assert (cpfl == True)


def test_rnmfl(rnmfl):
    assert (rnmfl == True)


def test_mvfl(mvfl):
    assert (mvfl == True)


def test_dldr(dldr):
    assert (dldr == True)

def test_dlfl(dlfl):
    assert (dlfl == True)