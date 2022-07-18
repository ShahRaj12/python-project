from flask import *

from base import app
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.category_vo import CategoryVO


@app.route("/")
def admin_home():
    try:
        return render_template("admin/Home.html")
    except:
        return "Error"
        # return render_template("admin/Home.html")


@app.route("/admin/load_category")
def admin_load_category():
    try:
        print('Load Category')
        return render_template("admin/addCategory.html")
    except:
        return "Error"
        # return render_template("admin/Home.html")


@app.route("/admin/insert_category", methods=["POST"])
def admin_insert_category():
    try:
        category_vo = CategoryVO()
        category_vo.category_name = request.form.get('category_name')
        category_vo.category_description = request.form.get('category_description')
        category_dao = CategoryDAO()
        category_dao.insert_category(category_vo)
        print('Home')
        return redirect(url_for(''))
    except:
        return "Error"
        # return render_template("admin/Home.html")

@app.route("/admin/view_category")
def admin_view_category():
    try:
        category_dao=CategoryDAO()
        category_vo_list=category_dao.view_category()
        print(category_vo_list)
        return render_template("admin/viewCategory.html",category_vo_list=category_vo_list)
    except:
        return "Error"

@app.route("/admin/delete_category")
def admin_delete_category():
    try:
        category_id=request.args.get("uid")
        category_vo = CategoryVO()
        category_dao=CategoryDAO()
        category_vo.category_id =category_id
        print(category_vo.category_id)
        category_dao.delete_category(category_vo)

        return redirect(url_for('admin_view_category'))
    except:
        return "Error"

@app.route("/admin/edit_category")
def admin_edit_category():
    try:
        category_id=request.args.get("eid")
        category_vo = CategoryVO()
        category_dao=CategoryDAO()
        category_vo.category_id =category_id
        print(category_vo.category_id)
        category_vo_list=category_dao.edit_category(category_vo)
        print(category_vo_list)
        return render_template('admin/editCategory.html',category_vo_list=category_vo_list)
    except:
        return "Error"

@app.route("/admin/update_category",methods=['POST'])
def admin_update_category():
    try:
        category_id=request.form.get('catId')
        category_name = request.form.get('cat_name')
        category_description=request.form.get('cat_description')

        category_vo = CategoryVO()
        category_dao=CategoryDAO()

        category_vo.category_id =category_id
        category_vo.category_name = category_name
        category_vo.category_description = category_description

        # print(category_vo.category_id)
        category_dao.update_category(category_vo)


        return redirect(url_for('admin_view_category'))
    except:
        return "Update Error"
