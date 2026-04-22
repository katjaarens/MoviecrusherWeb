
from flask import Flask, render_template, request, redirect, session, url_for
from database import Database

app = Flask(__name__)
app.secret_key = "supersecret"
db = Database("moviecrusher.db")


def require_login():
    return "user" in session


@app.route("/")
def home():
    if require_login():
        return redirect("/dashboard")
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        user = db.login(email)
        if user:
            session["user"] = {
                "id": user[0],
                "name": user[1],
                "email": user[2],
                "age": user[3],
            }
            return redirect("/dashboard")
        return render_template("login.html", error="E-Mail nicht gefunden")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]

        user_id = db.add_user(name, email, int(age))
        session["user"] = {
            "id": user_id,
            "name": name,
            "email": email,
            "age": age,
        }
        return redirect("/dashboard")

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/dashboard")
def dashboard():
    if not require_login():
        return redirect("/login")

    user = session["user"]
    stats = db.get_stats(user["id"])
    return render_template("dashboard.html", user=user, stats=stats)


@app.route("/search", methods=["GET", "POST"])
def search():
    if not require_login():
        return redirect("/login")

    user = session["user"]
    results = []
    description = None
    message = None

    if request.method == "POST":
        keyword = request.form["keyword"]
        results = db.search_movies(keyword)

        if not results:
            message = "Keine Filme gefunden."
        elif len(results) == 1:
            description = db.get_movie_description(results[0][0])

    all_titles = db.get_all_titles()
    return render_template(
        "search.html",
        user=user,
        results=results,
        description=description,
        all_titles=all_titles,
        message=message,
    )


@app.route("/rate", methods=["GET", "POST"])
def rate():
    if not require_login():
        return redirect("/login")

    user = session["user"]
    message = None
    description = None

    if request.method == "POST":
        title = request.form["title"]
        rating = request.form["rating"]

        results = db.search_movies(title)
        if not results:
            message = "Film nicht gefunden."
        else:
            movie_id = results[0][0]
            db.add_rating(user["id"], movie_id, float(rating))
            description = db.get_movie_description(movie_id)
            message = f"Bewertung gespeichert für {results[0][1]}"

    all_titles = db.get_all_titles()
    return render_template(
        "rate.html",
        user=user,
        all_titles=all_titles,
        message=message,
        description=description,
    )


@app.route("/watchlist")
def watchlist():
    if not require_login():
        return redirect("/login")

    user = session["user"]
    wl = db.get_watchlist(user["id"])
    return render_template("watchlist.html", user=user, watchlist=wl)


@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    if not require_login():
        return redirect("/login")

    message = None

    if request.method == "POST":
        title = request.form["title"]
        genre = request.form["genre"]
        year = request.form["year"]
        description = request.form["description"]

        movie_id = db.add_movie(title, genre, int(year))
        if description:
            db.add_description(movie_id, description)

        message = f"Film hinzugefügt (ID: {movie_id})"

    return render_template("add_movie.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, session, url_for
from database import Database

app = Flask(__name__)
app.secret_key = "supersecret"
db = Database("moviecrusher.db")


def require_login():
    return "user" in session


@app.route("/")
def home():
    if require_login():
        return redirect("/dashboard")
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        user = db.login(email)
        if user:
            session["user"] = {
                "id": user[0],
                "name": user[1],
                "email": user[2],
                "age": user[3],
            }
            return redirect("/dashboard")
        return render_template("login.html", error="E-Mail nicht gefunden")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]

        user_id = db.add_user(name, email, int(age))
        session["user"] = {
            "id": user_id,
            "name": name,
            "email": email,
            "age": age,
        }
        return redirect("/dashboard")

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/dashboard")
def dashboard():
    if not require_login():
        return redirect("/login")

    user = session["user"]
    stats = db.get_stats(user["id"])
    return render_template("dashboard.html", user=user, stats=stats)


@app.route("/search", methods=["GET", "POST"])
def search():
    if not require_login():
        return redirect("/login")

    user = session["user"]
    results = []
    description = None
    message = None

    if request.method == "POST":
        keyword = request.form["keyword"]
        results = db.search_movies(keyword)

        if not results:
            message = "Keine Filme gefunden."
        elif len(results) == 1:
            description = db.get_movie_description(results[0][0])

    all_titles = db.get_all_titles()
    return render_template(
        "search.html",
        user=user,
        results=results,
        description=description,
        all_titles=all_titles,
        message=message,
    )


@app.route("/rate", methods=["GET", "POST"])
def rate():
    if not require_login():
        return redirect("/login")

    user = session["user"]
    message = None
    description = None

    if request.method == "POST":
        title = request.form["title"]
        rating = request.form["rating"]

        results = db.search_movies(title)
        if not results:
            message = "Film nicht gefunden."
        else:
            movie_id = results[0][0]
            db.add_rating(user["id"], movie_id, float(rating))
            description = db.get_movie_description(movie_id)
            message = f"Bewertung gespeichert für {results[0][1]}"

    all_titles = db.get_all_titles()
    return render_template(
        "rate.html",
        user=user,
        all_titles=all_titles,
        message=message,
        description=description,
    )


@app.route("/watchlist")
def watchlist():
    if not require_login():
        return redirect("/login")

    user = session["user"]
    wl = db.get_watchlist(user["id"])
    return render_template("watchlist.html", user=user, watchlist=wl)


@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    if not require_login():
        return redirect("/login")

    message = None

    if request.method == "POST":
        title = request.form["title"]
        genre = request.form["genre"]
        year = request.form["year"]
        description = request.form["description"]

        movie_id = db.add_movie(title, genre, int(year))
        if description:
            db.add_description(movie_id, description)

        message = f"Film hinzugefügt (ID: {movie_id})"

    return render_template("add_movie.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
