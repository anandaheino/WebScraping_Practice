from scrapy import Field, Item
from scrapy.loader.processors import Join, TakeFirst

class SyngentaCaseItem(Item):

    # defyning the fields for the items:
    nome_semente = Field()
    habito_crescimento = Field()
    grupo_maturacao = Field()
    # acamamento = Field()
    # altura_planta = Field()
    # insercao_vagem = Field()
    cor_flor = Field()
    # pubescencia = Field()
    # hilo = Field()
    # pms_medio = Field()"""

    beneficios = Field(output_processor = Join())

    # other very usefull fields:
    url = Field()
    # project = Field()
    # spider = Field()
    # server = Field()
    date = Field()
