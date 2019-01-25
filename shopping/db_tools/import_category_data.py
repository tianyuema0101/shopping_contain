__author__ = 'mty'

import os
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping.settings')

import django
django.setup()

from goods.models import GoodsCategory
from db_tools.data.category_data import row_data

for lev1_cat in row_data:
    lev1_sintance = GoodsCategory()
    lev1_sintance.code = lev1_cat["code"]
    lev1_sintance.name = lev1_cat["name"]
    lev1_sintance.category_type = 1
    lev1_sintance.save()

    for lev2_cat in lev1_cat["sub_categorys"]:
        lev2_sintance = GoodsCategory()
        lev2_sintance.code = lev2_cat["code"]
        lev2_sintance.name = lev2_cat["name"]
        lev2_sintance.category_type = 2
        lev2_sintance.parent_category = lev1_sintance
        lev2_sintance.save()

        for lev3_cat in lev2_cat["sub_categorys"]:
            lev3_sintance = GoodsCategory()
            lev3_sintance.code = lev3_cat["code"]
            lev3_sintance.name = lev3_cat["name"]
            lev3_sintance.category_type = 3
            lev3_sintance.parent_category = lev2_sintance
            lev3_sintance.save()
