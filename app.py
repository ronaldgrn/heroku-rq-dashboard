from flask import Flask, redirect
import rq_dashboard
from decouple import config

app = Flask(__name__)
app.config.from_object(rq_dashboard.default_settings)
app.config['REDIS_URL'] = config('REDIS_URL', 'localhost')

app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")


@app.route('/')
def hello_world():
    return redirect("/rq")


if __name__ == '__main__':
    app.run()
