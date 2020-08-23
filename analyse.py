# %%
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix

#%%
df = pd.read_pickle('./comm_real_estate_100-100_sqm.pkl')

# %%
df.info()
# %%
df.describe()
# %%
df.head()
df.columns

#%%
# Plot overviewing histograms:
%matplotlib inline
df.hist(bins=20, figsize=(20,15))
plt.show()

# %%
%matplotlib inline
df['Средняя цена за м2, ₽'].hist(bins=40)

# %%
%matplotlib inline
df['Высота потолков'].hist(bins=40)

#%%
# Filter prices that have only a single value, not a range:
price = [np.mean(i) for i in df['Цена, ₽/мес.']]
df.insert(41, 'Цена средняя, ₽/мес.', price, True)

# Plot a histogram for this data:
n, bins, patches = plt.hist(price, 50, density=False, facecolor='g', alpha=0.75)
plt.xlabel('Цена, ₽/мес.')
plt.xlim(0, 2_500_000)
plt.grid(True)
plt.show()

#%%
din_stavki = df['Динамика ставки за год жилая, %']
n, bins, patches = plt.hist(din_stavki, 60, density=False, facecolor='navy', alpha=0.75)
plt.xlabel('Динамика ставки за год жилая, %')
plt.xlim(-5, 20)
plt.grid(True)
plt.show()

# %%
# Корреляция цены с другими численными признаками:
corr_matrix = df.corr()
corr_matrix['Цена средняя, ₽/мес.'].sort_values(ascending=False)

#%%
%matplotlib inline
attributes = [
# 'Аварийный',
#  'Адрес',
#  'Арендные каникулы',
#  'Витринные окна',
#  'Вход',
#  'Высота потолков',
 'Год постройки',
#  'Девелопер',
#  'Динамика ставки за год жилая, %',
#  'Динамика цены за м2 за год жилая, %',
#  'Категория здания',
 'Количество квартир',
#  'Количество мест',
#  'Количество мокрых точек',
#  'Комиссия от клиента, %',
#  'Коммунальные платежи',
#  'Масштаб торгового комплекса',
#  'Материал пола',
#  'Материалы стен',
#  'Минимальный срок аренды, мес',
 'Мощность, кВт',
#  'Налог',
#  'Размер НДС',
#  'Номер налоговой',
#  'Обеспечительный платеж, ₽',
 'Общая площадь, м2',
#  'Описание',
#  'Парковка',
 'Площадь участка, га',
 'Количество подъездов',
#  'Предоплата, мес.',
#  'Состояние',
 'Средняя цена за м2, ₽',
#  'Срок аренды',
 'Ставка ₽ за м²/год',
#  'Статус участка',
#  'Стоимость',
#  'Тип аренды',
#  'Тип здания',
#  'Управляющая компания',
#  'Цена, ₽/мес.',
#  'Эксплуатационные расходы',
#  'Этажность',
#  'Юридический адрес',
 'Цена средняя, ₽/мес.']

scatter_matrix(df[attributes], figsize=(20, 20), alpha=0.3, marker='o', grid=True)
plt.show()
# %%
