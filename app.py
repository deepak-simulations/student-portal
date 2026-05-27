from flask import Flask, render_template,request
#Flask create web pages 
#render_template shows HTML pages
#request receives user input 
import sqlite3
app = Flask(__name__)

# when someone opens the website homepage show them login.html page
@app.route('/')
def home():
    return render_template("login.html")

# when student clicks check button
@app.route('/check',methods=['POST'])
def check():
    ID = request.form['ID']
    Name = request.form['Name']

    conn = sqlite3.connect("college.db")

    cursor = conn.cursor()

    query = """
    SELECT status
    FROM students
    WHERE ID = ? 
    AND Name = ?
    """

    cursor.execute(query,(ID,Name))
    data = cursor.fetchone()

    conn.close()

    return render_template("result.html", data=data)

if __name__=='__main__':
    app.run(debug=True)

    