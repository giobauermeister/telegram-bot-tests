# primeiro importamos a biblioteca telegram, instalada pelo Python-PIP
import telegram			
# e tambem importamos a biblioteca sleep de time, para poder criar
# "delay" no codigo Python.
from time import sleep 

# Faz os imports de bibliotecas para tratar erros de conexao URL.
try:
    from urllib.error import URLError
except ImportError:
    from urllib2 import URLError
	
# Criamos uma rotina main para gerir o codigo principal
def main():
    # Variavel update_id - usada pelo Telegram
    update_id = None

    # Criamos um objeto bot inserindo o Token fornecido
    # pelo The BotFather	
    bot = telegram.Bot('170008782:AAHt0_f6Ex3uVHkyvxl7JekhZ7GVBPXHP6w')

    print 'Bot Telegram iniciado...'

    # Loop infinito - programa em execucao
    while True:
        try:
            update_id = edisonGramBot(bot, update_id)
        except telegram.TelegramError as e:
            # Se ocorrer algum problema, lentidao, por ex:
            if e.message in ("Bad Gateway", "Timed out"):
                sleep(1) # Espera 1 segundo...
            else: # Caso contrario, lanca excessao.
                raise e
        except URLError as e:
            # Ha problemas de rede na execucao...
            sleep(1)


def edisonGramBot(bot, update_id):
    # Requisita atualizacoes depois da ultima id de update - update_id
	
    # bot.getUpdates(offset, timeout) - offset eh o ponto de partida em
    # que comeca a procurar novas atualizacoes de mensagens, timeout eh 
    # tempo minimo de espera para retorno da requisicao de resposta.
    for update in bot.getUpdates(offset=update_id, timeout=10):
        
        # o chat_id eh a id do chat de comunicacao Telegram
        # eh necessaria para o bot identificar a conversa e
	# gerar e enviar a resposta
        chat_id = update.message.chat_id
	
        # atualiza o indice update_id - para ref novas mensagens
        update_id = update.update_id + 1
	
        # Captura a mensagem de texto enviada ao bot no dado chat_id
        message = update.message.text

        if message:
            # Envia a mensagem para o chat_id especifico, com a mensagem 
	    # parametrizada.
            bot.sendMessage(chat_id=chat_id, text=message)

    # retorna o ultimo update_id para servir de referencia
    return update_id

# Rotina essencial para executar a rotina main() quando o codigo python
# eh executado.
if __name__ == '__main__':
    main()
