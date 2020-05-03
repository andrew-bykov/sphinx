
********************
Проектное управление
********************

Разработка программного обеспечения всегда сложный процесс. Управление таким процессом в чем-то схоже с классическим проектным подходом PMBoK (Project Management Body of Knowledge). Конечно есть специфика в неопределенном количестве итераций работ над каким либо участком программы, описанная в методиках Rational Unified Process, Agile, eXtreme programming.

Из практики проектной работы мне видно боольшое разнообразие индивидуальных методик буквально в каждом проекте. Шаблоны почти никогда не работают в общем виде. Постараюсь раскрыть особенности, с которым приходилось мне встречаться.

Microsoft Project
=================

Обычно первым инструментом на пути всех новичков попадает в руки продукт компании Microsoft. Он удобен табличным Excell стилем интерфейса, сразу видна группировка задач и легко назначать ответственных. Интеграция c Microsoft SharePoint сервером позволяет получить заодно удобное хранилище для документов и списков проекта.

Проект "Система проектной реализации заказов"
---------------------------------------------

Заказчик: WhiteSite (2002)

Проведен анализ бизнес процессов производства. Реализована система матричного проектного производства Интернет представительств на базе продукта "Microsoft Project 2000 + Microsoft SQL Server" с возможностью сетевого распределенного планирования проектов на едином пуле ресурсов. Разработаны библиотечный модуль управления мультипроектной структурой и модуль интеграции системы маркетинга продаж с системой реализации заказов.

Управление лабораторией беспроводных систем мониторинга
-------------------------------------------------------

Заказчик: Институт Точной Механики и Вычислительной Техники им. Лебедева

Развернут проектный офис в интеграции с Microsoft Sharepoint Server, организовано более 30 проектов для работы с заказчиками по изготовлению стендов и опытных образцов устройств сенсорной сети на основе радиопротокола ZigBee.

Spider Project
==============

Во время прохождения стажировки в российском отделении PMI в 2002 году у Либерзона Владимира Иосифовича (одного из автором PMBoK) узнал много интересного о методах проектного управления - о критическом пути в сетевых графиках работ, проектных вехах (а не групп задач), иерахиях задач, которых может быть несколько для разных проектных процессов.

Самое главное - пришло понимание необходимости описывать ресурсы проекта, их характеристики в затратах и эффектах. Такие характеристики позволяют легко рассчитывать сложные параметры проекта, строительные сметы. 

Expert Project
==============

Особенно глубоко оценка ресурсов проекта проводится в методиках бизнес планирования, например в UNIDO. Подробное моделирование инвестиционной, оперционной и финансовой деятельности позволяет определить много реперных и ораничительных параметров проекта.

Подготовка венчурного проекта
-----------------------------

Заказчик: Институт Точной Механики и Вычислительной Техники им. Лебедева

Одной из целей работы направления сенсорных сетей было формирование инвестиционного проекта для вывода технологии на рынок. Мною было разраоботаны несколько бизнес-планов в Project Expert для разных применений технологии. По некоторым из них были иницированы венчурные процессы.

Redmine
=======

Некоторые проекты обладают потребностями в учете процессов, что порождает различные топологии систем управления - дивизионной, функциональной или матричной структур подчинения людей и задач. В программировании процесс сопровождения клиентов и исправления багов часто становится типичным процессом, и система Redmine отлично справляется с совмещением задач управления проектами, трекингом задач и таблицами процессов с необходимыми атрибутами. 

Управление группой проектов программной разработки
--------------------------------------------------

Работа над системой электронной коммерции в компании Триумф в период 2009-2014 была связана с поиском продуктового образа и сопровождалась десятками проектов по программной разработке, веб дизайну и трехмерному моделированию.

В системе Redmine удалось формализовать многие поцессы разработки, совместить их с репозиториями программного кода, построить подобие системы требований с трассировками задач и автоматизированную систему отчетности потраченного времени.

Управление юридическим агентством
---------------------------------

