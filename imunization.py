import requests
import json

#Acessando API
url = "https://imunizacao-es.saude.gov.br/_search"

payload = json.dumps({
  "size": 1000
})
headers = {
  'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k=',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

vacinas = response.json()

#Variáveis para contagem de doses por fabricante
astrazeneca_doses = 0
astrazenenecafiocruz_doses = 0
janssen_doses = 0
pediatricapfizer_doses = 0
pfizer_doses = 0
sinovac_doses = 0
sinovacbutantan_doses = 0

#Lista para armazenar municipios sem duplicatas
lista_municipios = []

for j in vacinas['hits']['hits']:
	lista_municipios.append(j['_source']['paciente_endereco_nmMunicipio'])
	
lista_municipios = list(dict.fromkeys(lista_municipios))

#Contagem de doses aplicadas
for i in vacinas['hits']['hits']:
    
    if i['_source']['vacina_nome'] == 'COVID-19 ASTRAZENECA - ChAdOx1-S':
        astrazeneca_doses += 1
        
    if i['_source']['vacina_nome'] == 'COVID-19 ASTRAZENECA/FIOCRUZ - COVISHIELD':
        astrazenenecafiocruz_doses +=1
    
    if i['_source']['vacina_nome'] == 'COVID-19 JANSSEN - Ad26.COV2.S':
        janssen_doses +=1
    
    if i['_source']['vacina_nome'] == 'COVID-19 PEDIATRICA - PFIZER COMIRNATY':
        pediatricapfizer_doses+=1
        
    if i['_source']['vacina_nome'] == 'COVID-19 PFIZER - COMIRNATY':
        pfizer_doses+=1
        
    if i['_source']['vacina_nome'] == 'COVID-19 SINOVAC - CORONAVAC':
        sinovac_doses+=1
    
    if i['_source']['vacina_nome'] == 'COVID-19 SINOVAC/BUTANTAN - CORONAVAC':
        sinovacbutantan_doses+=1
        
total_doses = astrazeneca_doses + astrazenenecafiocruz_doses + janssen_doses + pediatricapfizer_doses + pfizer_doses + sinovac_doses + sinovacbutantan_doses

#Listas para contagem de doses por fabricante de acordo com o municipio
total_municipios_astrazeneca = []
total_municipios_astrazenecafiocruz = []
total_municipios_janssen = []
total_municipios_pediatricapfizer = []
total_municipios_pfizer = []
total_municipios_sinovac = []
total_municipios_sinovacbutantan = []

total_municipio = 0
uf_atual  = ''

#Computa as doses por municipio da vacina Astrazeneca
for i in range(0, len(lista_municipios)):
    	for j in vacinas['hits']['hits']:
    		
    		if j['_source']['vacina_nome'] == 'COVID-19 ASTRAZENECA - ChAdOx1-S' and j['_source']['paciente_endereco_nmMunicipio'] == lista_municipios[i]:
    			
    			total_municipio +=1
    			uf_atual  = j['_source']['paciente_endereco_uf']
    		elif j['_source']['vacina_nome'] != 'COVID-19 ASTRAZENECA - ChAdOx1-S' and j['_source']['paciente_endereco_nmMunicipio'] == lista_municipios[i]:
    			uf_atual  = j['_source']['paciente_endereco_uf']
    	if total_municipio>0:	
    		total_municipios_astrazeneca.append({"municipio": lista_municipios[i], "uf": uf_atual, 'total': total_municipio})
    	total_municipio = 0

#Computa as doses por municipio da vacina Astrazeneca/Fiocruz
for i in range(0, len(lista_municipios)):
    	for j in vacinas['hits']['hits']:
    		
    		if j['_source']['vacina_nome'] == 'COVID-19 ASTRAZENECA/FIOCRUZ - COVISHIELD' and j['_source']['paciente_endereco_nmMunicipio'] == lista_municipios[i]:
    			
    			total_municipio +=1
    			uf_atual  = j['_source']['paciente_endereco_uf']
    		elif j['_source']['vacina_nome'] != 'COVID-19 ASTRAZENECA/FIOCRUZ - COVISHIELD' and j['_source']['paciente_endereco_nmMunicipio'] == lista_municipios[i]:
    			uf_atual  = j['_source']['paciente_endereco_uf']
    	if total_municipio>0:	
    		total_municipios_astrazenecafiocruz.append({"municipio": lista_municipios[i], "uf": uf_atual, 'total': total_municipio})
    	total_municipio = 0

#Computa as doses por municipio da vacina Janssen
for i in range(0, len(lista_municipios)):
    	for j in vacinas['hits']['hits']:
    		
    		if j['_source']['vacina_nome'] == 'COVID-19 JANSSEN - Ad26.COV2.S' and j['_source']['paciente_endereco_nmMunicipio'] == lista_municipios[i]:
    			
    			total_municipio +=1
    			uf_atual  = j['_source']['paciente_endereco_uf']
    		elif j['_source']['vacina_nome'] != 'COVID-19 JANSSEN - Ad26.COV2.S' and j['_source']['paciente_endereco_nmMunicipio'] == lista_municipios[i]:
    			uf_atual  = j['_source']['paciente_endereco_uf']
    	if total_municipio>0:	
    		total_municipios_janssen.append({"municipio": lista_municipios[i], "uf": uf_atual, 'total': total_municipio})
    	total_municipio = 0
    	
#Computa as doses por municipio da vacina Pediátrica Pfizer
for i in range(0, len(lista_municipios)):
    	for j in vacinas['hits']['hits']:
    		
    		if j['_source']['vacina_nome'] == 'COVID-19 PEDIATRICA - PFIZER COMIRNATY' and j['_source']['paciente_endereco_nmMunicipio'] == lista_municipios[i]:
    			
    			total_municipio +=1
    			uf_atual  = j['_source']['paciente_endereco_uf']
    		elif j['_source']['vacina_nome'] != 'COVID-19 PEDIATRICA - PFIZER COMIRNATY' and j['_source']['paciente_endereco_nmMunicipio'] == lista_municipios[i]:
    			uf_atual  = j['_source']['paciente_endereco_uf']
    	if total_municipio>0:	
    		total_municipios_pediatricapfizer.append({"municipio": lista_municipios[i], "uf": uf_atual, 'total': total_municipio})
    	total_municipio = 0
    	
#Computa as doses por municipio da vacina Pfizer
for i in range(0, len(lista_municipios)):
    	for j in vacinas['hits']['hits']:
    		
    		if j['_source']['vacina_nome'] == 'COVID-19 PFIZER - COMIRNATY' and j['_source']['paciente_endereco_nmMunicipio'] == lista_municipios[i]:
    			
    			total_municipio +=1
    			uf_atual  = j['_source']['paciente_endereco_uf']
    		elif j['_source']['vacina_nome'] != 'COVID-19 PFIZER - COMIRNATY' and j['_source']['paciente_endereco_nmMunicipio'] == lista_municipios[i]:
    			uf_atual  = j['_source']['paciente_endereco_uf']
    	if total_municipio>0:	
    		total_municipios_pfizer.append({"municipio": lista_municipios[i], "uf": uf_atual, 'total': total_municipio})
    	total_municipio = 0
    	
#Computa as doses por municipio da vacina Sinovac
for i in range(0, len(lista_municipios)):
    	for j in vacinas['hits']['hits']:
    		
    		if j['_source']['vacina_nome'] == 'COVID-19 SINOVAC - CORONAVAC' and j['_source']['paciente_endereco_nmMunicipio'] == lista_municipios[i]:
    			
    			total_municipio +=1
    			uf_atual  = j['_source']['paciente_endereco_uf']
    		elif j['_source']['vacina_nome'] != 'COVID-19 SINOVAC - CORONAVAC' and j['_source']['paciente_endereco_nmMunicipio'] == lista_municipios[i]:
    			uf_atual  = j['_source']['paciente_endereco_uf']
    	if total_municipio>0:	
    		total_municipios_sinovac.append({"municipio": lista_municipios[i], "uf": uf_atual, 'total': total_municipio})
    	total_municipio = 0
    	
#Computa as doses por municipio da vacina Sinovac/Butantan
for i in range(0, len(lista_municipios)):
    	for j in vacinas['hits']['hits']:
    		
    		if j['_source']['vacina_nome'] == 'COVID-19 SINOVAC/BUTANTAN - CORONAVAC' and j['_source']['paciente_endereco_nmMunicipio'] == lista_municipios[i]:
    			
    			total_municipio +=1
    			uf_atual  = j['_source']['paciente_endereco_uf']
    		elif j['_source']['vacina_nome'] != 'COVID-19 SINOVAC/BUTANTAN - CORONAVAC' and j['_source']['paciente_endereco_nmMunicipio'] == lista_municipios[i]:
    			uf_atual  = j['_source']['paciente_endereco_uf']
    	if total_municipio>0:	
    		total_municipios_sinovacbutantan.append({"municipio": lista_municipios[i], "uf": uf_atual, 'total': total_municipio})
    	total_municipio = 0

#Dictionary para armazenar e organizar os dados finais
vacinas_contagem = {
"total_doses_aplicadas": total_doses,
"ASTRAZENECA": {
"total_doses": astrazeneca_doses,
"total_por_municipio": total_municipios_astrazeneca
},
"ASTRAZENECA/FIOCRUZ": {
"total_doses": astrazenenecafiocruz_doses,
"total_por_municipio": total_municipios_astrazenecafiocruz
},
"JANSSEN": {
"total_doses": janssen_doses,
"total_por_municipio": total_municipios_janssen
},
"PEDIATRICA - PFIZER": {
"total_doses": pediatricapfizer_doses,
"total_por_municipio": total_municipios_pediatricapfizer
},
"PFIZER": {
"total_doses": pfizer_doses,
"total_por_municipio": total_municipios_pfizer
},
"SINOVAC": {
"total_doses": sinovac_doses,
"total_por_municipio": total_municipios_sinovac
},
"SINOVAC/BUTANTAN": {
"total_doses": sinovacbutantan_doses,
"total_por_municipio": total_municipios_sinovacbutantan
}
}

#Criação do json final e impressão na tela
json_object = json.dumps(vacinas_contagem, indent = 4) 
with open("etapa1.json", "w") as outfile: 
    outfile.write(json_object) 
