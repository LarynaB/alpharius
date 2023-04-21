from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)

@app.route('/')
def home():
    return '''
        <html>
            <head>
                <style>
                    /* Styles for the banner */
                    #banner {
                        width: 100%;
                        height: 150px;
                        background-color: #333;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                    }
                    #banner img {
                        max-height: 100%;
                        max-width: 100%;
                        object-fit: contain;
                    }
                    /* Styles for the navigation bar */
                    #nav {
                        width: 100%;
                        height: 50px;
                        background-color: #eee;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        list-style-type: none;
                        margin: 0;
                        padding: 0;
                    }
                    #nav li {
                        margin-right: 10px;
                    }
                    #nav li a {
                        color: #333;
                        text-decoration: none;
                    }
                    #nav li a:hover {
                        color: #555;
                        text-decoration: underline;
                    }
                </style>
            </head>
            <body>
                <div id="banner">
                    <img src="https://placekitten.com/1200/150" alt="cat image">
                </div>
                <ul id="nav">
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
                <h1>Hello, World!</h1>
            </body>
        </html>
    '''

#run the app
if __name__ == '__main__':
    app.run()
