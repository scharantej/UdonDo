
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Dataframe of Japanese restaurants and their locations
restaurants = pd.read_csv('japanese_restaurants.csv')

@app.route('/')
def index():
    return render_template('index.html', restaurants=restaurants)

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search']
    filtered_restaurants = restaurants[restaurants['name'].str.contains(search_term)]
    return render_template('search_results.html', restaurants=filtered_restaurants)

@app.route('/restaurant/<restaurant_id>')
def restaurant(restaurant_id):
    restaurant_info = restaurants[restaurants['id'] == int(restaurant_id)]
    return render_template('restaurant.html', restaurant=restaurant_info)

if __name__ == '__main__':
  app.run()
