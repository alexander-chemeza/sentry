import sentry_sdk
from flask import Flask, request
from sentry_sdk.integrations.flask import FlaskIntegration
import logging

sentry_sdk.init(
    dsn="https://3038ebb0fb5497b533a64c31b9437cac@o4506270132404224.ingest.sentry.io/4506270505107456",
    integrations=[FlaskIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

app = Flask(__name__)


@app.route('/debug-sentry')
def trigger_error():
    divizion_by_zero = 1 / 0

@app.route('/test_type')
def test_type():
    user_id = request.args.get('user_id')
    user_id = float(user_id)

@app.route('/test_logging')
def test_logging():
    logging.error("error to log")


if __name__ == '__main__':
    app.run()