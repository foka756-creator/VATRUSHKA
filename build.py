#!/usr/bin/env python3
"""Генерирует статический сайт магазина «Весма» (данные с Ozon, 14.10.2026)."""
import html, pathlib

OUT = pathlib.Path(__file__).parent
SELLER = "https://www.ozon.ru/seller/magazin-5504707-5504707/"
IMG = {
 "5566452945": "multimedia-1-q/wc1000/14645812778", "5566312002": "multimedia-1-9/wc1000/14627211633",
 "5567333594": "multimedia-1-z/wc1000/14626901447", "5567018362": "multimedia-1-m/wc1000/14634124834",
 "5567078364": "multimedia-1-c/wc1000/14627183844", "5567320973": "multimedia-1-s/wc1000/14627046376",
 "5567310148": "multimedia-1-m/wc1000/14643937210", "5962820367": "multimedia-1-g/wc1000/20099581468",
 "5566983102": "multimedia-1-7/wc1000/14627339467", "5567067707": "multimedia-1-h/wc1000/14627153969",
 "5567297670": "multimedia-1-f/wc1000/14637765363", "5566589288": "multimedia-1-9/wc1000/14627117889",
 "5566617843": "multimedia-1-v/wc1000/14636516575", "5566541436": "multimedia-1-l/wc1000/14645222733",
 "5566566375": "multimedia-1-r/wc1000/14627668923", "5566999168": "multimedia-1-x/wc1000/14627269545",
 "5963631753": "multimedia-1-9/wc1000/20102163633", "5985812358": "multimedia-1-8/wc1000/20175357392",
 "5567624182": "multimedia-1-5/wc1000/14212067477", "5567684578": "multimedia-1-4/wc1000/14212319152",
}
# id, тип, цвет, размер, цена, цена2, старая цена, остаток, отзывов
T, L = "Тюбинг, диаметр 100 см", "Ледянка"
ROWS = [
 ("5566452945", T, "Небесный", "100 см", 4522, 5024, None, None, 1),
 ("5566312002", T, "Небесный", "100 см", 4522, 5024, None, None, 0),
 ("5567333594", T, "Небесный", "100 см", 4522, 5024, None, None, 0),
 ("5567018362", T, "Небесный", "100 см", 4522, 5024, None, None, 0),
 ("5567078364", T, "Небесный", "100 см", 4522, 5024, None, None, 0),
 ("5567320973", T, "Небесный", "100 см", 4522, 5024, None, None, 0),
 ("5567310148", T, "Небесный", "100 см", 4522, 5024, None, None, 0),
 ("5962820367", T, "Небесный", "100 см", 4035, 4484, 10300, 3, 0),
 ("5566983102", T, "Бордовый", "100 см", 4522, 5024, None, None, 0),
 ("5567067707", T, "Розовый", "100 см", 4522, 5024, None, None, 0),
 ("5567297670", T, "Зелёный", "100 см", 4522, 5024, None, None, 0),
 ("5566589288", T, "Чёрный", "100 см", 4522, 5024, None, None, 0),
 ("5566617843", T, "Красный", "100 см", 4972, 5524, None, None, 0),
 ("5566541436", T, "Жёлтый", "100 см", 4522, 5024, None, None, 0),
 ("5566566375", T, "Синий", "100 см", 4522, 5024, None, None, 0),
 ("5566999168", T, "Коричнево-красный", "100 см", 4522, 5024, None, None, 0),
 ("5963631753", L, "Фиолетовый", "45 см", 902, 1002, 2480, 3, 0),
 ("5985812358", L, "Фиолетовый", "55 см", 1015, 1128, 2930, 3, 0),
 ("5567624182", L, "Светло-зелёный", "45 см", 1272, 1414, None, None, 0),
 ("5567684578", L, "Светло-зелёный", "55 см", 1148, 1275, None, None, 0),
]
e = html.escape
rub = lambda n: f"{n:,}".replace(",", " ") + " ₽"
img = lambda i, w=1000: f"https://ir.ozone.ru/s3/{IMG[i].replace('wc1000', f'wc{w}')}.jpg"
def title(r): return f"{r[1]}, {r[2].lower()}" if r[1] == T else f"Ледянка {r[3]}, {r[2].lower()}"
def url(i): return f"https://www.ozon.ru/product/{i}/"