Попутная задача для соседнего юридического отдела выявила способности Redmine к организации юридических проектов с определением специфических метрик потраченных часов, проведенных мероприятий и оценки результативности юристов.

GitLab
======

Формальные проектные цифры все же не дают глубокой картины по проекту. На определенной стадии проекту нужно подробное описание и интегрированное взаимодействие участников. 

Тенденцию в программных проектах по уменьшению формальности, упрощению заведения задач и возможности проще описывать ситуации с задачами задал сервис GitHub с чатом Slack. Офисным аналогом GitHub стал GitLab и чат Mattermost.

Управление разработкой программных продуктов
--------------------------------------------

Работа над системой электронной коммерцией в компании Триумф в период 2015-2020 была связана больше с продуктовой разработкой. В этот период особое внимание уделялось проектному окружению, рабочей документацией, разработке конкуретноспособной системы требований, отладке архитектуры и функциональности программных продуктов.

Все перечисленные работы были более эффективно организованы в GitLab, Mattermost и Sphinx. Благодаря формату рабочей документации Sphinx удалось максимально сильно интегрировать все участки проекта и объединить программистов с конструкторами, руководством и группой тестирования.

Sphinx
======

Любой сложный проект требует рабочего окружения. По опыту продуктовой разработки желательно, чтобы формат рабочего окружения был близок к документации.

Интересным вариантом создания рабочего окружения было сочетание GitLab хранилища кода, интегрированный с GitLab чат Mattermost и система документирования Sphinx (подробнее см. :doc:`/ideas/sphinx/sphinx`).

Отличительные особенности программы
-----------------------------------

- формирование комплекта автономных веб-страниц с поддержкой поиска и тем оформления
- возможность размещения в качестве сайта на любом файловом хостинге без использования сервера баз данных и сервера веб-приложений (GitHub, BitBucket, GitLab)
- автоматическое создание структуры навигации по группе файлов на основе заголовков
- возможность использовать для работы любой тектовый редактор
- поддержка систем версионного контроля (Git например) для коллективной работы
- использование интуитивного языка разметки reStucturedText с богатым набором директив
- поддержка автодокументации программного кода
- кроссплатформенная работа на разных операционных системах (Windows, Linux, MacOS)

Плюсы для программной разработки
--------------------------------

- документация имеет сквозную структуру из нескольких файлов, что позволяет формировать логически связанную подшивку документов с более легкой навигацией и поиском по сравнению с офисными документами, сложенными в случайные папки
- документацию легко "наращивать" с простого технического задания иллюстрациями прототипированных пользовательских форм, описанем алгоритмов работы и спецификациями программных модулей
- документация может выполнять роль базы знаний по проекту, доступной для всех участников
- в каждом разделе документации можно фиксировать планы работ, замечания, ошибки и формировать сводный раздел по задачам из всех разделов
- для планирования легко выделять новые разделы для недельных и месячных спринтов
- в документацию легко вставлять видеофрагменты и анимированные гифы

Бизнес процессы
---------------

В документацию Sphinx можно размещать html фрагменты с помощью директивы ``.. raw:: html``.

Например можно вставить SVG диаграмму бизнес процессов, созданную предварительно в `Draw.io <https://diagrams.net>`_. SVG файлы можно также вставлять документацию с помощью лиректив ``.. image:: <название файла>`` и ``.. figure:: <название файла>``.

Пример диаграммы MindMap
------------------------

