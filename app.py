from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():

    # Load current count
    counter_read_file = open("count.txt", "r")
    count = int(counter_read_file.read())
    counter_read_file.close()

    # Increment the count
    count += 1

    # Overwrite the count
    counter_write_file = open("count.txt", "w")
    counter_write_file.write(str(count))
    counter_write_file.close()

    # Render HTML with count variable
    return render_template("index.html", count=count)

@app.route('/', methods=['POST'])
def my_form_post():
    # Load current count
    counter_read_file = open("count.txt", "r")
    count = int(counter_read_file.read())
    counter_read_file.close()

    text = request.form['text']

    corona_data = 'https://corona.dnsforfamily.com/graph.png?c='+text
    print(corona_data)
    return render_template("index.html", image=corona_data, count=count)

if __name__ == "__main__":
    app.run()