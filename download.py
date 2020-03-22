import urllib.request

def download():
    url = 'https://services6.arcgis.com/5jNaHNYe2AnnqRnS/arcgis/rest/services/COVID19_Japan/FeatureServer/0/query?where=%E9%80%9A%E3%81%97%3E0&returnIdsOnly=false&returnCountOnly=false&&f=pgeojson&outFields=*&orderByFields=%E9%80%9A%E3%81%97'
    title = 'COVID-19_data.json'
    urllib.request.urlretrieve(url, "{0}".format(title))