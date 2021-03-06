
**************************
Электронный проектный офис
**************************

Как в среде программной разработки, так и в бизнесе к проектам сегодня сложилось неоднозначное отношение. С одной стороны все понимают, что любую деятельность надо планировать. И для планирования наработаны подходы сетевых графиков работ, схем бизнес-процессов и целых бизнес-планов с финансово-инвестиционными параметрами.

Но, "отплывая от берега", часто оказывается ситуация, которую хорошо описали в пословице "гладко было на бумаге, да забыли про овраги". Среди кучи проектных документов тяжело бывает найти нужную директиву, особенно если ее там нет, и появилась потребность в ней уже в процессе работы.

Программисты научились бороться с недостаточностью постановочной информации с помощью трекинговых систем для ослеживания задач. Через обратную связь в электронных задачах программисты "сигналят" о проблемах. Но и там больше чем на недельный спринт видения картины движения по проекту нет.

Сочетание подхода трекинговых систем и электронной документации может дать интересный результат. В начале проекта в документацию можно разместить исходные данные - технические задания, проектные документы, предполагаемые графики работ. А вот уже графики работ можно связать с электронными задачами, в которых уже будет происходить взаимодействие участников проекта с попутным дополнением документации в части постановки задач, хода выполнения графиков работ.

GitHub сервер
=============

Для ведения документации идеальным форматом является текстовый файл с разметкой заголовков, стилей, таблиц, сносок, ссылок. Популярной системой документирования с поддержкой размеченного текста сегодня является Sphinx (подробнее можно посмотреть в разделе :doc:`/ideas/sphinx/sphinx`). Sphinx позволяет создавать автономный веб-сайт документации с автоматически сформированной навигацией и поиском без каких-либо серверов.

Версионную коллективную работу с документами текстовых форматов удобно вести в Git серверах, как на собственном сервере через GitLab, так и на интернет хостинге GitHub или BitBucket. Разберем сервер GitHub (https://github.com). Git позволяет всем участникам проекта в автоматизированном режиме делать версионные копии документации, вносить изменения и объединять их с изменениями других участников, сохраняя всю историю изменений. На GitHub можно бесплатно размещать проекты с открытым кодом, или выбрать тариф для ведения закрытых проектов с ограниченным доступом.

Проекты и электронные задачи
============================

Основным проектом в GitHub является репозиторий, вокруг которого формируется проектная среда из следующих составляющих:

:Репозиторий - раздел Code:
    - папки с файлами для версионной коллективной работы через ветки рабочих копий

:Задачи - раздел Issues:
    - список задач с поддержкой атрибутов: название и описание задачи, назначенные ответственные пользователи, привязанные теги, этапы и проектные процессы
    - список тегов (Labels) для сортировки задач по ситуациям их возникновения
    - список этапов (Milestones) для отслеживания работ и сроков по участкам проекта

:Проектные процессы - раздел Projects:
    - список процессов для фиксации сопутствующих основному проекту активностей, недельных спринтов в методике Agile, процессов обслуживания клиентов

.. figure:: /_static/github1.gif
    :align: center

    Пример создания электронных задач на GitHub.

Возможность коллективного раздельного управления в разных разделах проекта создает упорядоченную среду и эффективнную замену беспорядочному почтовому сообщению.

Для общения в стиле чата GitHub предлагает интегрированный сервис Slack (https://slack.com), аналогичный чат для собственного сервера на GitLab - Mattermost (https://mattermost.com). Оба чата предлагают мобильные приложения в AppStore и Google Play.

Создание копии через ветвление
==============================

Главный процесс работы с документацией сотоит из создания пользователем рабочей копии в так называемой ветке (branch), внесения изменения в текст документов, фиксации изменений (commit), слияния своей ветки с основной веткой репозитория и генерации веб-сайта документации.

Рабочая копия в GitHub формируется через активацию списка веток branch в разделе репозитория (название раздела Code). Список веток показывает активную ветку. При открытии списка появляется поле ввода названия ветки для поиска и одновременно создания новой ветки при отсутствии ветки с введенныи названием. В процессе ввода будет показана кнопка-подсказка, что можно добавить ветку с введенным названием. По этой кнопке будет создана и установлена активной новая ветка с рабочей копией репозитория.

.. figure:: /_static/github2.gif
    :align: center

    Пример создания собственной ветки, внесения и фикации изменений.

После внесения изменений в текстовые файлы через встроенный редактор необходимо зафиксировать изменения нажатием кнопки Commit, указав комментарий сути изменений.

Слияние копии с основной веткой
===============================

Ссылки на электронные задачи
============================

Чтобы добавить возможность указывать короткие ссылки на внешние адреса с номером задачи, нужно в файл ``conf.py`` добавить директиву ``extlinks = {'gh': ('https://github.com/andrew-bykov/sphinx/issues/%s','# ')}``. Тогда с помощью разметки ``:gh:`1``` можно сгенерировать на сайте документации ссылку ``https://github.com/andrew-bykov/sphinx/issues/1``.

.. todo::
    
    **Раздел - Электронный проектный офис - Запланировано**
    
    .. container:: todo-plan
    
        =========== =================== ========
        №           Дата                Задача
        =========== =================== ========
        **Ответственный - Коля**
        ----------------------------------------
        :gh:`1`     (60ч) ?.04.2020     Создание окружения для электронных задач
        :gh:`2`     (5мин) ?.04.2020    Создание ветки для изменений
        :gh:`3`     (5мин) ?.04.2020    Объединение изменений
        =========== =================== ========

    **Раздел - Электронный проектный офис - Сделано**
    
    .. container:: todo-done
    
        =========== =================== ========
        №           Дата                Задача
        =========== =================== ========
        **Ответственный - Вася**
        ----------------------------------------
        :gh:`1`     (60ч) ?.04.2020     Создание окружения для электронных задач
 
        **Ответственный - Петя**
        ----------------------------------------
        :gh:`2`     (5мин) ?.04.2020    Создание ветки для изменений
        :gh:`3`     (5мин) ?.04.2020    Объединение изменений
        =========== =================== ========
    
Подробнее о формате плановых блоков можно посмореть в разделе :doc:`/plan`.

Организация офиса
=================

В созданный на GitHub электронный офис с автоматизированной генерацией сайта документации Sphinx можно добавлять проектные документы как в начальной стадии проекта, так и в процессе ведения работ.

Благодаря постоянной работе с документацией в проекте будет всегда собранная картина планов и результатов. Интеграция документации и задач в GitHub позволяет соединить плановую работу с электронной средой задач.