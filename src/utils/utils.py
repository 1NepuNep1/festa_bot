import random

names_array = [
    "Сегодня ты голубой Эд Ширан",
    "Сегодня ты пусси Джаред Лето",
    "Сегодня ты квадробер Джаред Лето",
    "Сегодня ты фурри котик Джаред Лето",
    "Сегодня ты золотой Джоджо поуз Лил Нас Икс",
    "Сегодня ты черная Сара Джессика Паркер с горящей башкой",
    "Сегодня ты Lizzo Селедкина Чио Рио",
    "Сегодня тебя не пустили на мет гала",
    "Сегодня ты Доджа Кэт полностью в рэд",
    "Сегодня ты Чонгачкук умер на СВО 26-летний певец Чон Джонгук участвовал в штурме Авдеевки, в результате чего получил травмы несовместимые с жизнью😭",
    "Сегодня ты мармеладная задница Харибо Кара Делевинь",
    "Сегодня ты Доджа Кэт никотиновая падла дудкососка",
    "Сегодня ты Шакирку за шкирку в ебануто красном платье",
    "Сегодня ты Карди Бездна",
    "Сегодня ты Мики гламур банан Минаж",
    "Сегодня ты Деми Мур педовка в черном платье",
    "Сегодня ты Деми Мур в эстетичном черном фотообои платье с розами",
    "Сегодня ты Айс Спайс в бежевом платьице, давай сбежим на тебя буду тратиться",
    "Сегодня ты Блуши Дарлинг, никаких фото, мужской пол мимо",
    "Сегодня ты Иман цыганка",
    "Сегодня ты Иман солнышко, улыбайся чаще, пупсик",
    "Сегодня ты Асап Роки на лютейшем дрипе",
    "Сегодня ты Асап Роки притти мазэфака",
    "Сегодня ты Асап Роки такой приблатненный моднявый, забацай голивудскую улыбочку",
    "Сегодня ты Кэти Пери бургер",
    "Сегодня ты ебануто загадочный ловелас Бэд Банни",
    "Сегодня ты Рита Штора",
    "Сегодня ты Кайли Дженнер выходишь замуж за Тревиса Мирного😈🐺🥀",
    "Сегодня ты шина Мишлен Джиджи Хадид",
    "Сегодня ты Пи Дидди и мы знаем чем ты занимался прошедшим летом",
    "Сегодня ты на комфортном, словно Асап Роки",
    "Сегодня ты куришь в туалете, в принципе как и всегда",
    "Сегодня ты Ким Петрас, выбравшая хоббихорсинг",
    "Сегодня ты би, и мы не про бизнес-информатику",
    "Сегодня ты чёрный, но мы за белых",
    "Сегодня ты сияешь, прям как Кэти Перри",
    "Сегодня ты на серьёзном, но внутри на расслабоне",
    "Сегодня ты Джаред Лето (умри нахуй)",
    "Сегодня all eyes on you, прям как на Эзре Миллере",
    "Сегодня ты не расчесался",
    "Сегодня ты шкаф",
    "Сегодня ты рианна на сковородке"
]

