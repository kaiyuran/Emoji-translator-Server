from flask import Flask, request, jsonify
from flask_cors import CORS
import random

def emojify(message):

    choiceWordDict = {
    #happy face
    "happy": "😊",
    "joy": "😊",
    "content": "😊",
    "smile": "😊",
    "grateful": "😊",
    "kind": "😊",
    "warm": "😊",
    "friendly": "😊",
    "pleasant": "😊",

    #laugh
    "laugh": "😂",
    "funny": "😂",
    "lol": "😂",
    "hilarious": "😂",
    "joke": "😂",
    "laughter": "😂",
    "giggle": "😂",
    "humor": "😂",
    "meme": "😂",
    "comedy": "😂",

    #heart
    "love": "❤️",
    "heart": "❤️",
    "affection": "❤️",
    "adore": "❤️",
    "romance": "❤️",
    "care": "❤️",
    "beloved": "❤️",
    "fondness": "❤️",
    "sweetheart": "❤️",

    #heart face
    "cute": "🥰",
    "adorable": "🥰",
    "sweet": "🥰",
    "crush": "🥰",
    "blush": "🥰",
    "heartwarming": "🥰",
    "charming": "🥰",
    "affectionate": "🥰",
    "darling": "🥰",


    "amazing": "😍",
    "admire": "😍",
    "wow": "😍",
    "beautiful": "😍",
    "attractive": "😍",
    "captivated": "😍",
    "enchanted": "😍",

    "think": "🤔",
    "ponder": "🤔",
    "wonder": "🤔",
    "curious": "🤔",
    "consider": "🤔",
    "question": "🤔",
    "reflect": "🤔",
    "speculate": "🤔",
    "doubt": "🤔",
    "analyze": "🤔",


    "grin": "😁",
    "excited": "😁",
    "positive": "😁",
    "enthusiasm": "😁",
    "joyful": "😁",
    "cheerful": "😁",
    "beam": "😁",
    "delight": "😁",

    "like": "👍",
    "approval": "👍",
    "agree": "👍",
    "okay": "👍",
    "support": "👍",
    "endorse": "👍",
    "respect": "👍",
    "commend": "👍",
    "thumb": "👍",
    "thumbs": "👍",

    "celebrate": "🎉",
    "party": "🎉",
    "event": "🎉",
    "fun": "🎉",
    "cheer": "🎉",
    "festivity": "🎉",
    "win": "🎉",
    "success": "🎉",
    "achievement": "🎉",

    "fire": "🔥",
    "hot": "🔥",
    "intense": "🔥",
    "awesome": "🔥",
    "trending": "🔥",
    "lit": "🔥",
    "energy": "🔥",
    "passion": "🔥",
    "power": "🔥",

    # Pizza
    "pizza": "🍕",
    "cheese": "🍕",
    "slice": "🍕",
    "italian": "🍕",
    "pepperoni": "🍕",

    # Burger
    "burger": "🍔",
    "cheeseburger": "🍔",
    "fries": "🍔",
    "grill": "🍔",
    "food": "🍔",

    # Taco
    "taco": "🌮",
    "mexican": "🌮",
    "salsa": "🌮",
    "spicy": "🌮",
    "guacamole": "🌮",

    # Sushi
    "sushi": "🍣",
    "fish": "🍣",
    "rice": "🍣",
    "soysauce": "🍣",
    "japanese": "🍣",

    # Ice Cream
    "icecream": "🍦",
    "dessert": "🍦",
    "vanilla": "🍦",
    "cone": "🍦",
    "frozen": "🍦",

    # Apple
    "apple": "🍎",
    "healthy": "🍎",
    "red": "🍎",
    "snack": "🍎",

    # Cake
    "cake": "🍰",
    "birthday": "🍰",
    "celebration": "🍰",

    # Donut
    "donut": "🍩",
    "donuts": "🍩",
    "glazed": "🍩",
    "glaze": "🍩",
    "sprinkles": "🍩",
    # Bread
    "bread": "🍞",
    "toast": "🍞",
    "bakery": "🍞",
    "sandwich": "🍞",
    "loaf": "🍞",

    # Watermelon
    "watermelon": "🍉",
    "fruit": "🍉",
    "refreshing": "🍉",
    "summer": "🍉",



    "eggplant": "🍆",
    "aubergine": "🍆",
    "banana": "🍌",
    "peach": "🍑",
    "cherries": "🍒",
    "strawberry": "🍓",
    "tomato": "🍅",
    "avocado": "🥑",
    "broccoli": "🥦",
    "carrot": "🥕",
    "corn": "🌽",
    "cucumber": "🥒",
    "lettuce": "🥬",
    "mushroom": "🍄",
    "pepper": "🌶️",
    "hotpepper": "🌶️",
    "potato": "🥔",
    "sweetpotato": "🍠",
    "croissant": "🥐",
    "baguette": "🥖",
    "pretzel": "🥨",
    "cheese": "🧀",
    "egg": "🥚",
    "bacon": "🥓",
    "pancakes": "🥞",
    "poultryleg": "🍗",
    "chicken": "🍗",
    "meat": "🍖",
    "bacon": "🥓",

    "sad": "😢",
    "angry": "😡",
    "mad": "😡",
    "fury": "😡",
    "rage": "😡",
    "disgust": "🤢",
    "sick": "🤢",
    "vomit": "🤢",
    "gross": "🤢",
    "nausea": "🤢",
    "unhappy": "😞",
    "depressed": "😞",
    "miserable": "😞",
    "gloomy": "😞",
    "despair": "😞",
    "spy": "🕵️",
    "detective": "🕵️",
    "sleuth": "🕵️",
    "investigate": "🕵️",
    "search": "🕵️",
    "inspect": "🕵️",
    "dance": "💃",
    "dancer": "💃",
    "ballerina": "💃",
    "tango": "💃",
    "dancing": "🕺",
    "twin": "👯",
    "sisters": "👯",
    "twins": "👯",
    "ballet": "🩰",
    "pointeshoes": "🩰",
    "balletshoes": "🩰",
    "shoes": "👟",
    "heels": "👠",
    "finish": "🏁",
    "sign": "🚩",
    "leaf": "🍃",
    "plant": "🌱",
    "flower": "🌸",
    "blossom": "🌸",
    "rose": "🌹",
    "tulip": "🌷",
    "sunflower": "🌻",
    "daisy": "🌼",
    "hibiscus": "🌺",
}

    message = message.strip('"')
    message = message.strip("'")
    finalMessage = []
    print("message is:",message)
    message = message.split(" ")
    for word in message:
        try:
            formWord = word.lower()
            if formWord[-1] == ".":
                finalMessage.append(word[:-1]  + (choiceWordDict[formWord[:-1]] * random.randint(1,3)) +".")
            else:
                finalMessage.append(word  + choiceWordDict[word.lower()])

            

        except:
            finalMessage.append(word)
            pass
    print(finalMessage)
    final =" ".join([str(item) for item in finalMessage])
    return final



app = Flask(__name__)
CORS(app)

#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=33303)


@app.route('/getemoji', methods=['GET'])
# @cross_origin()
def get_random_emoji():
    # Get the 'letter' parameter from the URL
    message = request.args.get('message')
    print(message)


    final = emojify(message)
    # print(final)
    final = jsonify({"message": final})# emoji in JSON format
    # final = jsonify({final: 1})# emoji in JSON format

    return final

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(port=33303)
    # app.run(host='0.0.0.0', port=33303)