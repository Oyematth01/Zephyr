from zephyr import app
from flask import render_template
# from zephyr.models import Item

@app.route('/')
@app.route('/home')
def home_page():
     social_links ={
        "twitter": "https://x.com/oyematth",
        "linkedin": "https://www.linkedin.com/in/matthew-oyelami-1223b5244/",
        "github": "https://github.com/Oyematth01",
        "instagram": "https://www.instagram.com/oyematth/",
        "medium": "https://medium.com/@oyematth"}
     return render_template('home.html', social_links=social_links)

# @app.route('/zephyr')
# def market_page():
#     items = Item.query.all()
#     return render_template('market.html', items=items)