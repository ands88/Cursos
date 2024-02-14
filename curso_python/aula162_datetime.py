# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
from pytz import timezone

""" 
data_str = '2024-02-14 13:30:58'
data_frmt = '%Y-%m-%d %H:%M:%S'

#data = datetime(2024, 2, 14, 13, 25, timezone('Asia/Tokyo'))
data = datetime.strptime(data_str, data_frmt) """

data = datetime.now(timezone('Asia/Tokyo'))

print(data.timestamp()) # isso está salvo na base de dados - unix timestamp
print(datetime.fromtimestamp(1707929051))
print (data)

