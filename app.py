from flask import Flask, request, render_template 
from flask import jsonify

app = Flask(__name__) 
@app.route("/", methods=["POST", "GET"]) 
def home(): 
	return render_template("index.html") 

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
	search = request.args.get('q')
	f = open("words_alpha.txt")
	lines = f.read().splitlines()
	words = [word for word in lines if word.lower().startswith(search)][:5]
	return jsonify(matching_results=words)


@app.route('/result', methods=['GET'])
def search_result():
	search = request.args.get('autocomplete')
	f = open("words_alpha.txt")
	lines = f.read().splitlines()
	words = [word for word in lines if word.lower().startswith(search)][:15]
	if request.args.get('itr'):
		words = [search]
	return render_template("result.html", words=words, query=search) 

if __name__ == '__main__': 
	app.run(debug=False) 
