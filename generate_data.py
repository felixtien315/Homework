from django.conf import settings
import os
import django
from decimal import Decimal
from datetime import date

# 設置 Django 環境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nightmarket_project.settings')
django.setup()

from nightmarket.models import NightMarket, Vendor, Food

def generate_training_data():
    # 清空現有資料（可選）
    Food.objects.all().delete()
    Vendor.objects.all().delete()
    NightMarket.objects.all().delete()

    # 創建夜市
    night_markets = [
        NightMarket(name="士林夜市", city="台北市", address="台北市士林區文林路", opening_hours="每週二至週日 16:00-01:00", is_active=True),
        NightMarket(name="饒河夜市", city="台北市", address="台北市松山區饒河街", opening_hours="每週一至週日 17:00-23:00", is_active=True),
        NightMarket(name="逢甲夜市", city="台中市", address="台中市西屯區文華路", opening_hours="每週一至週日 16:00-02:00", is_active=True),
        NightMarket(name="花園夜市", city="台南市", address="台南市北區海安路三段", opening_hours="每週四、六、日 17:00-23:00", is_active=True),
    ]
    NightMarket.objects.bulk_create(night_markets)

    # 獲取夜市物件
    shilin = NightMarket.objects.get(name="士林夜市")
    raohe = NightMarket.objects.get(name="饒河夜市")
    fengjia = NightMarket.objects.get(name="逢甲夜市")
    huayuan = NightMarket.objects.get(name="花園夜市")

    # 創建攤販
    vendors = [
        Vendor(name="豪大大雞排", night_market=shilin, owner_name="王小明", contact_phone="0912345678", established_date=date(2010, 5, 1)),
        Vendor(name="阿宗麵線", night_market=shilin, owner_name="陳美玲", contact_phone="0923456789", established_date=date(2008, 3, 15)),
        Vendor(name="士林臭豆腐", night_market=shilin, owner_name="林志偉", contact_phone="0934567890", established_date=date(2015, 7, 20)),
        Vendor(name="珍奶小攤", night_market=shilin, owner_name="張雅婷", contact_phone="0945678901", established_date=date(2019, 1, 10)),
        Vendor(name="胡椒餅老店", night_market=raohe, owner_name="李建國", contact_phone="0956789012", established_date=date(2005, 11, 5)),
        Vendor(name="蚵仔煎達人", night_market=raohe, owner_name="黃麗華", contact_phone="0967890123", established_date=date(2012, 4, 25)),
        Vendor(name="饒河烤魷魚", night_market=raohe, owner_name="吳俊傑", contact_phone="0978901234", established_date=date(2017, 9, 30)),
        Vendor(name="水果冰店", night_market=raohe, owner_name="蔡宜靜", contact_phone="0989012345", established_date=date(2020, 6, 15)),
        Vendor(name="逢甲雞爪凍", night_market=fengjia, owner_name="劉家豪", contact_phone="0990123456", established_date=date(2014, 2, 18)),
        Vendor(name="大腸包小腸", night_market=fengjia, owner_name="許志宏", contact_phone="0901234567", established_date=date(2011, 8, 12)),
        Vendor(name="逢甲滷味", night_market=fengjia, owner_name="鄭怡君", contact_phone="0912345670", established_date=date(2016, 12, 1)),
        Vendor(name="奶茶工坊", night_market=fengjia, owner_name="林佩珊", contact_phone="0923456781", established_date=date(2018, 5, 5)),
        Vendor(name="花園鹹酥雞", night_market=huayuan, owner_name="陳冠宇", contact_phone="0934567892", established_date=date(2013, 10, 10)),
        Vendor(name="台南虱目魚湯", night_market=huayuan, owner_name="吳曉雯", contact_phone="0945678903", established_date=date(2009, 7, 15)),
    ]
    Vendor.objects.bulk_create(vendors)

    # 創建美食
    foods = [
        Food(name="香酥雞排", vendor=Vendor.objects.get(name="豪大大雞排"), price=Decimal("70.00"), category="小吃", is_available=True),
        Food(name="麻辣雞排", vendor=Vendor.objects.get(name="豪大大雞排"), price=Decimal("75.00"), category="小吃", is_available=True),
        Food(name="西多士", vendor=Vendor.objects.get(name="豪大大雞排"), price=Decimal("50.00"), category="小吃", is_available=True),
        Food(name="麵線糊", vendor=Vendor.objects.get(name="阿宗麵線"), price=Decimal("55.00"), category="小吃", is_available=True),
        Food(name="大腸麵線", vendor=Vendor.objects.get(name="阿宗麵線"), price=Decimal("60.00"), category="小吃", is_available=True),
        Food(name="炸臭豆腐", vendor=Vendor.objects.get(name="士林臭豆腐"), price=Decimal("50.00"), category="小吃", is_available=True),
        Food(name="脆皮臭豆腐", vendor=Vendor.objects.get(name="士林臭豆腐"), price=Decimal("60.00"), category="小吃", is_available=True),
        Food(name="珍珠奶茶", vendor=Vendor.objects.get(name="珍奶小攤"), price=Decimal("50.00"), category="飲料", is_available=True),
        Food(name="冬瓜茶", vendor=Vendor.objects.get(name="珍奶小攤"), price=Decimal("40.00"), category="飲料", is_available=True),
        Food(name="胡椒餅", vendor=Vendor.objects.get(name="胡椒餅老店"), price=Decimal("55.00"), category="小吃", is_available=True),
        Food(name="蚵仔煎", vendor=Vendor.objects.get(name="蚵仔煎達人"), price=Decimal("70.00"), category="小吃", is_available=True),
        Food(name="海鮮煎", vendor=Vendor.objects.get(name="蚵仔煎達人"), price=Decimal("80.00"), category="小吃", is_available=True),
        Food(name="碳烤魷魚", vendor=Vendor.objects.get(name="饒河烤魷魚"), price=Decimal("100.00"), category="燒烤", is_available=True),
        Food(name="芒果冰", vendor=Vendor.objects.get(name="水果冰店"), price=Decimal("80.00"), category="甜點", is_available=True),
        Food(name="草莓冰", vendor=Vendor.objects.get(name="水果冰店"), price=Decimal("85.00"), category="甜點", is_available=True),
        Food(name="雞爪凍", vendor=Vendor.objects.get(name="逢甲雞爪凍"), price=Decimal("45.00"), category="小吃", is_available=True),
        Food(name="大腸包小腸", vendor=Vendor.objects.get(name="大腸包小腸"), price=Decimal("60.00"), category="小吃", is_available=True),
        Food(name="麻辣滷味", vendor=Vendor.objects.get(name="逢甲滷味"), price=Decimal("50.00"), category="小吃", is_available=True),
        Food(name="奶茶", vendor=Vendor.objects.get(name="奶茶工坊"), price=Decimal("45.00"), category="飲料", is_available=True),
        Food(name="鹹酥雞", vendor=Vendor.objects.get(name="花園鹹酥雞"), price=Decimal("65.00"), category="小吃", is_available=True),
    ]
    Food.objects.bulk_create(foods)

    print("成功生成 20 筆訓練資料！")
    print(f"夜市數量：{NightMarket.objects.count()}")
    print(f"攤販數量：{Vendor.objects.count()}")
    print(f"美食數量：{Food.objects.count()}")

if __name__ == "__main__":
    generate_training_data()
