import requests
from jsonschema import validate, ValidationError

from elitedata.models import StationCommodity, Commodity, Station, System

class Ingester:
    schemaV1Url = 'http://schemas.elite-markets.net/eddn/commodity/1'
    schemaV2Url = 'http://schemas.elite-markets.net/eddn/commodity/2'

    def __init__(self):
        self.schemaV1 = requests.get(self.schemaV1Url).json()
        self.schemaV2 = requests.get(self.schemaV2Url).json()

    def ingest(self, data):
        try:
            validate(data, self.schemaV1)
            return self.ingest_v1(data)
        except ValidationError:
            pass

        try:
            validate(data, self.schemaV2)
            return self.ingest_v2(data)
        except ValidationError:
            pass

    @staticmethod
    def ingest_v1(data):
        message = data['message']

        try:
            commodity = Commodity.objects.get(name=message['itemName'])
            system = System.objects.get(name=message['systemName'])
            station = Station.objects.get(name=message['stationName'], system=system)

            defaults = {
                'buy_price': message['buyPrice'],
                'sell_price': message['sellPrice'],
                'supply': message['stationStock'],
                'supply_level': message.get('supplyLevel', None),
                'demand': message['demand'],
                'demand_level': message.get('demandLevel', None)
            }

            object, created = StationCommodity.objects.update_or_create(commodity=commodity, station=station,
                                                                        defaults=defaults)

            if created:
                print('Created', object)
            else:
                print('Updated', object)
        except Commodity.DoesNotExist:
            pass
        except Station.DoesNotExist:
            pass
        except System.DoesNotExist:
            pass

    @staticmethod
    def ingest_v2(data):
        message = data['message']

        try:
            system = System.objects.get(name=message['systemName'])
            station = Station.objects.get(name=message['stationName'], system=system)

            for item in message['commodities']:
                commodity = Commodity.objects.get(name=item['name'])

                defaults = {
                    'buy_price': item['buyPrice'],
                    'sell_price': item['sellPrice'],
                    'supply': item['supply'],
                    'supply_level': item.get('supplyLevel', None),
                    'demand': item['demand'],
                    'demand_level': item.get('demandLevel', None)
                }

                object, created = StationCommodity.objects.update_or_create(commodity=commodity, station=station,
                                                                            defaults=defaults)

                if created:
                    print('Created', object)
                else:
                    print('Updated', object)
        except Commodity.DoesNotExist:
            pass
        except Station.DoesNotExist:
            pass
        except System.DoesNotExist:
            pass
