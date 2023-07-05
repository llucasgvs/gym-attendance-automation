from pyicloud import PyiCloudService
from datetime import datetime, timedelta
from config import config


# Substitua '<seu_email>' e '<sua_senha>' pelas suas credenciais do iCloud
api = PyiCloudService(config.settings.ICLOUD_EMAIL, config.settings.ICLOUD_PASSWORD)

def marca_dia_pago():
    hoje = datetime.now().date()
    ontem = hoje - timedelta(days=1)  # Modifique se quiser verificar outro dia

    # Obtenha todas as localizações registradas no dia específico
    localizacoes = api.iphone.locations(ontem, hoje)

    # Substitua '<lat_academia>' e '<long_academia>' pelas coordenadas GPS da sua academia
    lat_academia = 123.456789
    long_academia = -12.345678

    tempo_total_academia = timedelta()

    for localizacao in localizacoes:
        latitude = localizacao.get('latitude')
        longitude = localizacao.get('longitude')

        distancia = localizacao.distance_to(lat_academia, long_academia)

        # Se a localização estiver próxima da academia, adicione o tempo gasto nesse dia
        if distancia <= 100:
            tempo_total_academia += localizacao.get('timestampDelta')

    # Verifique se o tempo total na academia é maior que 30 minutos
    if tempo_total_academia >= timedelta(minutes=30):
      print("Dia marcado como pago!")
      # Aqui, você pode adicionar a lógica para marcar o dia como pago

# Chama a função para marcar o dia como pago
#marca_dia_pago()
