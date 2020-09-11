from flask import Flask, request
from calculator.ippt import get_score

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    pushups = int(request.args.get("pushups", 0))
    situps = int(request.args.get("situps", 0))
    run_secs = int(request.args.get("run", 0))

    score = get_score(
        age=18,
        pushups=pushups,
        situps=situps,
        run_secs=run_secs,
    )

    return score
