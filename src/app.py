from flask import Flask
from config import config
from flask_cors import CORS
# Routes
from routes import Bills

app = Flask(__name__)

CORS(app)

def page_not_found(error):
    return "<h1>Not foung page</h1>", 404

if __name__ == "__main__":
        
    app.config.from_object(config['development'])

    app.register_blueprint(Bills.main,url_prefix='/api/bills')
   
    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, host='0.0.0.0', port=5000)