links = [
    "https://i.ibb.co/CVSZwr6/fc576d5ea720332daac0e31c8962941c.jpg",
    "https://i.ibb.co/BLWgb9F/51d8ecdd05d8654c9eeec2b110a22c85.jpg",
    "https://i.ibb.co/BLWgb9F/51d8ecdd05d8654c9eeec2b110a22c85.jpg",
    "https://i.ibb.co/BLWgb9F/51d8ecdd05d8654c9eeec2b110a22c85.jpg",
    "https://i.ibb.co/Zck6rB1/3a13c95c34defd2ccd901ddfc2be0816.jpg",
    "https://i.ibb.co/bzyrhrw/7e76cc6c3fe11edd02df1c6323bb6691.jpg",
    "https://i.ibb.co/ccRnn1Q/04f48eaef1263c0fb6224bc62d9a15b2.jpg",
    "https://i.ibb.co/m4RgLcF/2024-09-13-1-24-10.png",
    "https://i.ibb.co/G3jvb7K/ff09d95351470ea30dacc2a11d312575.jpg",
    "https://i.ibb.co/qnY4J91/600x600-1-417a8c4c7ddf15399b5b301913233f8f-900x900-0x8df-Fu0zj-3186858235363876079.jpg",
    "https://i.ibb.co/sKRmJf1/03baf5eedbac77a40284ca2bb23fcf7c.jpg",
    "https://i.ibb.co/SJqngh6/70492871-12038539-image-a-12-1683050056118.jpg",
    "https://i.ibb.co/g7jtdSx/138be44ec4f40655b2005670a06f2538.jpg",
    "https://i.ibb.co/ZgncB8H/6c84d51586d8820e44815646b7a2ee83.jpg",
    "https://i.ibb.co/JK4FYNC/40979b35b031dbf0311ae4b7be2b3c79.jpg",
    "https://i.ibb.co/nLfGXCR/de9ebb0a8eac5f4dde1d3cc4e382ab2d.jpg",
    "https://i.ibb.co/nLfGXCR/de9ebb0a8eac5f4dde1d3cc4e382ab2d.jpg",
    "https://i.ibb.co/1dwKBR4/c9ee8265f9a6782f6686901f79b0aac5.jpg",
    "https://i.ibb.co/THXphpB/10b9cc501872c967bda271da96824fd7.jpg",
    "https://i.ibb.co/Bcx9gm4/0b980516b38d69b5f8aeb21d586df529.jpg",
    "https://i.ibb.co/Bcx9gm4/0b980516b38d69b5f8aeb21d586df529.jpg",
    "https://i.ibb.co/fX46dfv/4f7a328137316a0ee75fd1f87bf5f4d5.jpg",
    "https://i.ibb.co/fX46dfv/4f7a328137316a0ee75fd1f87bf5f4d5.jpg",
    "https://i.ibb.co/fX46dfv/4f7a328137316a0ee75fd1f87bf5f4d5.jpg",
    "https://i.ibb.co/G2TFGT9/a0942afe31ce2054c449237facec4cae.jpg",
    "https://i.ibb.co/1mBwB2K/c73bed8fbaf79ab11c742c0fa805cf89.jpg",
    "https://i.ibb.co/cggxjYG/6e7791fac681af22a0d62d86f5c23d2e.jpg",
    "https://i.ibb.co/fX10vrS/9d6fa4dcc72db388d7cb438b3387c999.jpg",
    "https://i.ibb.co/Qrmg0ZT/9da2d72645c426db11f66d4f7949b5c0.jpg",
    "https://i.ibb.co/Q9vr6Dc/16276c493a61a71bf8a28e27987d4297.jpg",
    "https://i.ibb.co/bbvjgn4/d78f7ea39164f21226721de42268e76f.jpg",
    "https://i.ibb.co/s2WRYr2/2024-09-13-1-25-53.png",
    "https://i.ibb.co/4RvFkSb/961a4ce0d556a151a730e7c057d2732a.jpg",
    "https://i.ibb.co/8grTq9x/19f824be8ccf9af09f78c1801350a589.jpg",
    "https://i.ibb.co/k516GwJ/a473fcb89cb320b7d6b470d6cd870769.jpg",
    "https://i.ibb.co/X7jgF7W/148493a829ff31690254b410557d448d.jpg",
    "https://i.ibb.co/5Fk6crn/97861eac4a726e870c8b37f8687e590f.jpg",
    "https://i.ibb.co/Ln4tJVm/e8e700763bf7c1494ff1898e10fa32de.jpg",
    "https://i.ibb.co/G2cLYtz/0c9bc46a2300ecfbb4ce8c9ef63b034a.jpg",
    "https://i.ibb.co/Dtt3BHK/f2b36603cd14c5292b38b57768e873de.jpg",
    "https://i.ibb.co/mN01QRF/69ed8842b535c81d47e93e329dab2320.jpg",
    "https://i.ibb.co/10PsWzk/cd7b94b6b6f058ec704559fa18a96f09.jpg"
]


step_0 = ["🤬", "😤", "😡", "👿", "😠", "🤡"]
step_5 = ["😧", "🥺", "😱", "😯", "😮", "😓"]
step_10 = ["😰", "😩", "😦", "😣", "😥", "🙁"]
step_15 = ["😐", "😬", "😑", "🙄", "🤭"]
step_20 = ["😎", "🤓", "🤠", "🥳", "😋"]
step_25 = ["🤩", "😇", "😘"]

emojis = [ "👨🏿" , "👧🏿", "🎲", "🏀", "🎯", "🎰", "⚽️", "😤", "😡", "👿", "😠",
            "😧", "🥺", "😱", "😮", "😓", "😰", "😩", "😦", "😣", "😥",
             "🙁", "😐", "😬", "😑", "🙄", "🤭", "😎", "🤓", "🤠", "🥳", "😋", "🤩", "😇", "😘",
             "🙂‍↔️", "😼", "🧟‍♀️", "🦍", "🫑", "🤸‍♂️", "😟", "🚩", "🦵🏿","🎅🏿","👩‍🦽","👙","👶🏿","👠"]

def getRandom(arr: list[str]) -> str:
  return random.choice(arr)

def generateGaussianDistribution(mu: int, sigma: int) -> float:
  return random.uniform(mu, sigma)

def transformRandomValueResult(num: int) -> str:
  # if num <= 0:
  #   return f"My dick is less 1 cm {getRandom(step_0)}"
  # if num <= 5:
  #   return f"My dick is {str(num)} cm {getRandom(step_5)}"
  # if num <= 10:
  #   return f"My dick is {str(num)} cm {getRandom(step_10)}"
  # if num <= 15:
  #   return f"My dick is {str(num)} cm {getRandom(step_15)}"
  # if num <= 20:
  #   return f"My dick is {str(num)} cm {getRandom(step_20)}"
  
  # return f"My dick is {str(num)} cm {getRandom(step_25)}"
  return names_array[num]

def getRandomLink(num: int) -> str:
  return links[num]

def getRandomEmoji(num: int) -> str:
  return emojis[num]

