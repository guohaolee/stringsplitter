
def test_api(client):
    response = client.get('/api/v1/')
    assert response.status_code == 200

def test_endpoint(client):
    response = client.get('/api/v1/stringvalidation/LoveBeersGymHealthyPHP')
    assert response.status_code == 200
    assert response.json.get('output', '') == 'Love Beers Gym Healthy PHP'

def test_string_split(client):
    string = 'MSSQLhsqldbLovebeersAuthorizationPHPRunningGymmssqlJavaScript'
    response = client.get('/api/v1/stringvalidation/%s' % string)
    result = response.json.get('blaclisted', '')

    with open('dev/blacklist_strings.txt', 'r') as file:
        data = file.read().splitlines()

    compare = [r for r in data if r in result]
    print()

    assert response.status_code == 200
    assert (set(compare) - set(result)) == set()
