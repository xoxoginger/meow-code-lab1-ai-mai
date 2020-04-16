from experta import *


class Religion(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        # final
        yield Fact(action="last_q")
        # считаете ли, что белье может исцелять?
        yield Fact(action="linen_healing")
        # предпочитаете индийскую или китайскую еду? вы раздражаете людей?
        yield Fact(action="food_annoying")
        # у вас есть черный кот? вы любите хумус? а пасту?
        yield Fact(action="cat_hummus_pasta")
        # хотите перевоплотиться? # как вы относитесь к бекону? # вы богаты и безумны?
        yield Fact(action="reincarnation_bacon_richmad")
        yield Fact(action="gods_number")  # скольким богам поклоняться?

    @Rule(Fact(action='gods_number'),  # gn
          NOT(Fact(GN=W())))
    def gn(self):
        temp = input("Скольким богам ты хочешь поклоняться? (одному, множеству, ни одному) ").lower()
        while temp != 'множеству' and temp != 'одному' and temp != 'ни одному':
            print("Я не понимаю. Ответь еще раз, пожалуйста.")
            temp = input("Скольким богам ты хочешь поклоняться? (одному, множеству, ни одному) ").lower()
        self.declare(Fact(GN=temp))

    @Rule(Fact(action='reincarnation_bacon_richmad'),  # rbrm
          Fact(GN=MATCH.GN),
          NOT(Fact(RBRM=W())))
    def rbrm(self, GN):
        if GN == 'множеству':
            temp = input("Хочешь перевоплотиться? (да, нет) ").lower()
            while temp != 'да' and temp != 'нет':
                print("Я не понимаю. Ответь еще раз, пожалуйста.")
                temp = input("Хочешь перевоплотиться? (да, нет) ").lower()
            self.declare(Fact(RBRM=temp))
        elif GN == 'одному':
            temp = input("Как ты относишься к бекону? (я обожаю бекон!!!, ну...) ").lower()
            while temp != 'я обожаю бекон!!!' and temp != 'ну...':
                print("Я не понимаю. Ответь еще раз, пожалуйста.")
                temp = input("Как ты относишься к бекону? (я обожаю бекон!!!, ну...)").lower()
            self.declare(Fact(RBRM=temp))
        elif GN == 'ни одному':
            temp = input("Ты богат и безумен? (да, нет) ").lower()
            while temp != 'да' and temp != 'нет':
                print("Я не понимаю. Ответь еще раз, пожалуйста.")
                temp = input("Ты богаты и безумен? (да, нет) ").lower()
            self.declare(Fact(RBRM=temp))

    @Rule(Fact(action='cat_hummus_pasta'),  # CHP
          Fact(GN=MATCH.GN),
          Fact(RBRM=MATCH.RBRM),
          NOT(Fact(CHP=W())))
    def chp(self, GN, RBRM):
        if GN == 'множеству' and RBRM == 'да':
            temp = input("У тебя есть черный кот? (да, нет) ").lower()
            while temp != 'да' and temp != 'нет':
                print("Я тебя не понимаю. Ответь еще раз, пожалуйста.")
                temp = input("У тебя есть черный кот? (да, нет) ").lower()
            self.declare(Fact(CHP=temp))
        if RBRM == 'нет' and GN == 'множеству':
            print("Ты должен следовать религии Майя.")
        if RBRM == 'я обожаю бекон!!!' and GN == 'одному':
            temp = input("А пасту? (да, фу, паста) ").lower()
            while temp != 'да' and temp != 'фу, паста':
                print("Я не понимаю. Ответь еще раз, пожалуйста.")
                temp = input("А пасту? (да, фу, паста) ").lower()
            self.declare(Fact(CHP=temp))
        if RBRM == 'ну...' and GN == 'одному':
            temp = input("Ты любишь хумус? (я обожаю хумус!!!, ну...) ").lower()
            while temp != 'я обожаю хумус!!!' and temp != 'ну...':
                print("Я не понимаю. Ответь еще раз, пожалуйста.")
                temp = input("Ты любишь хумус? (я обожаю хумус!!!, ну...) ").lower()
            self.declare(Fact(CHP=temp))
        if GN == 'ни одному' and RBRM == 'да':
            print("Стань саентологом.")
        if RBRM == 'нет' and GN == 'ни одному':
            print("Будь атеистом.")

    @Rule(Fact(action='food_annoying'),  # FA
          Fact(GN=MATCH.GN),
          Fact(RBRM=MATCH.RBRM),
          Fact(CHP=MATCH.CHP),
          NOT(Fact(FA=W())))
    def fa(self, GN, RBRM, CHP):
        if GN == 'множеству' and RBRM == 'да':
            if CHP == 'да':
                print("Тебе подходит Викка - религия колдунов.")
            if CHP == 'нет':
                temp = input("Ты предпочитаешь индийскую или китайскую еду? (индийскую, китайскую) ").lower()
                while temp != 'индийскую' and temp != 'китайскую':
                    print("Я не понимаю. Ответь еще раз, пожалуйста.")
                    temp = input("Ты предпочитаешь индийскую или китайскую еду? (индийскую, китайскую) ").lower()
                self.declare(Fact(FA=temp))
        if GN == 'одному':
            if RBRM == 'я обожаю бекон!!!':
                if CHP == 'да':
                    print("Ты станешь отличным пастафарианцем, мой друг.")
                if CHP == 'фу, паста':
                    temp = input("Ты раздражаешь людей? (да, нет) ").lower()
                    while temp != 'да' and temp != 'нет':
                        print("Я не понимаю. Ответь еще раз, пожалуйста.")
                        temp = input("Ты раздражаешь людей? (да, нет) ").lower()
                    self.declare(Fact(FA=temp))
            if RBRM == 'ну...':
                if CHP == 'ну...':
                    print("Стань иудеем.")
                if CHP == 'я обожаю хумус!!!':
                    print("Стань мусульманином.")

    @Rule(Fact(action='linen_healing'),  # LH
          Fact(GN=MATCH.GN),
          Fact(RBRM=MATCH.RBRM),
          Fact(CHP=MATCH.CHP),
          Fact(FA=MATCH.FA),
          NOT(Fact(LH=W())))
    def lh(self, GN, RBRM, CHP, FA):
        if GN == 'множеству' and RBRM == 'да':
            if CHP == 'нет':
                if FA == 'индийскую':
                    print("Хинди - твоё всё.")
                if FA == 'китайскую':
                    print("Тебя ждет буддизм.")
        if GN == 'одному':
            if RBRM == 'я обожаю бекон!!!':
                if CHP == 'фу, паста':
                    if FA == 'да':
                        temp = input("Считаешь ли ты, что белье может исцелять? (да, нет) ").lower()
                        while temp != 'да' and temp != 'нет':
                            print("Я не понимаю. Ответь еще раз, пожалуйста.")
                            temp = input("Считаешь ли ты, что белье может исцелять? (да, нет) ").lower()
                        self.declare(Fact(LH=temp))
                    if FA == 'нет':
                        print("Можешь быть обычным скучным христианином.")

    @Rule(Fact(action='last_q'),  # LQ
          Fact(GN=MATCH.GN),
          Fact(RBRM=MATCH.RBRM),
          Fact(CHP=MATCH.CHP),
          Fact(FA=MATCH.FA),
          Fact(LH=MATCH.LH),
          NOT(Fact(LQ=W())))
    def lq(self, GN, RBRM, CHP, FA, LH):
        if GN == 'одному':
            if RBRM == 'я обожаю бекон!!!':
                if CHP == 'фу, паста':
                    if FA == 'да':
                        if LH == 'да':
                            print("Будь мормоном.")
                        if LH == 'нет':
                            print("Стань Свидетелем Иеговы.")


agree = input('Здравствуй, мой дорогой и не определившийся, к какой же религии примкнуть, друг!\nЯ помогу тебе в этом! '
              '\nПожалуйста, отвечай на вопросы при помощи вариантов ответа, данных при вопросе, \nиначе я не смогу '
              'понять тебя. Приступим? (да, нет) ').lower()
if agree == 'да':
    engine = Religion()
    engine.reset()
    engine.run()
else:
    print('Тогда хорошего дня тебе ^_^')
