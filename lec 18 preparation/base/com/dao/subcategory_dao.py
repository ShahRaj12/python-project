from base import db
from base.com.vo.subcategory_vo import SubCategoryVO
from base.com.vo.category_vo import CategoryVO

class SubCategoryDAO:
    def insert_subcategory(self, subcategory_vo):
        db.session.add(subcategory_vo)
        db.session.commit()

    def view_subcategory(self):
        subcategory_list=db.session.query(SubCategoryVO,CategoryVO).\
            join(CategoryVO,SubCategoryVO.subcategory_category_id==CategoryVO.category_id).all()
        return subcategory_list

    def delete_subcategory(self, subcategory_vo):
        subcategory_vo_list = SubCategoryVO.query.get(subcategory_vo.subcategory_id)
        db.session.delete(subcategory_vo_list)
        db.session.commit()

    def edit_subcategory(self, subcategory_vo):
        sub_category_list=db.session.query(CategoryVO,SubCategoryVO).\
            join(SubCategoryVO,SubCategoryVO.subcategory_category_id==CategoryVO.category_id).\
            filter_by(subcategory_id=subcategory_vo.subcategory_id).all()
        return sub_category_list


    def update_subcategory(self, subcategory_vo):
        db.session.merge(subcategory_vo)
        db.session.commit()

    def view_category_subcategory(self,subcategory_vo):
        subcategory_list=SubCategoryVO.query.filter_by(
            subcategory_category_id=subcategory_vo.subcategory_category_id).all()
        return subcategory_list
