import datetime

from flask import request, render_template, url_for
from flask import redirect, session, jsonify

from ToDo import app
from ToDo.Model._m_Home import _m_Home


@app.route("/", methods=["GET"])
def _v_home():
    if request.method == "GET":
        to_return = _m_Home().get_home()
        page_title = f"ToDo: {str(datetime.datetime.now().strftime('%Y-%m-%d'))}"
        return render_template(template_name_or_list="Home.html", to_return=to_return, page_title=page_title)



