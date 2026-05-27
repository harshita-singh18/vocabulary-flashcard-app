from __future__ import annotations

from flask import Flask, render_template, request


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

    @app.route("/study")
    def study():
        total = len(app.flashcards)
        try:
            idx = int(request.args.get("idx", 0))
        except ValueError:
            idx = 0
        idx = max(0, min(idx, total - 1))
        next_idx = (idx + 1) % total
        return render_template(
            "study.html",
            card=app.flashcards[idx],
            idx=idx,
            next_idx=next_idx,
            total=total,
        )

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
