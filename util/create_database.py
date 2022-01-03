from datetime import date
from sqlalchemy import func
from models.database import create_db, Session
from models.group import Group
from models.product import Product    # Закомент.для отладки
from util.parser import data          # Закомент.для отладки

# Раскомент.для отладки
#data = [{'product_name': ' Lezard Mira Белый-Белый Розетка с заземляющими контактами керамика скрытая установка (859658) 701-0202-122 ', 'price': 178.2, 'amount': 890, 'group_name': 'Установка, Выключатели, Розетки и аксессуары'}, {'product_name': ' Greenel Коробка установочная 3-местная 212х70х45мм. д/скрыт. монтажа в кирпичных стенах (с саморезами) (45шт) GE40009 ', 'price': 52.1, 'amount': 0, 'group_name': 'Установка, Выключатели, Розетки и аксессуары'}, {'product_name': ' TDM Подрозетник в бетон 65х65 с ушами SQ1402-1018 ', 'price': 16.7, 'amount': 0, 'group_name': 'Установка, Выключатели, Розетки и аксессуары'}, {'product_name': ' Коробка распаячная КМР-030-014 с крышкой (100х100х50), 8 мембр. вводов чёрная IP54 EKF ', 'price': 80.8, 'amount': 0, 'group_name': 'Установка, Выключатели, Розетки и аксессуары'}, {'product_name': ' Коробка накладного монтажа ABB Variant+ IP20 для механизмов 45х45 с четырьмя вводами серый ', 'price': 777.1, 'amount': 0, 'group_name': 'Установка, Выключатели, Розетки и аксессуары'}, {'product_name': ' TDM Коробка установочная D73х73 мм углубл. саморезы металлические лапки скрытая установка IP20 SQ1403-0010 ', 'price': 34.9, 'amount': 0, 'group_name': 'Установка, Выключатели, Розетки и аксессуары'}, {'product_name': ' TDM Черный Коробка распаячная фарфоровая D7,8х4,5см ', 'price': 643.6, 'amount': 0, 'group_name': 'Установка, Выключатели, Розетки и аксессуары'}, {'product_name': ' Коробка клеммная Schneider Electric Рондо KLK-5S (КлК-5С) IP44 с монтажной пластиной, кр.л. (5х6,0 мм2, 380В, 40А) KLK-5S ', 'price': 298.8, 'amount': 448, 'group_name': 'Установка, Выключатели, Розетки и аксессуары'}, {'product_name': ' Эл. Быт. изделия Коробка монтажная г/к армлен Минск К-205 (г/к) 76x40мм 192039 ', 'price': 24.5, 'amount': 0, 'group_name': 'Установка, Выключатели, Розетки и аксессуары'}]


def create_database(load_data: bool = True):
    create_db()
    if load_data:
        _load_data(Session())


def _load_data(session: Session):
    global group_id
    print('Спарсенные с сайта данные загружаются в базу данных...')

    for item in data:

        group_if = session.query(Group).filter_by(group_name=item['group_name']).first()

        if not group_if:
            group = Group(group_name=item['group_name'])
            session.add(group)
            session.commit()

        products = session.query(Product).filter_by(product_name=item['product_name']).first()
        if not products:
            group_id = (session.query(Group).filter_by(group_name=item['group_name']).first()).id
            product = Product(product_name=item['product_name'], price=item['price'], amount=item['amount'],
                              group=group_id)
            session.add(product)
            session.commit()

        product_date_max = session.query(func.max(Product.created)).first()[0]
        last_date = str(product_date_max.strftime("%Y-%m-%d"))
        current_date = str(date.today())

        if not (last_date == current_date):

            product = Product(product_name=item['product_name'], price=item['price'], amount=item['amount'],
                              group=group_id)
            session.add(product)

    session.commit()
    session.close()


