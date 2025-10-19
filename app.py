from flask import Flask, render_template, request

app = Flask(__name__)

# ✅ 50 Fun Facts about Numbers
facts = {
    1: "1 is the first natural number and represents unity.",
    2: "2 is the only even prime number.",
    3: "3 is the number of spatial dimensions we live in.",
    4: "4 is the number of seasons in a year.",
    5: "5 is the number of human senses.",
    6: "6 is considered a perfect number because 1 + 2 + 3 = 6.",
    7: "7 is often called a lucky number and appears in many cultures.",
    8: "8 is the number of planets in our solar system.",
    9: "9 is a magic number — any multiple of 9’s digits add up to 9.",
    10: "10 is the base of our decimal number system.",
    11: "11 is the smallest two-digit palindrome.",
    12: "12 months make a year and 12 zodiac signs exist.",
    13: "13 is often considered unlucky in Western culture.",
    14: "14 is the atomic number of silicon.",
    15: "15 minutes of fame — a phrase coined by Andy Warhol.",
    16: "16 is a square number (4 × 4).",
    17: "17 is the number of syllables in a traditional haiku.",
    18: "18 is the legal voting age in most countries.",
    19: "19 is a prime number and the atomic number of potassium.",
    20: "20 is the number of faces on an icosahedron in geometry.",
    21: "21 is the legal drinking age in the U.S.",
    22: "22 divided by 7 is a famous approximation for π (pi).",
    23: "23 is known as the '23 enigma' in conspiracy theories.",
    24: "24 hours make one full day.",
    25: "25 is the square of 5.",
    26: "26 is the number of letters in the English alphabet.",
    27: "27 is 3 cubed (3 × 3 × 3).",
    28: "28 is the number of days in February (in a common year).",
    29: "29 is the number of days in February during a leap year.",
    30: "30 degrees Celsius is often considered warm and pleasant.",
    31: "31 is the maximum number of days in a calendar month.",
    32: "32°F is the freezing point of water.",
    33: "33 is believed to be a 'master number' in numerology.",
    34: "34 is the number of bones in a cat’s tail (on average).",
    35: "35mm film was once the standard for photography and cinema.",
    36: "36 is the number of inches in a yard.",
    37: "37°C is the normal human body temperature.",
    38: "38 is the atomic number of strontium.",
    39: "39 is the number of books in the Old Testament.",
    40: "40 days and nights of rain fell in the story of Noah’s Ark.",
    41: "41 is the atomic number of niobium.",
    42: "42 is the 'Answer to the Ultimate Question of Life' (Hitchhiker’s Guide).",
    43: "43 is a prime number and the atomic number of technetium.",
    44: "44 is the number of U.S. President Barack Obama.",
    45: "45 RPM records were used for singles in vinyl music.",
    46: "46 is the total number of human chromosomes.",
    47: "47 is often used as an Easter egg number in pop culture (especially Star Trek).",
    48: "48 hours make two days.",
    49: "49 is 7 squared (7 × 7).",
    50: "50 is the golden anniversary — celebrating 50 years of marriage."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_fact', methods=['POST'])
def get_fact():
    try:
        number = int(request.form['number'])
        fact = facts.get(number, f"Sorry! No fun fact found for {number}. Try a number between 1 and 50.")
        return render_template('result.html', number=number, fact=fact)
    except ValueError:
        return render_template('result.html', number=None, fact="Please enter a valid number!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
