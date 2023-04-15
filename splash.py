#class name from module
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <html>
            <head>
                <style>
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
                </style>
            </head>
            <body>
                <div id="banner">
                    <img src="https://placekitten.com/1200/150" alt="cat image">
                </div>
                <h1>Hello, World!</h1>
            </body>
        </html>
    '''
#run the app
if __name__ == '__main__':
    app.run()

