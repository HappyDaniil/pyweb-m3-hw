"<meta charset='utf-8'>"
def generate_page(head, body):
	page = "<html>" + head + body + "</html>"
	return page

def generate_head(title):
	head = "<title>" + title + "</title>"   
	return "<head>" + head + "</head>"

def generate_body(header,body,href):
	body = "<h1>" + header + "</h1>"
	body =  "<p>" "О чём всё это" "</p>"
	body = "< img src= овен.png width= 100 ></img>"
	# t = "<ul>(Утром,днём,вечером,после обеда,перед сном )</ul>"
	# a = "<ul>(Ожидайте,предостерегайтесь,будьте открыты для) </ul>"
	# p = "<ul>(гостей из забытого прошлого,встреч со старыми знакомыми,неожиданного праздника,приятных перемен) </ul>"
	Времена_дня = t = "<ul>(Утром,днём,вечером,после обеда,перед сном )</ul>"
	Глаголы = a = "<ul>(Ожидайте,предостерегайтесь,будьте открыты для) </ul>"
	События = p = "<ul>(гостей из забытого прошлого,встреч со старыми знакомыми,неожиданного праздника,приятных перемен) </ul>"
	body = "<ol>Времена_дня(),Глаголы(),События()</ol>"
	href = "index.html"
	body = "<a href = index.html> Вернуться на главную страницу </a>"
	return "<body>" + body + "</body>"

def save_page(output="about.html"):
	header="О чём всё это."
	title="Гороскоп на сегодня"
	href = "index.html"
	Времена_дня = t = "<ul>(Утром,днём,вечером,после обеда,перед сном )</ul>"
	Глаголы = a = "<ul>(Ожидайте,предостерегайтесь,будьте открыты для) </ul>"
	События = p = "<ul>(гостей из забытого прошлого,встреч со старыми знакомыми,неожиданного праздника,приятных перемен) </ul>"
	body = "<ol>Времена_дня(),Глаголы(),События()</ol>"
	fp = open(output, "w", encoding="utf-8")
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header,body,href)
		)
	print(page, file=fp)
	fp.close()
save_page()
# def gen_page(title,paragraphs,href, output = "about.html"):
# 	fp = open(output,"w", encoding="utf-8" )
# 	head = "<title>" + "О чём всё это" + "</title>" 
# 	# paragraphs = <p> <a href = "about.html">О реализации </a> </p>
