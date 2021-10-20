from flask import Flask, render_template, url_for, request
import pandas as pd
import random

# data path to data
data_path = "~/python/projects/content-db/data/test_1_combined.csv"
df = pd.read_csv(data_path)

app = Flask(__name__)

@app.route('/')
def index():
    # sample 5 rows from data frame
    df_sampled = df.sample(n=5)
    return render_template("index.html", content=df_sampled)

@app.route('/db.html')
def db():
    return render_template("db.html", content=df)

@app.route('/search.html', methods=['GET', 'POST'])
def serach():
    if request.method == "POST":
        options = request.form.getlist('source')
        print(options)
        if len(options) == 1:
            # options is a list 
            df_searched = df[df['source'] == options[0]]
            print(df_searched.shape)
            try:
                return render_template("search.html", data = options, dataFrame = df_searched)
            except:
                pass
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug = True)
