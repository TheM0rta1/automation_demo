import time

import allure
import pytest
from data.new_brand_data import NewBrandData


@allure.feature("新增品牌功能")
@allure.description("新增品牌界面功能测试")
class TestNewBrand(object):
    new_brand_data = NewBrandData

    @pytest.mark.BrandManage
    @allure.story('关联分类测试')
    @allure.title('关联分类成功场景')
    @pytest.mark.parametrize('data', new_brand_data.add_new_category_relation_data)
    def test_add_new_brand(self, login, data):
        brand_page = login[1]
        brand_page.add_new_category_relation(data["brand_name"], data["category"])
        actual = brand_page.get_relation_success_msg()
        assert actual == data["expected"]
        brand_page.confirm_relate_category()

    # @pytest.mark.AddNewBrand
    # @allure.story('添加新品牌成功测试')
    # @allure.title('添加新品牌成功场景')
    # @pytest.mark.parametrize('data', new_brand_data.add_new_brand_data)
    # def test_add_new_brand(self, login, data):
    #     brand_page = login[1]
    #     brand_page.add_new_brand(data["brand_name"], data["file_path"], data["file_name"], data["introduction"],
    #                              data["show_status"], data["search_initial"], data["sort"])
    #     actual = brand_page.get_success_msg()
    #     assert actual == data["expected"]
    #
    # @pytest.mark.AddNewBrand
    # @allure.story('添加失败测试')
    # @allure.title('添加新品牌失败场景: 品牌名/logo/介绍/检索首字母/排序为空')
    # @pytest.mark.parametrize('data', new_brand_data.add_brand_attr_none_data)
    # def test_brand_attr_none(self, login, data):
    #     time.sleep(2)
    #     brand_page = login[1]
    #     brand_page.add_brand_attr_none(data["brand_name"], data["introduction"], data["show_status"],
    #                                    data["search_initial"], data["sort"])
    #     actual = brand_page.get_common_none()
    #     assert actual == data["expected"]
