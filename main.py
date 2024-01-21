from flask import Flask, render_template, url_for, request, redirect
import matplotlib.pyplot as plt
import mpld3
import numpy as np

app = Flask(__name__)

 
c = [0,0]
r = []
nums = []

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        rows = request.form.get("rows")
        for i in range(int(rows)):
            r.append(0)
        return redirect(url_for('table'))
    return render_template('home.html')

@app.route('/table', methods = ["GET", "POST"])
def table():
    if request.method == "POST":
        for i in range(len(r)):
            for n in range(len(c)):
                nums.append(request.form.get(str(i+1) + " + " + str(n+1)))
                print(str(i+1) + " + " + str(n+1))
                print(nums)

        return redirect(url_for('graph'))
    return render_template('table.html', c = c, r = r)

@app.route('/graph', methods = ["GET", "POST"])
def graph():
    x = []
    y = []
    cr = len(c) * len(r)
    for i in range(cr):
        if i == 0 or i % 2 == 0:
            x.append(nums[i])
        else:
            y.append(nums[i])

    
    # Create a line chart
    plt.figure(figsize=(8, 6))
    fig = plt.plot(x, y, marker='o', linestyle='-')
    
    # Add annotations
    for i, (xi, yi) in enumerate(zip(x, y)):
        plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')
    
    # Add title and labels
    plt.title('Line Chart with Annotations')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    
    # Display grid
    plt.grid(True)
    
    # Show the plot
    plt.show()
    plt.savefig('graph.png')

    return render_template("graph.html")



if __name__ == '__main__':
    app.run('0.0.0.0', 12345)