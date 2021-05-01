from flask import Blueprint, request, jsonify
from db import do_sql_cmd

ajax_bp = Blueprint("ajax_bp", __name__)


@ajax_bp.route("/api/v1.0/courses/", methods=["GET"])
def ret_courses():
    data = do_sql_cmd("select * from courses")
    return jsonify({"status": "ok", "data": data})


@ajax_bp.route("/api/v1.0/courses/", methods=["POST"])
def new_course():
    req = request.get_json()
    data = do_sql_cmd(
        f"insert into courses (name,dbegin,dend,cntlections) values ('{req['name']}', '{req['dbegin']}', '{req['dend']}',{req['cntlections']})"
    )
    return jsonify({"status": "ok", "data": data})


@ajax_bp.route("/api/v1.0/courses/<int:id>", methods=["GET"])
def ret_course(id):
    data = do_sql_cmd(f"select * from courses where id={id}")
    return jsonify({"status": "ok", "data": data})


@ajax_bp.route("/api/v1.0/courses/<int:id>", methods=["DELETE"])
def del_course(id):
    data = do_sql_cmd(f"delete from courses where id={id}")
    return jsonify({"status": "ok", "data": data})


@ajax_bp.route("/api/v1.0/courses/<id>", methods=["PUT"])
def upd_course(id):
    req = request.get_json()
    data = do_sql_cmd(
        f"update courses set name='{req['name']}', dbegin='{req['dbegin']}', dend='{req['dend']}',cntlections={req['cntlections']} where id={id}"
    )
    return jsonify({"status": "ok", "data": data})


@ajax_bp.route("/api/v1.0/courses/q", methods=["GET"])
def search_course():
    req = request.get_json()
    data = do_sql_cmd(
        f"select * from courses where name like '%{req['q']}%' or dbegin like '%{req['q']}%'"
    )
    return jsonify({"status": "ok", "data": data})
