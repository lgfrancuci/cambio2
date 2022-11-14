import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all') #Tem lá no site da API

cotacoes_dic = cotacoes.json() #Transformar em dicionário
#print(cotacoes) #Sempre que dá certo é 200
#print(cotacoes_dic)


# In[2]:



#Vamos pegar o BID já que é o preço de compra, ou seja, cotação
print('Dolár: {}'.format(cotacoes_dic['USD']['bid']))

#Fazer o mesmo para o euro
print('Euro: {}'.format(cotacoes_dic['EUR']['bid']))


# In[3]:


usd = cotacoes_dic['USD']['bid']
usd = float(usd)
usd = usd * 0.9 - 0.05

euro = cotacoes_dic['EUR']['bid']
euro = float(euro)
euro = euro * 0.9 - 0.05

print('Dolar deve estar em {:.1f} e Euro deve estar em {:.1f}'.format(usd, euro))


# In[5]:


import requests
#U+1F600  = Emoji
#Barra invertiva e ao invés do mais coloca 000


frase = '\U0001F916 ATENÇÃO (mensagem automática): \U0001F916 \n =================================================== \n  Verificar se atualizou o \U0001F4B5 DÓLAR para {:.1f} e \U0001F4B6 EURO para {:.1f}.\n===================================================\n Caso já tenha atualizado, dê o OK aqui. Caso contrário atualize, por favor'.format(usd, euro)

payload = {
    'content': frase
}

header = {
    'authorization':'ODc1NzEwMDc0NzM4MzQzOTY2.GxEpS8.K1Cap_tFEDwQN3CWXOZgjGwH8cQaO7Sv4ioXp8'
}

request = requests.post("https://discord.com/api/v9/channels/1001665792900866061/messages", data = payload, headers = header)
#https://discord.com/api/v9/channels/983372661734400051/messages