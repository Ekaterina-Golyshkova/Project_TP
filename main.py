from pathlib import Path
from datetime import datetime
import time
import schedule
import traceback

from shcedule import sync


GROUP = "26КНТ-3"
MarkFILE = Path("#пишем свой путь обсидиан") / "Tables" / "table.md" #пишем свой путь обсидиан
INTERVALH = 6
Log = Path("sync.log")


def log(msg: str) -> None:
    line = f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}"
    print(line)
    with Log.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def job():
    try:
        log(f"Старт синхронизации {GROUP}")
        out = sync(GROUP, MarkFILE)#вызвали синк делает нужн вещи
        log(f"Успех: {out}")
    except Exception as e:
        log(f"Ошибка: {e}")
        log(traceback.format_exc())


def main():
    log("Старт проги") 
    job()#запустили синхрониз сразу, чтоб не ждать часами
    schedule.every(INTERVALH).hours.do(job)

    while True:
        schedule.run_pending()
        time.sleep(300) #РЕБЯТА ЗАМЕЧАНИЕ при таком лучше сделать выбор с 2 и более часов, т.к. 1 час может уперется максимум значения,
#Вроде ничего не теряем за час к тому же программу можно перерестартнуть и она проверит сразу же расписание
#в целом можно поставить вместо 300 - 60, но мне душе спокойнее, что она просыпается раз в 5 минут, даже если оно почти не нагружает


if __name__ == "__main__":
    main()