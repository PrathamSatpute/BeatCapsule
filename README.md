#   BeatCapsule

This project fetches a user's Spotify listening data and creates visualizations using Python, Flask, and Matplotlib.

## Features

- Authenticates with Spotify API
- Fetches user's top artists, top tracks, and recent listening history
- Creates visualizations for top artists and listening time
- Displays results on a web page

## Installation

1. Clone the repository:
   https://github.com/PrathamSatpute/BeatCapsule.git

2. Create a virtual environment and activate it:
   python -m venv venv
   venv\Scripts\activate

3. Install the required packages:
   pip install -r requirements.txt

4. Set up your Spotify Developer account and create an app to get your Client ID and Client Secret.
   Go to -> https://developer.spotify.com/
   Login through your Spotify account
   Profile -> Dashboard -> Create App -> Fill the details and put redirecting URL as - http://localhost:5000/callback -> Save the details.
   Go to App from Dashboard -> Setting -> You'll get CLient ID and Client Secret ID.
   Put this credentials in spotify_auth.py file.

## Usage

1. Run the Flask application:
   python main.py

2. Open a web browser and go to http://localhost:5000

3. Log in with your Spotify account and view your personalized visualizations.

       
