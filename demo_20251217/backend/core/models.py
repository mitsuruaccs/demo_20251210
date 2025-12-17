from django.db import models

# 入庫予定: accs_t_receipt
class AccsTReceipt(models.Model):
    client_cd = models.CharField(max_length=8)
    receipt_plan_date = models.DateField()
    receipt_plan_no = models.CharField(max_length=15)
    receipt_plan_dtl_no = models.CharField(max_length=10)
    receipt_type = models.CharField(max_length=1)
    item_id = models.CharField(max_length=10)
    entry_item_cd = models.CharField(max_length=50)
    receipt_plan_qty = models.DecimalField(max_digits=12, decimal_places=3)
    loc_no = models.CharField(max_length=20)
    stock_ele_value01 = models.CharField(max_length=20)
    stock_ele_value02 = models.CharField(max_length=20)
    stock_ele_value03 = models.CharField(max_length=20)
    stock_ele_value04 = models.CharField(max_length=20)
    stock_ele_value05 = models.CharField(max_length=20)

# 在庫
class Stock(models.Model):
    client_cd = models.CharField(max_length=8)
    receipt_date = models.DateField()
    ident_tag_no = models.CharField(max_length=6)
    receipt_qty = models.DecimalField(max_digits=12, decimal_places=3)
    stock_qty = models.DecimalField(max_digits=12, decimal_places=3)
    alloc_qty = models.DecimalField(max_digits=12, decimal_places=3)
    pick_comp_qty = models.DecimalField(max_digits=12, decimal_places=3)

# 商品
class Item(models.Model):
    client_cd = models.CharField(max_length=8)
    item_id = models.CharField(max_length=10)
    item_cd01 = models.CharField(max_length=50)
    item_cd02 = models.CharField(max_length=50)
    item_cd03 = models.CharField(max_length=50)
    item_cd04 = models.CharField(max_length=50)
    item_cd05 = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)

# 在庫属性設定
class StockElementSetting(models.Model):
    client_cd = models.CharField(max_length=8)
    stock_ele_value01_use = models.CharField(max_length=1)
    stock_ele_value01 = models.CharField(max_length=20)
    stock_ele_value02_use = models.CharField(max_length=1)
    stock_ele_value02 = models.CharField(max_length=20)
    stock_ele_value03_use = models.CharField(max_length=1)
    stock_ele_value03 = models.CharField(max_length=20)
    stock_ele_value04_use = models.CharField(max_length=1)
    stock_ele_value04 = models.CharField(max_length=20)
    stock_ele_value05_use = models.CharField(max_length=1)
    stock_ele_value05 = models.CharField(max_length=20)

# 得意先部課
class Client(models.Model):
    client_cd = models.CharField(max_length=8)
    client_name = models.CharField(max_length=30)

# 汎用区分分類
class GeneralPurposeTypeClass(models.Model):
    gene_prps_type_class = models.CharField(max_length=8)
    gene_prps_type_class_name = models.CharField(max_length=30)

# 汎用区分
class GeneralPurposeType(models.Model):
    gene_prps_type_class = models.CharField(max_length=8)
    gene_prps_type = models.CharField(max_length=8)
    gene_prps_type_class_name = models.CharField(max_length=30)
    value01 = models.CharField(max_length=30)
    value02 = models.CharField(max_length=30)
    value03 = models.CharField(max_length=30)
    value04 = models.CharField(max_length=30)
    value05 = models.CharField(max_length=30)

# 機能パラメータ
class FunctionParameter(models.Model):
    client_cd = models.CharField(max_length=8)
    gene_prps_type_class = models.CharField(max_length=8)
    gene_prps_type = models.CharField(max_length=8)
    value01 = models.CharField(max_length=30)
    value02 = models.CharField(max_length=30)
    value03 = models.CharField(max_length=30)
    value04 = models.CharField(max_length=30)
    value05 = models.CharField(max_length=30)
