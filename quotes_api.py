from flask import Flask, jsonify
import json, time

app = Flask(__name__)

# Love quotes data
love_quotes = {
    "love_quotes": [
        "In a sea of people, my eyes will always search for you.",
        "You are the love that came without a warning, and I cherish every moment with you.",
        "With every heartbeat, I fall deeper in love with you.",
        "You are my favorite chapter in this beautiful story called life.",
        "Your laughter is my favorite melody.",
        "When I hold your hand, I feel like I’m holding the entire universe.",
        "You are the reason I wake up every morning with a smile.",
        "Every love song reminds me of you and makes my heart sing.",
        "You are the dream I never want to wake up from.",
        "In your eyes, I see my forever.",
        "You are the most beautiful part of my day.",
        "Your love is my favorite adventure.",
        "With you, every moment is a treasure.",
        "You are the sparkle in my life and the sunshine in my soul.",
        "I never knew true happiness until I met you.",
        "You make my heart dance with joy.",
        "In your embrace, I have found my home.",
        "You are the reason I believe in magic.",
        "Every day with you is a wonderful addition to my life’s journey.",
        "You are my heart’s delight and my greatest joy.",
        "You are the peanut butter to my jelly, the stars to my sky.",
        "With you, love is not just a word; it’s a feeling that fills my soul.",
        "You are my greatest blessing.",
        "When I look at you, I see my forever.",
        "You make every day feel like a fairytale.",
        "Together, we create a beautiful symphony of love.",
        "Your smile lights up my darkest days.",
        "You are my sweet escape from reality.",
        "With you, I have everything I need.",
        "You are the reason I believe in love at first sight.",
        "You are the magic that makes my heart flutter.",
        "In a world full of chaos, you are my peace.",
        "You are my sunshine, brightening even the cloudiest days.",
        "You complete my life in ways I never knew were possible.",
        "Your love is my guiding star.",
        "With you, I have found my happy place.",
        "You are my favorite hello and my hardest goodbye.",
        "Every moment spent with you is a moment I cherish.",
        "You are the reason I write love stories.",
        "Your love is the sweetest melody in my heart.",
        "You are my dream come true, and I never want to wake up.",
        "Together, we can conquer the world.",
        "You are the light that brightens my path.",
        "With you, I feel like I can do anything.",
        "You are my heart's desire, my soul's companion.",
        "Your love is a beautiful journey I never want to end.",
        "You are the reason I smile every day.",
        "You are my forever love, my sweet escape.",
        "In your arms, I have found my safe haven.",
        "You are my universe, my everything.",
        "With every kiss, you steal my heart all over again.",
        "You are the inspiration behind my every heartbeat.",
        "You are the sweetest chapter in my life’s story.",
        "With you, love feels effortless and beautiful.",
        "You are the heartbeat of my existence.",
        "Your love is my favorite fairy tale.",
        "You are the missing piece to my puzzle.",
        "In your eyes, I see a love that transcends time.",
        "You are my greatest adventure, my sweetest journey.",
        "With you, I am home.",
        "You are the reason love songs were written.",
        "Every day with you is a new page in our love story.",
        "You are my sunshine and my moonlight.",
        "In a world of choices, I choose you always.",
        "Your love is the sweetest gift I've ever received.",
        "You are my heart's melody, my soul's song.",
        "With you, I have discovered true happiness.",
        "You are the love I always dreamed of.",
        "Every moment with you is a treasure to cherish.",
        "You are the smile I look forward to every day.",
        "With you, my heart is forever entwined.",
        "You are my inspiration, my heart's delight.",
        "In your love, I have found my forever.",
    ]
}


@app.route("/", methods=["GET"])
def get_love_quotes():
    return json.dumps(love_quotes)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
