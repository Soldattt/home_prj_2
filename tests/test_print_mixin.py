from src.products import Product
from src.lawngrass import LawnGrass
from src.smartphone import Smartphone

def test_print(capsys):
    Product(name="Lenovo Legion 5", description="Ryzen 7, Черный цвет, 1 Tb", price=140000.0, quantity=5)
    mes = capsys.readouterr()
    assert mes.out.strip() == 'Product, Lenovo Legion 5, Ryzen 7, Черный цвет, 1 Tb, 140000.0, 5'

    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 1, 95.5, "S23 Ultra", 256, "Серый"
    )
    mes = capsys.readouterr()
    assert mes.out.strip() == ('Smartphone, Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, '
 '180000.0, 1')


    LawnGrass(
        name="Трава_2",
        description="для курения",
        price=15000.0,
        quantity=5,
        country="Афганистан",
        germination_period="3 дня",
        color="Зеленая",
    )
    mes = capsys.readouterr()
    assert mes.out.strip() == 'LawnGrass, Трава_2, для курения, 15000.0, 5'