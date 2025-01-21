from flask import Flask, render_template
import sqlite3
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="pass@123",
    database="ecell_db"
)
mycursor = mydb.cursor()
mycursor1 = mydb.cursor()


@app.route('/')
@app.route('/index.html')
def index():
    # Fetch image paths from the database


    image_paths = fetch_image_paths()
    print(image_paths)

    # Pass image_paths to the HTML template
    return render_template('index.html', image_path=image_paths[0])


def fetch_image_paths():
    # Fetch image paths from the database
    mycursor.execute("SELECT img_path FROM images")
    image_paths = [row[0] for row in mycursor.fetchall()]


    return image_paths



@app.route("/about.html")
def about():
    return render_template('about.html')


@app.route("/blog-home.html")
def bloghome():
    return render_template('blog-home.html')


@app.route("/blog-post.html")
def blodpost():
    return render_template('blog-post.html')


@app.route("/contact.html")
def contact():
    return render_template('contact.html')


@app.route("/faq.html")
def faq():
    d1 = data_fetching()
    return render_template('faq.html',first_txt = d1[0][3],second_txt = d1[1][3],third_txt = d1[2][3])

def data_fetching():
    mycursor1.execute("select * from faq")
    data = mycursor1.fetchall()
    return data
@app.route("/portfolio-item.html")
def portfolioitem():
    return render_template('portfolio-item.html')

@app.route("/portfolio-overview.html")
def portfoliooverview():
    return render_template('portfolio-overview.html')

@app.route("/pricing.html")
def pricing():
    return render_template('pricing.html')

if __name__ == '__main__':
    app.run(debug=True)