.. raw:: html

    <center>
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="501px" height="421px" viewBox="-0.5 -0.5 501 421" content="<mxfile host=&quot;app.diagrams.net&quot; modified=&quot;2020-05-02T18:29:04.730Z&quot; agent=&quot;5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36&quot; version=&quot;13.0.3&quot; etag=&quot;qKS7XU4cczFLUmH6ajE8&quot; type=&quot;github&quot;><diagram id=&quot;7f8NsTD8YnoAwTJ67WiY&quot;>7Vptc9soEP41/tqxJEt2PsZ2cncz7bQTt9P2I5aIRA+BD+G3/vpbJJCEkV3FcZq0zUwmI5aFhd19HhaSQTDLd38JtMre8QTTgT9MdoNgPvD98SSC30qwrwSj8bASpIIklchrBAvyHWuhUVuTBBeWouScSrKyhTFnDMfSkiEh+NZWu+fUtrpCKXYEixhRV/qZJDKrpBN/3Mj/xiTNjGUvuqp6cmSU9U6KDCV82xIFN4NgJjiX1Ve+m2GqfGf8Uo27PdJbL0xgJvsM8KsBG0TXem8zziQiDAu9QLk3uy62JKeIQWuqR2Eh8e6oZa/eD+QB5jmWYg8qeoA/1C7Ym9jq9rbxaGhkWcubI+M7pKOY1nPX5u4g6oilsPLaXnBoz3ftXXWY8wPbGqISC4YknvI1S4q2d+GjtdNGVPq82/+B63/wn0BK558EIycIMByyXMVgmxGJFysUq54t4AxkmczB0tyDT0RJyuA7hvkgmMGU4e1NAmls5hpDFKP/1irTprjuqEWD4LrVzySR+ztMkSSc3XRo+7OmUUgk5LXC2ZHpGGfHxmKWnDmywGmucq89UBFGSyVeiw1ObI3BeA5fUmB8CzRAWKr9pyTv+KYR9Mp5/2TOB6GVgpGbgV5nxp9IeCv3TiTayEm0qUAszpwE+0FaAWGtVA9sWhJEG6CBxzjozofwRfG91J9LLiXP9WCh96Q6VpwwWW4onMKPCpQ3COcqXuHUM61QBeeeUDrjlEMWz8sE6MhuFRcCDH2tO4zdqeBrCUGclYpflfE3odoHQ6uP/INahFkchvQoyAbf4aI6cdQy0Vpy3fT65ckrzk7g7AIg8sY2ikYuiiZdPH4BEIUOiFx+boX+WDStyNUpXUeklhhPQ14NG6+22UhZO+1GWBxfixhbxw1YT7Ehl25ni3LVG3v2EyduhaQmSAdUNznwfrUoPehRJ2jkxGSxXoLgI1+R+KHsJtSZXvsYiVjXnuGwD+fkJEl0eAX/ty4NPZdGClhBxRijV1J5EaQS2fnqeR1ns9dFK9HjaWX8G9JK9DS04h+EKbwUr3wqsHi//KZui/6QoiWm1YTvRYoY+V66Wu8SsHlXXtBaWzChnLTWrqPcn30cgnlqYqBLvn05fHApLNcVgUmSrjo76MBy9PASAZqtzOmG99VJNHMhM55yhmgbyc1BpCDa6LzlZZGtIv8NS7nX55M6Xuxcwjsiv9TVrmp9bfXMd3rmsrHXDYsJXN4AyS1RG69GwjV1/6XdaIrrstnYKFvGyMUYZtKdBL0Zpi87G9Z3KowFhLxmhUeg/GgZ8XMupVc2pQZhz1vpGWhxfev93r71x8/pXPdx71mY6AdEch4hTFxC8MKfxQjuq92cbEjx3An7Wgu4df3EBmDvN7eLANB9dDsDgP2KehumFSw+wIQzzuA2iqpnLowKucVFGUpdKB9oMLUG6FO+OROZXsdZ7Q27o/TI64Af2pWeP36yZwbPfft5xfzLxHwQPSfm3feoPxXzR/7+9wth/qEPMzaeNMCgwwD8zMiec5e7XFUVPFEYrSgGh8/zZ0cRms2fzyv15n8Qgpv/AQ==</diagram></mxfile>" style="background-color: rgb(255, 255, 255);"><defs></defs><g><path d="M 0 23 L 0 0 L 500 0 L 500 23" fill="#ffffff" stroke="#000000" stroke-miterlimit="10" pointer-events="all"></path><path d="M 0 23 L 0 420 L 500 420 L 500 23" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="none"></path><path d="M 0 23 L 500 23" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="none"></path><g fill="#000000" font-family="Helvetica" font-weight="bold" text-anchor="middle" font-size="12px"><text x="249.5" y="16">Container</text></g><ellipse cx="85" cy="80" rx="50" ry="20" fill="#ffffff" stroke="#000000" pointer-events="none"></ellipse><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 98px; height: 1px; padding-top: 80px; margin-left: 36px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: none; white-space: normal; word-wrap: normal; ">Central Idea</div></div></div></foreignObject><text x="85" y="84" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Central Idea</text></switch></g><path d="M 175 40 M 255 40 M 255 60 L 175 60" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="none"></path><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe flex-end; justify-content: unsafe center; width: 78px; height: 1px; padding-top: 57px; margin-left: 176px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: none; white-space: normal; word-wrap: normal; ">Branch</div></div></div></foreignObject><text x="215" y="57" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Branch</text></switch></g><path d="M 135 80 Q 145 80 155 70 Q 165 60 175 60" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="none"></path><rect x="165" y="110" width="110" height="26" rx="13" ry="13" fill="#ffffff" stroke="#000000" pointer-events="none"></rect><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 104px; height: 1px; padding-top: 123px; margin-left: 168px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: none; white-space: normal; word-wrap: normal; ">Sub Topic</div></div></div></foreignObject><text x="220" y="127" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Sub Topic</text></switch></g><path d="M 135 80 Q 145 80 150 101.5 Q 155 123 165 123" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="none"></path><rect x="240" y="160" width="130" height="60" fill="#ffffff" stroke="#000000" pointer-events="none"></rect><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 128px; height: 1px; padding-top: 190px; margin-left: 241px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: none; white-space: normal; word-wrap: normal; ">Organization</div></div></div></foreignObject><text x="305" y="194" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Organization</text></switch></g><path d="M 85 100 Q 85 190 240 190" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="none"></path><rect x="95" y="350" width="100" height="60" fill="#ffffff" stroke="#000000" pointer-events="none"></rect><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 98px; height: 1px; padding-top: 380px; margin-left: 96px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: none; white-space: normal; word-wrap: normal; ">Sub Section</div></div></div></foreignObject><text x="145" y="384" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Sub Section</text></switch></g><rect x="275" y="350" width="100" height="60" fill="#ffffff" stroke="#000000" pointer-events="none"></rect><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 98px; height: 1px; padding-top: 380px; margin-left: 276px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: none; white-space: normal; word-wrap: normal; ">Sub Section</div></div></div></foreignObject><text x="325" y="384" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Sub Section</text></switch></g><path d="M 305 220 L 305 240 L 415 240 L 415 260" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="none"></path><rect x="185" y="260" width="100" height="60" fill="#ffffff" stroke="#000000" pointer-events="none"></rect><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 98px; height: 1px; padding-top: 290px; margin-left: 186px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: none; white-space: normal; word-wrap: normal; ">Division</div></div></div></foreignObject><text x="235" y="294" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Division</text></switch></g><path d="M 235 320 L 235 380 L 195 380" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="none"></path><rect x="365" y="260" width="100" height="60" fill="#ffffff" stroke="#000000" pointer-events="none"></rect><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 98px; height: 1px; padding-top: 290px; margin-left: 366px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; "><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: #000000; line-height: 1.2; pointer-events: none; white-space: normal; word-wrap: normal; ">Division</div></div></div></foreignObject><text x="415" y="294" fill="#000000" font-family="Helvetica" font-size="12px" text-anchor="middle">Division</text></switch></g><path d="M 235 320 L 235 380 L 275 380" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="none"></path><path d="M 305 220 L 305 240 L 235 240 L 235 260" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="none"></path></g><switch><g requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"></g><a transform="translate(0,-5)" xlink:href="https://desk.draw.io/support/solutions/articles/16000042487" target="_blank"><text text-anchor="middle" font-size="10px" x="50%" y="100%">Viewer does not support full SVG 1.1</text></a></switch></svg>
    </center>

Пример диаграммы Aris
---------------------

.. figure:: /_static/D.svg
    :align: center
