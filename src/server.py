from flask import Flask, render_template, jsonify, request

from src.person_scoring import calculate_person_similarity

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/scores', methods=['GET'])
def calculate():
    score, name_score, bd_scores = calculate_person_similarity(
        (request.args.get('name1'), request.args.get('birth_date1')),
        (request.args.get('name2'), request.args.get('birth_date2')))
    return jsonify({
        'success': True,
        'score': score,
        'name-score': name_score,
        'year-score': bd_scores[0],
        'month-score': bd_scores[1],
        'day-score': bd_scores[2]
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
