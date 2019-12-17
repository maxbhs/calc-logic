from flask import Flask, request, jsonify

app = Flask(__name__) 

def change_mult_div_char(expr):
	
	exprlist = list(expr)

	for i, c in enumerate(exprlist):
		if c == "x":
			exprlist[i] = "*"
		elif c == "÷":
			exprlist[i] = "/"
	

	expr = ''.join(exprlist)
	
	return expr

	
@app.route("/", methods=['POST'])
def calculator():

	expr = request.get_json()['expr']
	expr = change_mult_div_char(expr)
	result = eval(expr)
	expr= ""

	return jsonify(
		expr=expr,
		result=result
    	)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
