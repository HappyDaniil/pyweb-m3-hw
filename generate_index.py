# coding: utf-8
"<meta charset='utf-8'>"
from horoscope import generate_prophecies
from datetime import datetime as dt
from generate_about import save_page

def generate_page(head, body):
	page = "<html>" + head + body + "</html>"
	return page

def generate_head(title):
	head = "<title>" + title + "</title>"   
	return "<head>" + head + "</head>"

def generate_body(header, paragraphs,href):
	body = "<h1>" + header + "</h1>"
	i = 0
	while i < len(paragraphs):
		body = body + "<p>" + paragraphs[i] + "</p>"
		i = i + 1
	href = "about.html"
	body = body + "<a href = about.html> О реализации.</a>"
	return "<body>" + body + "</body>"

def save_page(title, header, paragraphs, output="index.html"):
	fp = open(output, "w", encoding="utf-8")
	today = dt.now().date()
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header=header, paragraphs=paragraphs,href="about.html" )
		)
	print(page, file=fp)
	fp.close()
today = dt.now().date()
save_page(
    title="Гороскоп на сегодня",
    header="Что день " + str(today) + " готовит",
    paragraphs=generate_prophecies(),
)
#C 31-страницы моя попытка добавить эбаут,заканчивается она присваением сегодняшней даты.