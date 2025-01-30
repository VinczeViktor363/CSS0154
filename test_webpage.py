import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def load_html():
    with open("index.html", encoding="utf-8") as f:
        return BeautifulSoup(f, "html.parser")

def test_html_structure(load_html):
    assert load_html.html is not None, "A dokumentumnak kell tartalmaznia <html> elemet."
    assert load_html.head is not None, "A dokumentumnak kell tartalmaznia <head> elemet."
    assert load_html.body is not None, "A dokumentumnak kell tartalmaznia <body> elemet."

def test_language_attribute(load_html):
    assert load_html.html.has_attr("lang"), "A <html> elemnek kell rendelkeznie 'lang' attribútummal."
    assert load_html.html["lang"] == "hu", "A nyelvi beállításnak 'hu' értékűnek kell lennie."

def test_charset(load_html):
    meta_tag = load_html.find("meta", charset=True)
    assert meta_tag is not None, "A dokumentumnak tartalmaznia kell egy meta charset beállítást."
    assert meta_tag["charset"].lower() == "utf-8", "A karakterkódolásnak 'utf-8'-nak kell lennie."

def test_title(load_html):
    title = load_html.title
    assert title is not None, "Az oldalnak tartalmaznia kell egy <title> elemet."
    assert title.string.strip() == "Rugalmas dobozok", "Az oldal címének 'Rugalmas dobozok'-nak kell lennie."

def test_container_exists(load_html):
    container = load_html.find("div", class_="container")
    assert container is not None, "A fő konténer hiányzik."

def test_boxes_exist(load_html):
    boxes = load_html.find_all("div", class_="box")
    assert len(boxes) == 2, "Az oldalon pontosan két doboznak kell lennie."

def test_css_link(load_html):
    link = load_html.find("link", {"rel": "stylesheet"})
    assert link is not None, "A CSS fájl hiányzik."
    assert link["href"] == "style.css", "A CSS fájl neve helytelen."

def test_background_color():
    with open("style.css", encoding="utf-8") as f:
        css_content = f.read()
    assert "background-color: blueviolet;" in css_content, "A háttérszín nincs megfelelően beállítva."

def test_box_background_color():
    with open("style.css", encoding="utf-8") as f:
        css_content = f.read()
    assert "background-color: aqua;" in css_content, "A belső dobozok háttérszíne nincs megfelelően beállítva."