HEAD = """<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="referrer" content="no-referrer"><link rel="stylesheet" href="{p}style.css"></head><body>
<header><a class="logo" href="{p}index.html">Весма</a><nav><a href="{p}index.html#catalog">Каталог</a><a href="{SELLER}" target="_blank" rel="noopener">Магазин на Ozon</a></nav></header>"""
FOOT = "<footer>Данные и фото взяты со страницы магазина на Ozon на 14.10.2026. Цены и наличие могут измениться: актуальные данные — на Ozon.</footer></body></html>"

def card(r):
    i = r[0]; old = f'<s>{rub(r[6])}</s>' if r[6] else ""
    badge = f'<span class="badge">−{round(100 - r[4] * 100 / r[6])}%</span>' if r[6] else ""
    left = f'<small>Осталось {r[7]} шт.</small>' if r[7] else ""
    return (f'<a class="card" href="product/{i}.html">{badge}<img loading="lazy" referrerpolicy="no-referrer" src="{img(i, 600)}" alt="{e(title(r))}">'
            f'<div class="b"><h3>{e(title(r))}</h3><div class="p"><b>{rub(r[4])}</b> {old}</div>{left}</div></a>')

slides = "".join(
    f'<a class="slide" href="product/{r[0]}.html"><img referrerpolicy="no-referrer" src="{img(r[0])}" alt="{e(title(r))}">'
    f'<div class="cap"><b>{e(title(r))}</b><span>{rub(r[4])}</span></div></a>'
    for r in ROWS)
dots = "".join(f'<button aria-label="Слайд {n+1}"></button>' for n in range(len(ROWS)))
index = (HEAD.format(t="Весма — тюбинги и ледянки", p="", SELLER=SELLER) + f"""
<section class="hero"><div class="carousel" id="car"><div class="track">{slides}</div>
<button class="nav prev" aria-label="Назад">‹</button><button class="nav next" aria-label="Вперёд">›</button><div class="dots">{dots}</div></div></section>
<main id="catalog"><h1>Тюбинги и ледянки</h1><p class="sub">{len(ROWS)} товаров · Россия · магазин «Весма» на Ozon</p>
<div class="grid">{"".join(card(r) for r in ROWS)}</div></main>
<script src="carousel.js"></script>""" + FOOT)
(OUT / "index.html").write_text(index, encoding="utf-8")

(OUT / "product").mkdir(exist_ok=True)
for r in ROWS:
    i = r[0]
    specs = [("Тип", "Тюбинг" if r[1] == T else "Ледянка"), ("Диаметр" if r[1] == T else "Длина", r[3]), ("Цвет", r[2]),
             ("Страна-изготовитель", "Россия"), ("Артикул Ozon", i)]
    specs.insert(3, ("Аудитория", "Взрослая, детская") if r[1] == T else ("Пол ребёнка", "Унисекс"))
    rows = "".join(f"<tr><th>{k}</th><td>{e(str(v))}</td></tr>" for k, v in specs)
    old = f"<s>{rub(r[6])}</s>" if r[6] else ""
    left = f'<p class="warn">Осталось {r[7]} шт.</p>' if r[7] else ""
    rev = "1 отзыв, оценка 5" if r[8] else "Пока нет отзывов"
    page = (HEAD.format(t=title(r) + " — Весма", p="../", SELLER=SELLER) + f"""
<main class="prod"><img referrerpolicy="no-referrer" src="{img(i)}" alt="{e(title(r))}"><div><a class="back" href="../index.html#catalog">← Каталог</a>
<h1>{e(title(r))}</h1><p class="sub">{rev}</p><div class="price"><b>{rub(r[4])}</b> {old}</div>
<p class="sub">{rub(r[5])} — цена «с другими банками» на Ozon</p>{left}
<table>{rows}</table><a class="buy" href="{url(i)}" target="_blank" rel="noopener">Купить на Ozon</a></div></main>""" + FOOT)
    (OUT / "product" / f"{i}.html").write_text(page, encoding="utf-8")
print("ok", len(ROWS))
