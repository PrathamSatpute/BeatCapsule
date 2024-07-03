from flask import Flask, render_template, redirect, request, session
from spotify_auth import get_auth_manager
from data_fetcher import fetch_spotify_data
from data_processor import process_data
from visualizer import create_visualizations

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a real secret key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    auth_manager = get_auth_manager()
    auth_url = auth_manager.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    auth_manager = get_auth_manager()
    token = auth_manager.get_access_token(request.args.get("code"), as_dict=False)
    session['token_info'] = auth_manager.get_cached_token()
    return redirect('/visualize')

@app.route('/visualize')
def visualize():
    if 'token_info' not in session:
        return redirect('/login')
    
    token_info = session['token_info']
    raw_data = fetch_spotify_data(token_info)
    processed_data = process_data(raw_data)
    visualizations = create_visualizations(processed_data)
    
    return render_template('visualizations.html', visualizations=visualizations)

if __name__ == '__main__':
    app.run(debug=True)