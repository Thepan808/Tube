class Presets(object):
    HELP_TEXT = """
<b><u>Comandos:</u></b>
<code>
🔰 Envie qualquer imagem para configurar uma miniatura permanente para os vídeos de download.

🔰 Para excluir a miniatura definida anteriormente, selecione o botão</code> <b>/help</b> <code>e clique no botão Excluir.

🔰 Se nenhuma miniatura personalizada estiver disponível, a miniatura de vídeo padrão será usada nos vídeos de download.

🔰 Pesquise em linha ou cole qualquer URL do YouTube para iniciar a atividade do bot.

🔰 SUDO USERS pode transmitir as mensagens para todos os usuários do bot. Use:</code>
<b>/subs</b><code> - para contar assinantes</code>
<b>/send</b><code>  - para transmitir (como resposta)</code>

<b>Entre:</b><a href='https://t.me/botssaved'><b> Suporte</b></a> | Criado por\
<a href='https://t.me/the_panda_official'><b> Criador</b></a>   
    """

    OPTIONS_TXT = "<code>🔰 Selecione a opção 🔰</code>"
    WELCOME_MSG = "<code>Olá...</code><b>{}</b> 👋\n<code>Eu sou um bot downloader do YouTube com muitos recursos. " \
                  "Pesquise vídeos embutidos e clique para prosseguir para o download.</code>"
    RESULTS_TXT = "👀 Resultados:"
    NO_RESULTS = "❌ Sem resultados"
    DESCRIPTION = "Duração: {} || {}"
    NOT_AUTH_TXT = "<b>Error : </b>\n\n<code>Você não está autorizado a usar este bot.</code>"
    DEFAULT_TITLE = "Canal"
    DEFAULT_THUMB_URL = "https://image.flaticon.com/icons/png/512/25/25231.png"
    DEFAULT_LINK = "https://t.me/botssaved"
    DEFAULT_DESCRIPTION = "Link: Canal | Criador"
    DEV_TITLE = "Informações do desenvolvedor"
    DEV_THUMB_URL = "https://freepikpsd.com/media/2019/10/software-developer-icon-png-2-Transparent-Images.png"
    DEV_LINK = "https://t.me/the_panda_official"
    DEV_DESCRIPTION = "Nome: The Panda | Telegram"
    SHARE_BUTTON_TEXT = "Olá.. 👋\nSobre isso : @{username}\nPara pesquisar e baixar vídeos do YouTube"
    SAVED_THUMB = "<b>✅ Miniatura salva com êxito</b>\n<code>Este arquivo será usado no próximo YouTube " \
                  "downloads até que você limpá-lo !</code> "
    WAIT_MESSAGE = "<code>Processamento...</code>"
    THUMB_CAPTION = "<code>Esta imagem é a sua miniatura atual, toque em </code><b> DEL THUMB </b><code> se desejar " \
                    "limpá-lo !</code> "
    NO_THUMB = "❌ Não é possível encontrar nenhuma miniatura no seu local, faça o upload de uma imagem para defini-la.."
    DEL_THUMB_CNF = "Thumbnail Limpo com êxito ✅"
    LINK_ERROR = "<b>Error : </b>\n\n<code>Ocorreu algum erro durante o processo !\n por favor, tente novamente mais tarde..</code>"
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    FINISHED_PROGRESS_STR = "◼️"
    UN_FINISHED_PROGRESS_STR = "◻️"
    SOURCE_URL = "https://github.com/m4mallu/inline-tube-mate"
    SUPPORT_URL = "https://t.me/RMProjects"
    CHECKING_LINK = "⏳ <code>Analyzing your link...</code>"
    DOWNLOAD_START = "⬇️ <code>Download Initiated...</code>"
    UPLOAD_START = "⬆️ <code>Upload Initiated...</code>"
    NOT_DOWNLOADABLE = "<b>This URL is not downloadable !</b> 🙄"
    CANCEL_PROCESS = "<b>Process Cancelled Successfully</b>  ✅"
    SEND_TEXT = "<b>Processing...</b>\n<i>This message will automatically disappear when the broadcasting is " \
                "finished</i> "
    REPLY_ERROR = "<i>Use this command as a replay to any telegram message with out any spaces.</i>"
    USERS_LIST = "<b>Total: {}</b>\n\nSubscribers - {}\nBlocked / Deleted - {}"
    WAIT_MSG = "<b>Processing...</b>\n<i>This will take some time...</i>"
    PROMPT_THUMB = "<b>Do you want to set this image as a thumbnail?</b>"
    FORMAT_SELECTION = """
<code>Title - </code><b>{}</b>

<code>Channel -</code> <a href={}><b>{}</b></a>
<code>Uploaded On -</code> <b>{}</b>
<code>Views -</code> <b>{}  |</b>  <code>Rating:</code> <b>{}</b>

👇<code>Select the required format</code>👇
    """
    NOT_SUB_TXT = "<b>Oopz </b> 😯\n\n<code>In order to use this feature, You need to join my channel.</code>"
    BOT_NOT_PRESENT = "<b>Error : </b>\n\n<code>Bot need to be an admin to the force subscribe chat !</code>"
    NO_INVITE_METHOD = "<b>Error : </b>\n\n<code>Chat invite method not found ! Try to generate an invite " \
                       "link in your force subscribe chat.</code>"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""
    CUSTOM_CAPTION_UL_FILE = "\xad \xad\n<b>{}</b>\n\n<b>DL Credits: </b><b><a " \
                             "href='https://github.com/m4mallu'> M4Mallu</a></b> "
    RCHD_TG_API_LIMIT = "Detected File Size: {}\n\nSorry. But, I cannot upload files " \
                        "greater than 1.95GB due to Telegram API limitations."
    AD_STRING_TO_REPLACE = "please report this issue on https://yt-dl.org/bug . Make sure you are using the " \
                           "latest version; see  https://yt-dl.org/update  on how to update. Be sure to call " \
                           "youtube-dl with the --verbose flag and include its complete output."
    INITIAL_MEDIA = "https://telegra.ph/file/c3f88ba6883554654fb4e.png"
    ERROR_MEDIA = "https://telegra.ph/file/27fd810c591c884dba11d.jpg"
    SETTINGS = "<code>Need an update in settings?</code>"
