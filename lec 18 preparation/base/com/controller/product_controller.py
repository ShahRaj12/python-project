from flask import *

from base import app
from werkzeug.utils import *
from base.com.dao.category_dao import *
from base.com.dao.subcategory_dao import *
from base.com.vo.subcategory_vo import *
from base.com.vo.product_vo import *
from base.com.dao.product_dao import *

PRODUCT_FOLDER='base/static/adminResources/product/'
app.config['PRODUCT_FOLDER']=PRODUCT_FOLDER


@app.route('/admin/load_product')
def admin_load_product():
    try:
        category_dao=CategoryDAO()
        category_vo_list=category_dao.view_category()
        return render_template('admin/addProduct.html',product_vo_list=category_vo_list)

    except:
        print('Product Description')

@app.route('/admin/load_product_subcategory',methods=['GET'])
def admin_load_product_subcategory():
    try:
        category_id=request.args.get('prodcat')
        subcategory_vo=SubCategoryVO()
        subcategory_dao=SubCategoryDAO()

        subcategory_vo.subcategory_category_id=category_id
        subcategory_obj=subcategory_dao.view_category_subcategory(subcategory_vo)

        subcategory_list=[i.as_dict() for i in subcategory_obj]
        # print('subcategory List:',subcategory_list)

        return jsonify(subcategory_list)

    except:
        print('Product Subcategory Exception')

@app.route('/admin/insert_product',methods=['POST'])
def admin_insert_product():
    try:
        product_category_id=request.form.get('productCategory')
        product_subcategory_id=request.form.get('productSubcategory')
        product_name=request.form.get('productName')
        product_description = request.form.get('productDescription')
        product_price = request.form.get('productPrice')
        product_quantity = request.form.get('productQuantity')
        product_image = request.files.get('productImage')

        product_imagename = secure_filename(product_image.filename)
        product_imagepath = os.path.join(app.config['PRODUCT_FOLDER'])
        product_image.save(os.path.join(product_imagepath,product_imagename))

        product_vo=ProductVO()
        product_dao=ProductDAO()

        product_vo.product_name=product_name
        product_vo.product_description=product_description
        product_vo.product_price=product_price
        product_vo.product_quantity=product_quantity
        product_vo.product_imagename=product_imagename
        product_vo.product_imagepath=product_imagepath.replace("base","..")

        product_vo.product_category_id=product_category_id
        product_vo.product_subcategory_id=product_subcategory_id

        product_dao.insert_product(product_vo)

        return render_template('admin/Home.html')

    except Exception as e:
        return e

@app.route('/admin/view_product')
def admin_view_product():
    try:
        product_dao = ProductDAO()
        product_list = product_dao.view_product()
        return render_template("admin/viewProduct.html",product_list=product_list)
    except Exception as e:
        return e

@app.route('/admin/delete_product')
def admin_delete_product():
    try:
        product_id = request.args.get('pid')
        product_path=request.args.get('path').replace("..","base")
        product_vo = ProductVO()
        product_dao = ProductDAO()

        product_vo.product_id = product_id
        print(product_vo.product_id)
        product_dao.delete_product(product_vo)
        os.remove(product_path)

        return redirect(url_for('admin_view_product'))

    except Exception as e:
        return e



















