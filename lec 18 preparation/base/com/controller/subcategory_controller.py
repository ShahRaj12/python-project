from flask import *

from base import app
from base.com.dao.subcategory_dao import SubCategoryDAO
from base.com.vo.subcategory_vo import SubCategoryVO
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.category_vo import CategoryVO


@app.route("/admin/load_subcategory")
def admin_load_subcategory():
     try:
         category_dao = CategoryDAO()
         category_vo_list = category_dao.view_category()
         print(category_vo_list)

         return render_template('admin/addSubCategory.html',category_vo_list=category_vo_list)
     except:
         return "load error"


@app.route("/admin/insert_subcategory",methods=['POST'])
def admin_insert_subcategory():
    try:
        subcategory_name=request.form.get('subcategory_name')
        subcategory_description=request.form.get('subcategory_description')
        subcategory_category_id=request.form.get('subcategory_category_id')
        print(subcategory_name)
        print(subcategory_description)
        print(subcategory_category_id)
        subcategory_vo=SubCategoryVO()

        subcategory_vo.subcategory_name=subcategory_name
        subcategory_vo.subcategory_description=subcategory_description
        subcategory_vo.subcategory_category_id=subcategory_category_id
        # print()
        subcategory_dao=SubCategoryDAO()
        subcategory_dao.insert_subcategory(subcategory_vo)
        return render_template('admin/Home.html')
    except:
        return "Insert sub Error"
        # return render_template("admin/Home.html")

@app.route("/admin/view_subcategory",)
def admin_view_subcategory():
    try:
        subcategory_dao = SubCategoryDAO()
        subcategory_vo_list = subcategory_dao.view_subcategory()
        print(subcategory_vo_list)
        return render_template("admin/viewSubCategory.html", subcategory_vo_list=subcategory_vo_list)
    except:
        return "Error"

@app.route("/admin/delete_subcategory")
def admin_delete_subcategory():
    try:
        subcategory_id = request.args.get('subid')

        subcategory_vo = SubCategoryVO()
        subcategory_dao = SubCategoryDAO()

        subcategory_vo.subcategory_id = subcategory_id
        print(subcategory_vo.subcategory_id)
        subcategory_dao.delete_subcategory(subcategory_vo)

        return redirect(url_for('admin_view_subcategory'))
    except:
        return "Error"

@app.route("/admin/edit_subcategory")
def admin_edit_subcategory():
    try:
        subcategory_id=request.args.get("eid")

        subcategory_vo = SubCategoryVO()
        subcategory_dao= SubCategoryDAO()

        subcategory_vo.subcategory_id =subcategory_id

        print(subcategory_vo.subcategory_id)
        subcategory_vo_list=subcategory_dao.edit_subcategory(subcategory_vo)

        category_dao=CategoryDAO()
        category_vo_list=category_dao.view_category()

        print(subcategory_vo_list)
        return render_template('admin/editSubCategory.html',subcategory_vo_list=subcategory_vo_list,category_vo_list=category_vo_list)
    except:
        return "Error"

@app.route("/admin/update_subcategory",methods=['POST'])
def admin_update_subcategory():
    try:
        subcategory_id=request.form.get('subcatId')
        subcategory_name = request.form.get('subcat_name')
        subcategory_description=request.form.get('subcat_description')
        subcategory_category_id=request.form.get('categoryId')

        subcategory_vo = SubCategoryVO()
        subcategory_dao=SubCategoryDAO()

        subcategory_vo.subcategory_id =subcategory_id
        subcategory_vo.subcategory_name = subcategory_name
        subcategory_vo.subcategory_description = subcategory_description
        subcategory_vo.subcategory_category_id=subcategory_category_id

        # print(category_vo.category_id)
        subcategory_dao.update_subcategory(subcategory_vo)


        return redirect(url_for('admin_view_subcategory'))
    except:
        return "Update Error"










