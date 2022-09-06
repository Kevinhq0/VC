
import sys,os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

def load_json():
    with open('../Downloads/response.json') as json_obj:
        response = json.load(json_obj)
    return response


def test_load_json():
  response = load_json()
  assert isinstance(response, dict)
  assert response.get("Data Glacier") =="Cricket"




