import numpy as np
import csv
import plotly.express as px

def plotFigure():
    with open("data1.csv", newline = "") as f:
        reader = csv.DictReader(f)
        file_data = list(reader)

    fig = px.scatter(file_data, y = "Days Present", x = "Marks In Percentage")
    fig["layout"]["xaxis"]["autorange"] = "reversed"
    fig["layout"]["yaxis"]["autorange"] = "reversed"
    fig.show()

def getDataSource(data_source):
    marks_in_percentage = []
    Days_present = []
    with open(data_source, newline = "") as f:
        reader = csv.DictReader(f)
        for data in reader:
            marks_in_percentage.append(float(data["Marks In Percentage"]))
            Days_present.append(float(data["Days Present"]))
    return ({"x": marks_in_percentage, "y": Days_present})

def findCorrelation(data):
    correlation = np.corrcoef(data["x"], data["y"])
    print("Correlation between days present vs marks in percentage is " + str(correlation[0][1]))

def setup():
    result = getDataSource("data1.csv")
    findCorrelation(result)
    plotFigure()

setup()