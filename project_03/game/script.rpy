# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sn = Character('sniper', color="#FF4500")
define pl = Character('phantom lancer', color="#C5D0E6")
define am = Character('antimage', color="#00FF00")
define pa = Character('phantom assassin', color="#FFFF00")

default point = 0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene first 
    play music red

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sniper at left

    sn "сегодня я вам покажу сценку"

    show sniper at right:
        xalign 0.0
        linear 0.7 xalign 0.9
    
    sn "на тему: как сказать <<нет>>"

    scene scene_1 with dissolve
    show phantom_lancer at right with dissolve

    #   sn "" sniper
    #   pl "" phantom_lancer

    #СЦЕНА 1

    show phantom_lancer at right
    pl "Срочно нужна аналитика по новому проекту! К утру"

    show sniper at left
    sn "Мой отчет сдан. Я ухожу"

    menu:

        "как ответить?"

        "Жестко":
            sn "Нет. Не в моих обязанностях"
            $ point += 1
            
        "Мягко":
            sn "Сожалею, но не смогу"
            

    #СЦЕНА 2
  
    stop music
    play sound mus_1 noloop
    $ renpy.pause(3.0)
    play music red

    scene scene_2 with dissolve
    show phantom_lancer at left with dissolve

    pl "Команда на меня рассчитывает! Без цифр — провал."

    show sniper at right
    menu:

        "Обвинить":
            sn "Твоя ошибка в планировании"
            
        "Уйти":
            sn "Собрать вещи и молча выйти"
            $ point += 1

    hide phantom_lancer
    hide sniper
    "sniper уходит"

    #СЦЕНА 3

    scene scene_3 with dissolve
    show antimage at left with dissolve

    show sniper at right

    am "Лансер провалил презентацию. Почему не помог?"

    menu:

        "Взять вину":
            sn "Мог помочь, но не стал. Моя ошибка"
            
        "Отстоять позицию":
            sn "Он неверно распланировал задачи. Я был занят своей работой"
            $ point += 1

    #СЦЕНА 4

    scene scene_4 with dissolve
    show phantom_lancer at right with dissolve

    pl "(Настойчиво) Новые данные. Нужна твоя помощь. Сейчас"

    show sniper at left

    menu:

        "Извиниться":
            sn "Извини. Не в этот раз"
            $ point += 1
            
        "Условия":
            sn "Только если всё по регламенту. Письменный запрос"
            $ point += 2

    #СЦЕНА 5

    stop music
    play sound mus_2 noloop
    $ renpy.pause(3.0)
    play music red

    scene scene_5 with dissolve

    "Коллега шепчет Снайперу"
    
    show sniper at left with dissolve
    show phantom_assassin at right with dissolve

    pa "Все говорят, что ты подвел Лансера"
    pa "Боитсясь просить о помощи"

    menu:

        "Игнорировать":
            sn "Продолжать работать, не реагируя на сплетни"
            
        "Объяснить":
            sn "Я не подводил. Есть регламент для все"
            $ point += 1

    #СЦЕНА 6

    stop music
    play sound mus_3 noloop
    $ renpy.pause(3.0)
    play music red

    scene scene_6 with dissolve

    "Начальник вызывает Снайпера"

    show antimage at left with dissolve
    show sniper at right with dissolve

    am "Лансер снова сорвал сроки. Но твой отчет был идеальным"

    menu:

        "Предложить уволить Лансера":
            sn "Его непрофессионализм вредит всем"
            $ point += 1
            
        "Предложить научить":
            sn "Могу провести для него инструктаж по планированию"

    #СЦЕНА 7

    stop music 
    play music green

    scene scene_7 with dissolve

    "Лансер сталкивается со Снайпером у кофемашины"
    "Напряжение достигло пика"

    show phantom_lancer at right with dissolve
    show sniper at left with dissolve

    pl "Доволен? Тебя хвалят, а на меня жалуются"

    menu:

        "Холодно":
            sn "Ты сам сделал этот выбор"
            $ point += 3
         
            
        "Сдержанно":
            sn "Давай обсудим, как работать дальше"
            


    #
    #=======================================================================
    if point >= 6:
        jump one_last
    else:
        jump two_last
    #=======================================================================
    #

    #КОНЦОВКА 1

label one_last:

    scene black

    show text "Лансера увольняют. Снайпер получает повышение, но команда боится его" with dissolve

    $ renpy.pause(4.0)

    show text "Границы, построенные на страхе, становятся клеткой" with dissolve

    $ renpy.pause(4.0)

    jump last_path
    
    #КОНЦОВКА 2

label two_last:

    scene black

    show text "Лансер начинает работать по правилам. Их следующий проект становится успешным" with dissolve

    $ renpy.pause(4.0)

    show text "Сильное «нет» может стать началом уважения" with dissolve

    $ renpy.pause(4.0)

    jump last_path

    #ИТОГ

label last_path:
    scene second with dissolve
    show sniper at right with dissolve

    sn 'Правильное «нет» защищает ваше время'
    sn 'сохраняет уважение и строит здоровые границы, а не рушит отношения'
    show sniper at right:
        xalign 0.0
        linear 0.5 xalign 0.1
    sn 'конец'

    # These display lines of dialogue.

    # This ends the game.

    return
