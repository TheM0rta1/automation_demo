from page.base_page import BasePage
from utils.parseConFile import ParseConFile
from utils.keyboard import KeyBoard


class BrandPage(BasePage):
    do_conf = ParseConFile()
    keyboard = KeyBoard()
    goods_system = do_conf.get_config_data("HomePageElements", "goods_system")
    brand_manage = do_conf.get_config_data("HomePageElements", "brand_manage")
    # 品牌管理页面
    search_box = do_conf.get_config_data("BrandManagePageElements", "search_box")
    search_btn = do_conf.get_config_data("BrandManagePageElements", "search_btn")
    add_btn = do_conf.get_config_data("BrandManagePageElements", "add_btn")
    batch_delete_btn = do_conf.get_config_data("BrandManagePageElements", "batch_delete_btn")
    # 品牌列表
    table_brand_name = do_conf.get_config_data("BrandManagePageElements", "brand_name")
    table_introduction = do_conf.get_config_data("BrandManagePageElements", "introduction")
    table_show_status = do_conf.get_config_data("BrandManagePageElements", "show_status")
    relate_category = do_conf.get_config_data("BrandManagePageElements", "relate_category")
    modify_brand = do_conf.get_config_data("BrandManagePageElements", "modify_brand")

    delete_brand = do_conf.get_config_data("BrandManagePageElements", "delete_brand")
    confirm_delete_brand = do_conf.get_config_data("BrandManagePageElements", "confirm_delete_btn")
    # 新增品牌页面
    brand_name = do_conf.get_config_data("AddNewBrandElements", "brand_name")
    brand_logo_update_btn = do_conf.get_config_data("AddNewBrandElements", "brand_logo_update_btn")
    introduction = do_conf.get_config_data("AddNewBrandElements", "introduction")
    show_status = do_conf.get_config_data("AddNewBrandElements", "show_status")
    search_initial = do_conf.get_config_data("AddNewBrandElements", "search_initial")
    sort = do_conf.get_config_data("AddNewBrandElements", "sort")
    cancel_btn = do_conf.get_config_data("AddNewBrandElements", "cancel_btn")
    confirm_btn = do_conf.get_config_data("AddNewBrandElements", "confirm_btn")
    logo_upload_success = do_conf.get_config_data("AddNewBrandElements", "logo_upload_success")
    success_alert = do_conf.get_config_data("AddNewBrandElements", "success_alert")
    common_none = do_conf.get_config_data("AddNewBrandElements", "common_none")

    # 关联分类页面
    add_relation_btn = do_conf.get_config_data("RelateCategoryElements", "add_relation_btn")
    relation_cancel_btn = do_conf.get_config_data("RelateCategoryElements", "cancel_btn")
    relation_confirm_btn = do_conf.get_config_data("RelateCategoryElements", "confirm_btn")
    input_category_box = do_conf.get_config_data("RelateCategoryElements", "input_category_box")
    category_in_list = do_conf.get_config_data("RelateCategoryElements", "category_in_list")
    new_relation_cancel_btn = do_conf.get_config_data("RelateCategoryElements", "new_cancel_btn")
    new_relation_confirm_btn = do_conf.get_config_data("RelateCategoryElements", "new_confirm_btn")
    add_relation_success_msg = do_conf.get_config_data("RelateCategoryElements", "add_relation_success_msg")

    def add_new_brand(self, brand_name, file_path, file_name, introduction, show_status, search_initial, sort):
        self.locate_to_brand_page()
        self.open_add_brand_page()
        self.input_brand_name(brand_name)
        self.upload_brand_logo(file_path, file_name)
        self.check_logo_update_success()
        self.input_introduction(introduction)
        self.change_show_status(show_status)
        self.input_search_initial(search_initial)
        self.input_sort(sort)
        self.confirm_add_new_brand()

    def add_brand_attr_none(self, brand_name, introduction, show_status, search_initial, sort):
        self.locate_to_brand_page()
        self.open_add_brand_page()
        self.input_brand_name(brand_name)
        self.input_introduction(introduction)
        self.change_show_status(show_status)
        self.input_search_initial(search_initial)
        self.input_sort(sort)
        self.confirm_add_new_brand()

    def add_new_category_relation(self, brand_name, category):
        self.locate_to_brand_page()
        brand_index = self.locate_spec_brand(brand_name)
        self.click_relate_category(brand_index)
        self.open_add_relation_page()
        self.input_category(category)
        self.choose_category()
        self.confirm_choose_category()

    def locate_to_brand_page(self):
        """打开品牌管理页面"""
        self.wait_element_to_be_located(*BrandPage.goods_system, model="商品系统")
        self.click(*BrandPage.goods_system, model="商品系统")
        self.wait_element_to_be_located(*BrandPage.brand_manage, model="品牌管理")
        return self.click(*BrandPage.brand_manage, model="品牌管理")

    def locate_spec_brand(self, brand_name):
        """定位品牌列表中特定的品牌"""
        table_brand_names = self.get_elements_text(*BrandPage.table_brand_name, model="品牌列表所有品牌的名字")
        for table_brand_name in table_brand_names:
            if table_brand_name == brand_name:
                brand_index = table_brand_names.index(table_brand_name)
        return brand_index

    def open_add_brand_page(self):
        """打开新建品牌页面"""
        self.wait_element_to_be_located(*BrandPage.add_btn, model="新增品牌按钮")
        return self.click(*BrandPage.add_btn, model="新增品牌按钮")

    def click_modify_brand(self):
        """点击品牌的修改按钮"""
        modify_brand_btn = self.find_element_by_index(*BrandPage.modify_brand, model="修改品牌按钮")
        return modify_brand_btn.click()

    def click_delete_brand(self):
        """点击品牌的删除按钮"""
        delete_brand_btn = self.find_element_by_index(*BrandPage.delete_brand, model="删除品牌按钮")
        return delete_brand_btn.click()

    def confirm_delete_brand(self):
        """确定删除品牌"""
        self.wait_element_to_be_located(*BrandPage.confirm_delete_brand, model="删除品牌的确定按钮")
        return self.click(*BrandPage.confirm_delete_brand, model="删除品牌的确定按钮")

    # 品牌管理界面操作
    def input_brand_name(self, brand_name):
        """输入品牌名字"""
        self.wait_element_to_be_located(*BrandPage.brand_name, model="品牌名输入框")
        return self.send_keys(*BrandPage.brand_name, brand_name, model="品牌名输入框")

    def upload_brand_logo(self, file_path, file_name):
        """上传品牌logo"""
        self.wait_element_to_be_located(*BrandPage.brand_logo_update_btn, model="品牌logo上传按钮")
        self.click(*BrandPage.brand_logo_update_btn, model="品牌logo上传按钮")
        return self.upload_file(file_path, file_name)

    def input_introduction(self, introduction):
        """输入品牌介绍"""
        self.wait_element_to_be_located(*BrandPage.introduction, model="品牌介绍输入框")
        return self.send_keys(*BrandPage.introduction, introduction, model="品牌介绍输入框")

    def change_show_status(self, show_status):
        """修改显示状态"""
        self.wait_element_to_be_located(*BrandPage.show_status, model="显示状态按钮")
        is_checked = self.get_element_text(*BrandPage.show_status, 'aria-checked', model="显示状态")
        if (is_checked is True and show_status == 0) or (is_checked is False and show_status == 1):
            return self.click(*BrandPage.show_status, model="显示状态按钮")

    def input_search_initial(self, search_initial):
        """输入检索首字母"""
        self.wait_element_to_be_located(*BrandPage.search_initial, model="检索首字母输入框")
        return self.send_keys(*BrandPage.search_initial, search_initial, model="检索首字母输入框")

    def input_sort(self, sort):
        """输入排序"""
        self.wait_element_to_be_located(*BrandPage.sort, model="排序输入框")
        return self.send_keys(*BrandPage.sort, sort, model="排序输入框")

    def confirm_add_new_brand(self):
        """确定添加品牌"""
        self.wait_element_to_be_located(*BrandPage.confirm_btn, model="确定按钮")
        return self.click(*BrandPage.confirm_btn, model="确定按钮")

    def cancel_add_new_brand(self):
        """取消添加品牌"""
        self.wait_element_to_be_located(*BrandPage.cancel_btn, model="取消按钮")
        return self.click(*BrandPage.cancel_btn, model="取消按钮")

    def check_logo_update_success(self):
        """获取logo上传成功提示信息"""
        self.logger.info("===获取logo上传成功提示信息===")
        return self.is_element_exist(*BrandPage.logo_upload_success, model="logo上传成功提示")

    def get_success_msg(self):
        """获取操作成功提示信息"""
        self.logger.info("===获取操作成功提示信息===")
        return self.get_element_text(*BrandPage.success_alert, model="操作成功提示")

    def get_common_none(self):
        """品牌名/logo/介绍/检索首字母/排序为空提示信息"""
        self.logger.info("===获取品牌名/logo/介绍/检索首字母/排序为空提示信息===")
        return self.get_elements_text(*BrandPage.common_none, model='品牌名/logo/介绍/检索首字母/排序为空提示信息')

    #   关联分类页面
    def click_relate_category(self, brand_index):
        """点击关联分类按钮"""
        relate_category = self.find_element_by_index(*BrandPage.relate_category, brand_index, model="关联分类按钮")
        return relate_category.click()

    def open_add_relation_page(self):
        """打开关联分类的新增关联页面"""
        self.wait_element_to_be_located(*BrandPage.add_relation_btn, model="新增关联按钮")
        return self.click(*BrandPage.add_relation_btn, model="新增关联按钮")

    def input_category(self, category):
        """输入分类"""
        self.wait_element_to_be_located(*BrandPage.input_category_box, model="新增关联搜索框")
        input_category = self.find_element(*BrandPage.input_category_box, model="新增关联搜索框")
        self.driver.execute_script("arguments[0].click()", input_category)
        return self.send_keys(*BrandPage.input_category_box, category, model="新增关联搜索框")

    def choose_category(self):
        """从下拉列表中选择一个分类"""
        self.wait_element_to_be_located(*BrandPage.category_in_list, model="新增关联中的分类列表")
        return self.click(*BrandPage.category_in_list, model="新增关联中的分类列表")

    def confirm_choose_category(self):
        """点击新增关联中的确定按钮"""
        self.wait_element_to_be_located(*BrandPage.new_relation_confirm_btn, model="新增关联中的确定按钮")
        return self.click(*BrandPage.new_relation_confirm_btn, model="新增关联中的确定按钮")

    def get_relation_success_msg(self):
        """通过关联分类页面的列表判断关联成功"""
        self.wait_element_to_be_located(*BrandPage.add_relation_success_msg, model="关联分类列表的数据")
        return self.get_element_text(*BrandPage.add_relation_success_msg, model="关联分类列表的数据")

    def confirm_relate_category(self):
        """点击关联分类的确定按钮"""
        self.wait_element_to_be_located(*BrandPage.relation_confirm_btn, model="关联分类的确定按钮")
        return self.click(*BrandPage.relation_confirm_btn, model="关联分类的确定按钮")
