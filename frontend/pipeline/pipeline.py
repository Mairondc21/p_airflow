from time import sleep
from loguru import logger


logger.add("execution_logs.log", format="{time} - {message}", level="INFO", rotation="1 day")

def primeira_att():
    logger.info("Minha primeira atividade")
    sleep(2)

def segunda_att():
    logger.info("Minha segunda atividade")
    sleep(2)

def terceira_att():
    logger.info("Minha terceira atividade")
    sleep(2)

def pipeline():
    primeira_att()
    segunda_att()
    terceira_att()

    logger.info("pipeline finalizaou")


if __name__ == "__main__":
    pipeline()
