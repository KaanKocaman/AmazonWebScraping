import matplotlib
matplotlib.use('Agg')
import json
import matplotlib.pyplot as plt
from collections import defaultdict
from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def index():
    # Read the JSON file
    with open('AmazonVeri.json', 'r') as file:
        data = json.load(file)

    # Calculate average price for each brand
    brand_prices = defaultdict(list)
    for item in data:
        brand_prices[item['Marka']].append(float(item['Fiyat']))  # Convert price to float

    average_prices = {brand: sum(prices) / len(prices) for brand, prices in brand_prices.items()}

    # Create column chart
    plt.bar(average_prices.keys(), average_prices.values())
    plt.xlabel('Marka')
    plt.ylabel('Ortalama Fiyat')
    plt.title('Markaların Ortalama Fiyatları')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot as an image
    chart_image = 'chart.png'
    plt.savefig(chart_image)

    # Clear the plot to avoid memory issues
    plt.clf()

    # Return the image in the response
    with open(chart_image, 'rb') as image_file:
        image_data = image_file.read()

    return Response(image_data, mimetype='image/png')
def run_flask():
    app.run(debug=True)

if __name__ == '__main__':
    run_flask()