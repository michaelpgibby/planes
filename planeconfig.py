from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Load the initial configuration from web_config.json
with open('web_config.json', 'r') as f:
    config_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', config=config_data)

@app.route('/update_config', methods=['POST'])
def update_config():
    if request.method == 'POST':
        new_config = request.form.to_dict()
        # Update the config_data dictionary with the new values
        config_data.update(new_config)
        # Save the updated config back to web_config.json
        with open('web_config.json', 'w') as f:
            json.dump(config_data, f, indent=4)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)