import datetime, os

from flask import request, render_template, url_for
from flask import redirect, session, jsonify, send_from_directory

from ToDo import app, auth
from ToDo.Model._m_Home import _m_Home


@app.route("/", methods=["GET"])
@auth.login_required
def _v_home():
    if request.method == "GET":
        username = request.authorization["username"]
        to_return = _m_Home().get_home()
        page_title = f"ToDo_: {str(datetime.datetime.now().strftime('%Y-%m-%d'))}"
        return render_template(template_name_or_list="Home.html", to_return=to_return, page_title=page_title, username=username)


# Favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico', mimetype='image/x-icon')


# Robots.txt
@app.route('/robots.txt')
def robotstxt():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'robots.txt', mimetype='application/txt')