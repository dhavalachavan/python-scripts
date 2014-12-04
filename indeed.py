import indeed 

token = '7889129902747288'

api = indeed(token)

json_results = api.search('network engineer,ca')

print json_results
