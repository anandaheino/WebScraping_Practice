from scrapy import Field, Item
from scrapy.loader.processors import Join

class SyngentaCaseItem(Item):

    # defyning the fields for the items:
    nome_semente = Field()
    habito_crescimento = Field()
    cor_flor = Field()
    grupo_maturacao = Field()
    pubescencia = Field()
    acamamento = Field()
    hilo = Field()
    altura_planta = Field()
    pms_medio = Field()
    insercao_vagem = Field()
    beneficios = Field(output_processor= Join())

    # other very usefull fields:
    url = Field()
    date = Field()
