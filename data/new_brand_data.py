import os
from selenium.webdriver import Keys
from config.conf import ROOT_DIR


class NewBrandData(object):
    """添加品牌测试数据"""

    add_new_brand_data = [
        {
            "case": "成功添加新的品牌信息",
            "brand_name": "TestBrand",
            "file_path": os.path.join(ROOT_DIR, 'data\\pics'),
            "file_name": "test_brand.png",
            "introduction": "Test for brand",
            "show_status": "1",
            "search_initial": "T",
            "sort": "0",
            "expected": "操作成功"
        }
    ]

    # 添加新品牌失败场景
    add_brand_attr_none_data = [
        {
            "case": "品牌名/logo/介绍/检索首字母/排序为空",
            "brand_name": "",
            "introduction": "",
            "show_status": "1",
            "search_initial": "",
            "sort": Keys.BACK_SPACE,
            "expected": ["品牌名不能为空", "品牌logo地址不能为空", "介绍不能为空", "首字母必须填写", "排序字段必须填写"]
        }
    ]

    add_new_category_relation_data = [
        {
            "case": "新增分类关联",
            "brand_name": "TestBrand",
            "category": "手机",
            "expected": "手机"
        }
    ]


if __name__ == '__main__':
    pass


