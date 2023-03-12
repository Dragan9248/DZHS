import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/cards")
def get_cards():
    response = requests.get('https://api.hearthstonejson.com/v1/121569/ruRU/cards.collectible.json')
    cards = response.json()
    card_info = []
    for card in cards:
        card_info.append({
            'name': card['name'],
            'type': card['type'],
            'rarity': card['rarity'],
            'cost': card.get('cost', 0)  
        })
    return render_template('cards.html', card_info=card_info)

if __name__ == '__main__':
    app.run(
        port=8080,
        debug=True
    )