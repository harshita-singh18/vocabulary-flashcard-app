from __future__ import annotations

from flask import Flask, render_template


def create_app() -> Flask:
    app = Flask(__name__)

    app.flashcards: list[dict] = [  # type: ignore[attr-defined]
        {"word": "Ubiquitous", "definition": "Present, appearing, or found everywhere."},
        {"word": "Ephemeral", "definition": "Lasting for a very short time."},
        {"word": "Eloquent", "definition": "Fluent or persuasive in speaking or writing."},
        {"word": "Tenacious", "definition": "Tending to keep a firm hold; persistent."},
        {"word": "Ambiguous", "definition": "Open to more than one interpretation; unclear."},
    ]

    @app.route("/")
    def home():
        return render_template("home.html", flashcards=app.flashcards)

    return app


if __name__ == "__main__":
    create_app().run(debug=True, port=5000)
