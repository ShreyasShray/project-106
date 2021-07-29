import numpy as np
import csv
import plotly.express as px

def plotFigure():
    with open("data2.csv", newline = "") as f:
        reader = csv.DictReader(f)
        file_data = list(reader)

    fig = px.scatter(file_data, y = "Coffee in ml", x = "sleep in hours")
    fig["layout"]["yaxis"]["autorange"] = "reversed"
    fig.show()

def getDataSource(data_source):
    coffee_in_ml = []
    sleep_in_hours = []
    with open(data_source, newline = "") as f:
        reader = csv.DictReader(f)
        for data in reader:
            coffee_in_ml.append(float(data["Coffee in ml"]))
            sleep_in_hours.append(float(data["sleep in hours"]))
    return ({"x": coffee_in_ml, "y": sleep_in_hours})

def findCorrelation(data):
    correlation = np.corrcoef(data["x"], data["y"])
    print("Correlation between coffee in ml vs sleep in hours is " + str(correlation[0][1]))

def setup():
    result = getDataSource("data2.csv")
    findCorrelation(result)
    plotFigure()

setup()