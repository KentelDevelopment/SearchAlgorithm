from flask import Flask,request,abort

app = Flask(__name__)

@app.route("/search")
def search():
	URLS = []
	TITLES =[]
	query = request.args.get("q")
	results = []
	if query != None:
		reader = open("results.txt","r").read()
		reader = reader.split("\n")
		for r in reader:
			try:
				title = r.split("?==+!")[0]
				link = r.split("?==+!")[1]
				URLS.insert(0,link)
				TITLES.insert(0,title)
			except:
				pass

		for t in TITLES:
			try:
				t.split(query)[1]
				results.insert(0,{"title":t,"url":URLS[int(TITLES.index(t))]})
			except:
				pass

		return str(results)





	else:
		abort(500)
	return ""

app.run(debug=True)