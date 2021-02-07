from flask import Flask, render_template, jsonify
from json import load

app = Flask(__name__)
with open('story.json') as f:
    story_dict = load(f)

@app.route('/')
def home():
    return render_template(
        'home.html'
        )

@app.route('/story/<string:str_id>')
def story(str_id):
    try:
        story_node = story_dict[str_id]
        return render_template(
            'story.html', 
            blocktext=story_node['text'],
            str_id_A=story_node['A']['str_id'],
            option_A=story_node['A']['text'],
            str_id_B=story_node['B']['str_id'],
            option_B=story_node['B']['text']
            )
    except:
        return jsonify('Woops, something went wrong.'), 404


if __name__ == '__main__':
    app.run(debug=True)