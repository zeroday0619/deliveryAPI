import requests
import datetime
import json


class de_dhl:
    def __init__(self):
        self.api_url = 'https://www.logistics.dhl/shipmentTracking'
        self.STATUS_ID_MAP = {
            'picked up': {'id': 'at_pickup', 'text': '상품인수'},
            'delivered': {'id': 'delivered', 'text': '배송완료'}
        }
                
    def query(self, track_id):
        resp = requests.get(
            url=self.api_url,
            params={
                'AWB': track_id,
                'countryCode': 'g0',
                'languageCode': 'ko'
            },
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
            }
        )
        #print(resp.status_code)
        if resp.status_code != 200:
            print("ERROR")
            return
        
        return resp

    def _data(self, track_id):
        return de_dhl().query(track_id).json()
class Processing_dhl(de_dhl):
    def __init__(self):
        self.data = super()._data
        self.shippingInfo_templit = {
            'from': {
                "origin": None
            },
            'to': {
                'destination': None
            },
            'state': {
                'DeliveryStatus': None,
                'description': None,
                'location': None,
                'date': None,
                'time': None
            }
        }

    def get(self, track_id):
        data = self.data(track_id)
        results = data['results']
        
        state = results[0]
        checkpoints = state['checkpoints']
        last_checkpoint = checkpoints[0]

        templit = self.shippingInfo_templit
        templit['from']['origin'] = state['origin']['value']
        templit['to']['destination'] = state['destination']['value']
        templit['state']['DeliveryStatus'] = state['delivery']['status']
        templit['state']['description'] = last_checkpoint['description']
        templit['state']['location'] = last_checkpoint['location']
        templit['state']['date'] = last_checkpoint['date']
        templit['state']['time'] = last_checkpoint['time']
        return templit


app = Processing_dhl()
print(json.dumps(app.get("-----------"),indent=4, sort_keys=False, ensure_ascii=False))

        
        
    
    
