from base.com.vo.product_vo import *

class ProductDAO:
    def insert_product(self, product_vo):
        db.session.add(product_vo)
        db.session.commit()

    def view_product(self):
        product_vo_list=db.session.query(ProductVO,CategoryVO,SubCategoryVO).\
        join(SubCategoryVO,ProductVO.product_subcategory_id==SubCategoryVO.subcategory_id).\
        join(CategoryVO,ProductVO.product_category_id==CategoryVO.category_id).all()

        return product_vo_list

    def delete_product(self, product_vo):
        product_vo_list = ProductVO.query.get(product_vo.product_id)
        db.session.delete(product_vo_list)
        db.session.commit()

