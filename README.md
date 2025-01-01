# Private read and watch list on Data Landscape (ETL-tools, concepts, etc)

Hello everyone! My name is Kirill, [I'm a data engineer](https://www.linkedin.com/in/smirnovkirilll/), and this is my reading list on some data engineering topics. I will be glad if this list is useful or at least interesting for you.


&nbsp;
## Whola lot of disclaimers


&nbsp;
### What is it?
- personal TODO-list (articles, videos, courses, books), which is supposed to help to organize learning path in Data Engineering (DE) stuff. it is divided on topics and I believe it can help to achieve strong versatile knowledge on building of Data Warehouses
- this list can also be used to form an opinion about my area of interest if you would like to collaborate in any way. hope it'll help you to save efforts to know that I'm not good enough at some specific area you need or vice versa - I know something useful for you
- in a very limited sense it maybe can help you to know more about Data Engineering itself. limitations arise from first two points: it is not general-purpose list at all, it reflects only my experience and interests (next section tells more on it)
- if you are supposed to be a member of my team (time to time I do hire too) here are some topics that could possibly be discussed during final sections of hiring process
- the main topic of this post - Data Engineering, but as it does not exist in vacuum and often accompanied with other tasks, I'm also interested in related crafts, like: DevOps, MLOps, BI, Data Analysis, Data Modeling. For now these themes included sporadically, but as DE profession widening in time and absorbing more and more (and more often become Analytics Engineering), useful to know at least where you should watch
- as it is a TODO-list, it gonna be actualised, new items to be added, those which have no sense anymore to be removed/deprecated, and so on


&nbsp;
### What it is not?
- this post can't answer properly to the question "how do i become a Data Engineer?", the reader should already know it. but i've made small section on this topic as a reminder on where to start search of proper answers
- it can't, doesn't intent and would not illuminate all the tools/technics and methods of Data Landscape. according to the [MAD map](https://mad.firstmark.com) there are more than 2000 tools (ML, AI & Data) and counting. no one knows it all, absolutely no sense to require that knowledge from candidate you speaking to (much more reasonable to ask methodics of data processing and tasks ever solved). that's why this post aimed to observe some tools (tiny part of the spectrum), which are industry standard or close to or has perspectives to become or just reflects my personal preferences
- it is not objective, as I have preferences and biases: [Big Data](https://en.wikipedia.org/wiki/Big_data) and [Yandex](https://yandex.com/company) technological stack. if needed to adjust to some specific techno-stack, [by-company map](https://www.moderndatastack.xyz/stacks) could be useful to choose proper tools
- it is not objective, as I am natively speaking russian, most of materials are in Russian (other in English)

> [!NOTE]
> in short: this list is private in many ways, reconsider reasons why you are still reading this


&nbsp;
### Few words for entry-level engineers
**one should already know a lot of stuff to pretend to be a junior engineer, e.g.:**
- algorithms (entry level) - [Алгоритмы и структуры данных (Сергей Бабичев)](https://www.youtube.com/playlist?list=PLrCZzMib1e9pDxHYzmEzMmnMMUK-dz0_7)
- linux shell - [Effective Shell (Dave Kerr)](https://effective-shell.com)
- python (entry level) - [Python (Сергей Лебедев)](https://youtube.com/playlist?list=PLlb7e2G7aSpTTNp7HBYzCBByaE1h54ruW)
- SQL - [SQL Cookbook (Anthony Molinaro)](https://www.amazon.com/SQL-Cookbook-Solutions-Techniques-Developers/dp/0596009763)
- any popular RDBMS (Postgresql, Mysql, Oracle,..)
- dataframes juggling (e.g. pandas)

**next level engineer will have to know elsemore:**
- [Intro to Database Systems (CMU)](https://www.youtube.com/playlist?list=PLSE8ODhjZXjbj8BMuIrRcacnQh20hmY9g)
- [Advanced Database Systems (CMU)](https://www.youtube.com/playlist?list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ)
- [Designing Data-Intensive Applications (Martin Kleppmann)](https://www.amazon.com/Designing-Data-Intensive-Applications-Reliable-Maintainable/dp/1449373321)
- [Методы и системы обработки больших данных (Иван Пузыревский)](https://www.youtube.com/playlist?list=PL-_cKNuVAYAVJJRItmIfqft4HtAmaNgB4)
- one also should [understand expectations](https://gopractice.ru/skills/data_analysts_levels) for engineers of different grades (article is about analysts, but it's so good and can easily be projected on engineers, so I can strongly recommend it)
  - little bit more on levels:
    - [brief review](https://www.levels.fyi/blog/swe-level-framework.html) on software engineer levels (by levels.fyi)
    - [unnecessarily detailed](https://github.com/avito-tech/playbook/blob/master/developer-profile.md) set of developers profiles. as for me, this is more corporate nonsense than helping someone progress. but if ignore that part on performance review, it still could be useful for self-development (by avito)

**everything you will find later in this post is much more specific and much less fundamental**, so this is a basics. if you don't see why chapter of Kleppmann's book dedicated to partitioning is pretty controversial, maybe you have read it too early (hint: partitioning vs distribution).

> [!NOTE]
> you can find more information on concepts and tools of Data Engineering on [wiki article](https://dataengineering.wiki/Tools/Tools), written and curated by Reddit enthusiasts ([DE subreddit & community](https://www.reddit.com/r/dataengineering/)) or [data engineer handbook by Zach Wilson](https://github.com/DataExpert-io/data-engineer-handbook).


&nbsp;
## Engineering stuff itself


&nbsp;
### Complex courses & tutorials
- [Инженер облачных сервисов - Practicum](https://practicum.yandex.ru/profile/ycloud)
- [Построение корпоративной аналитической платформы - Practicum](https://yandex.cloud/ru/training/corpplatform)
- [Витрина данных для веб‑аналитики в ClickHouse - Practicum](https://yandex.cloud/ru/training/datamart)
- [Data Engineering - Zoomcamp](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
  - [additional materials](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform)
- [MLOps - Zoomcamp](https://www.youtube.com/watch?v=o34Q_61iA4Y&list=PL3MmuxUbc_hKqamJqQ7Ew8HxptJYnXqQM&pp=iAQB)


&nbsp;
### DevOps, Infrastructure, Security
- [Packer](https://developer.hashicorp.com/packer/docs)
- [Terraform](https://developer.hashicorp.com/terraform)
  - [IaC: Terraform - Practicum](https://yandex.cloud/ru/training/terraform)
  - [Importing Existing Infrastructure Into Terraform – Step by Step](https://spacelift.io/blog/importing-exisiting-infrastructure-into-terraform)
- [Docker](https://docs.docker.com/)
  - [Контейнеризация с Docker - Practicum](https://yandex.cloud/ru/training/docker)
  - [Как оптимизировать размер контейнерного образа в Docker](https://habr.com/ru/companies/piter/articles/839874/)
  - [Основы Docker. Большой практический выпуск - YouTube](https://www.youtube.com/watch?v=QF4ZF857m44)
- [Kubernetes](https://kubernetes.io/docs/home/)
  - [Kubernetes для разработчиков | Илья Бочаров - YouTube](https://www.youtube.com/watch?v=9ZxZ9gb9pQs)
  - [Kubernetes®. Managed на все 100% - YouTube](https://www.youtube.com/watch?v=M4tX5ixdDf0)
  - [Практикум Kubernetes в Yandex.Cloud - YouTube](https://www.youtube.com/watch?v=jWttCo73rTQ)
- [Шифрование данных и управление ключами - Practicum](https://yandex.cloud/ru/training/encrypt)
- [Как работает сеть в Облаке - YouTube](https://www.youtube.com/watch?v=g3cZ0o50qH0)
- [Деплоим Yandex Cloud с помощью Terraform и GitLab - YouTube](https://www.youtube.com/watch?v=U58zSIvgyDI)


&nbsp;
### Cloud Platforms
- Snowflake (DE-oriented)
  - [What is Snowflake? 8 Minute Demo - YouTube](https://www.youtube.com/watch?v=9PBvVeCQi0w)
  - [Snowflake Vs Databricks - A Race To Build THE Cloud Data Platform - YouTube](https://www.youtube.com/watch?v=VLtq0eeHc14)
- DataBricks (DA-oriented)
  - [Евгений Ермаков, Леонид Кожинов - Сказ про то, как Toloka Ai мигрировала на Modern Data Stack - YouTube](https://www.youtube.com/watch?v=EjvTVutGaGM)
- BigQuery (GCP)
- RedShift (Amazon)
- Yandex Cloud
  - [Возможности Yandex.Cloud - YouTube](https://www.youtube.com/watch?v=wjAjGMtx9zI)
  - [Как начать работу в Yandex Cloud: пошаговая инструкция для новичков - YouTube](https://www.youtube.com/watch?v=u9PI_VncAd4)
  - [Как настроить сквозную аналитику в Yandex Cloud: возможности и практический опыт - YouTube](https://www.youtube.com/watch?v=DgyMCpnmEAw)
  - [Аналитическая платформа для бизнеса - YouTube](https://www.youtube.com/watch?v=CdmFxw4j_dI)
  - [Архитектуры обработки больших данных - YouTube](https://www.youtube.com/watch?v=FHUnirudntU)
  - [Возможности легковесных кластеров Apache Spark в Yandex Data Proc - YouTube](https://www.youtube.com/watch?v=-H2kWnNMZto)
  - [Обработка данных на Apache Airflow в Yandex Cloud - YouTube](https://www.youtube.com/watch?v=jF3YemOVofQ)
  - [Yandex MetaData Hub: как управлять метаданными в облаке - YouTube](https://www.youtube.com/watch?v=Riouu4szE5g)
- [Data Apps: Data warehouse as a Platform | Hightouch - YouTube](https://www.youtube.com/watch?v=PEFP5fLx1dY)


&nbsp;
### Serverless
- [Yandex Database Serverless: публичный запуск - Андрей Фомичев - YouTube](https://www.youtube.com/watch?v=o0-IpbkQKjc)
- [Запускаем контейнерные приложения в Yandex Serverless Containers - YouTube](https://www.youtube.com/watch?v=OVFAjzGDU5w)
- [Собираем и анализируем статистику Telegram-чатов с Serverless и DataLens - YouTube](https://www.youtube.com/watch?v=IhfHNGVqTxI)


&nbsp;
### Data Modeling
- [How To Data Model – Real Life Examples Of How Companies Model Their Data](https://www.theseattledataguy.com/how-to-data-model-real-life-examples-of-how-companies-model-their-data)
- [Data Modeling - Why Data Engineers Need To Understand It - An Introduction To Data Engineering - YouTube](https://www.youtube.com/watch?v=nof9jYIhv54)
- [Modern Data Modeling Beyond The Theory - With Veronika Durgin - YouTube](https://www.youtube.com/watch?v=3P3wMCYTQJc)
- [Data Modeling - Walking Through How To Data Model As A Data Engineer - Dimensional Modeling 101 - YouTube](https://www.youtube.com/watch?v=gG7upg6QaBI)
- [What is Data Vault? - Understanding Data Vault 2.0 by the inventor himself, Dan Linstedt - YouTube](https://www.youtube.com/watch?v=y7faBrUcb74)
- [Как с помощью Data Mesh разломать ваше DWH - Евгений Ермаков, Яндекс GO - YouTube](https://www.youtube.com/watch?v=XCnHS_lXHAA)
- [Ольга Титова - Слабоумие и отвага. Как мы за два месяца объединили данные Delivery Club и Яндекс Еды - YouTube](https://www.youtube.com/watch?v=m4qOlVxTfxA)
- [SQL HowTo: разные варианты работы с EAV](https://habr.com/ru/companies/tensor/articles/657895/)


&nbsp;
### Important Algorithms
- [MapReduce - An Introduction to Distributed Computing for Beginners](https://medium.com/@mmoshikoo/mapreduce-an-introduction-to-distributed-computing-for-beginners-1f718a7bf546)
- [MapReduce - The Scalable Distributed Data Processing Solution](https://tcpp.cs.gsu.edu/curriculum/?q=system/files/ch07.pdf)
- [MapReduce Patterns, Algorithms, and Use Cases](https://highlyscalable.wordpress.com/2012/02/01/MapReduce-patterns/)
- [How do nested loop, hash, and merge joins work? Databases for Developers Performance #7 - YouTube](https://www.youtube.com/watch?v=pJWCwfv983Q)
- [B-Tree индекс и его производные в PostgreSQL](https://habr.com/ru/companies/quadcode/articles/696498/)
- [Introducing LSM trees](https://mahesh-sv.medium.com/introducing-lsm-trees-chapter-3-designing-data-intensive-applications-5bf03fe7bbee)
- [B-Tree vs LSM-Tree](https://tikv.org/deep-dive/key-value-engine/b-tree-vs-lsm/)


&nbsp;
### Storage
- [Avro, Parquet, and ORC File Format Comparison](https://medium.com/@ganeshnv0/avro-parquet-and-orc-file-format-comparison-ff776d375c7e)
- [Comparing Performance of Big Data File Formats: A Practical Guide](https://towardsdatascience.com/comparing-performance-of-big-data-file-formats-a-practical-guide-ef366561b7d2)
- [Data Lake Fundamentals, Apache Iceberg and Parquet in 60 minutes on DataExpert.io - YouTube](https://www.youtube.com/watch?v=hFFP2OYFlTA)
- [Iceberg format: a short introduction](https://medium.com/@cesar.cordoba/iceberg-format-a-short-introduction-6cca39e48ac)
- [YTsaurus: опыт эксплуатации хранилища из 180К дисков / Павел Сушин (Яндекс) - YouTube](https://www.youtube.com/watch?v=R-4veDB2-SA)
- [Внутри S3 - YouTube](https://www.youtube.com/watch?v=NElTqVWM8WQ)
- [Практические советы: как не нужно работать с S3-хранилищем - YouTube](https://www.youtube.com/watch?v=nBYQqLUyYXo)
- [Частичная модификация объектов в Yandex Object Storage: как мы улучшаем работу ФС / Александр Снопов - YouTube](https://www.youtube.com/watch?v=V53lsVO31XQ)


&nbsp;
### Data Bases
- [YTsaurus](https://ytsaurus.tech/docs/en/)
  - https://www.youtube.com/@ytsaurus
  - [YTsaurus - это будущее DWH, и в Яндекс Маркете оно наступило / Филипп Козьмин (Яндекс Маркет) - YouTube](https://www.youtube.com/watch?v=y1Jqm8ObcZ4)
- [Clickhouse](https://clickhouse.com/docs)
  - [Managed Service for ClickHouse - Practicum](https://yandex.cloud/ru/training/clickhouse)
  - [004. ClickHouse как сделать самую быструю распределённую аналитическую СУБД - Виктор Тарнавский - YouTube](https://www.youtube.com/watch?v=Ho4_dQk7dAg)
  - [005. Как работает ClickHouse, лекция в ШАД - YouTube](https://www.youtube.com/watch?v=vbhSrZxm66E)
  - [Вредные советы ClickHouse - YouTube](https://www.youtube.com/watch?v=UR0rmA_-KfA)
- [YDB](https://ydb.tech/docs/en/) TBD


&nbsp;
### Ingestion
- CDC
  - [Change Data Capture (CDC) в Yandex Data Transfer: гид по технологии с примерами](https://habr.com/ru/companies/yandex_cloud_and_infra/articles/754802/)
  - [Change Data Capture (CDC) Done Correctly - Best Practices for Implementing Change Data Capture](https://estuary.dev/cdc-done-correctly/)
- Debezium (CDC) TBD
- Airbyte (seems better solution) TBD
- Yandex DataTransfer (less connectors than Airbyte) TBD
  - [Тимофей Брунько - CDC. От баззворда к реализации в Data Transfer - YouTube](https://www.youtube.com/watch?v=-1yuwfe7b6I)
- Fivetran (pricy stuff aimed to simpler usage) TBD
- [Как устроен PXF Greenplum: архитектура и принципы работы](https://bigdataschool.ru/blog/pxf-greenplum-architecture.html)
- [Сценарии применения Greenplum PXF для интеграции с Data Lake, OLTP, Clickhouse](https://habr.com/ru/companies/otus/articles/682990/)
- [Key Concepts of a Schema Registry](https://developer.confluent.io/courses/schema-registry/key-concepts/)


&nbsp;
### Reverse ETL
> [!NOTE]
> IMHO, it's a pretty strange idea to have a separate tool to do the same thing as the ingest applications, but in the opposite direction. seems that it would be pretty straightforward if one of the competitors (Airbyte, Fivetran, whoever) will fill this gap if it really exists

- Census
  - [How to "Reverse ETL" w Census | Census Tutorial - YouTube](https://www.youtube.com/watch?v=XkS7DQFHzbA)
  - [Why reverse ETL? How Census works with your data ecosystem today and beyond - YouTube](https://www.youtube.com/watch?v=FaZ5XstOaXA)
- Hightouch TBD


&nbsp;
### Streaming
- Kafka
  - [Kafka Tutorial](https://www.redpanda.com/guides/kafka-tutorial)
  - [What is Kafka Connect?](https://www.redpanda.com/guides/kafka-tutorial-what-is-kafka-connect)
  - [Денис Ефаров - 100 миллиардов сообщений в Kafka: загрузил и забыл - YouTube](https://www.youtube.com/watch?v=px6Dy9d-m3o)
  - [Даниэл Рачич - Kafka Connect: что за зверь этот ваш Single Message Transform? - YouTube](https://www.youtube.com/watch?v=HVvt_tjPd6E)
- Flink
  - [Exploring Apache Flink & AWS KDA: Realtime data streaming](https://www.capitalone.com/tech/cloud/aws-apache-flink/)
  - [Apache Spark Vs Apache Flink – Looking Through How Different Companies Approach Spark And Flink - YouTube](https://www.youtube.com/watch?v=6ldUZ4iHxI8)
  - [Валентина Предтеченская - Apache Flink под капотом: distributed, stateful, realtime - YouTube](https://www.youtube.com/watch?v=N0VIhpUf4qM)
- Yandex DataStreams
  - [Стриминг данных с Yandex Data Streams: больше, чем Kafka - YouTube](https://www.youtube.com/watch?v=2xxoFp9vX1g)
  - [Yandex Data Streams: шина данных с поддержкой транзакций и Kafka API - YouTube](https://www.youtube.com/watch?v=iAXqPEsgj-s)
  - [Анализ потоковых данных с помощью Yandex Query - интерактивного сервиса виртуализации данных в YDB - YouTube](https://www.youtube.com/watch?v=PW7v57ELCfQ)
- [Евгений Ненахов - Spark Streaming: брать или не брать? - YouTube](https://www.youtube.com/watch?v=rPzgQsJoMOI)
- [Конвертируй это - с Yandex Message Queue - YouTube](https://www.youtube.com/watch?v=uyIMvEtr3cI)


&nbsp;
### Transformation
- [Dbt](https://docs.getdbt.com/)
  - [Что такое dbt и зачем он нужен маркетинг-аналитику / Хабр](https://habr.com/ru/articles/552542/)
  - [Введение в dbt шаг за шагом / Хабр](https://habr.com/ru/articles/670062/)
  - [DataVault на Greenplum с помощью DBT / Хабр](https://habr.com/ru/articles/671836/)
  - [Простая документация с dbt: Упрощение документирования хранилищ данных / Хабр](https://habr.com/ru/articles/821503/)
  - [Евгений Ермаков - dbt - ядро современной платформы данных - YouTube](https://www.youtube.com/watch?v=u8LkCBVKKus)
  - [Марк Порошин - Data Vault на Greenplum c помощью DBT - YouTube](https://www.youtube.com/watch?v=i1Bq2CRp8WE)
  - [Виталий Бодренков - Визуализация для ELT-процессов в DWH - YouTube](https://www.youtube.com/watch?v=AiOBkOqiSDw)
  - [Airflow with DBT tutorial - The best way! - YouTube](https://www.youtube.com/watch?v=MhCuxTDlVkE)
  - [How to implement unit testing in dbt | Automated test framework in dbt - YouTube](https://www.youtube.com/watch?v=z0uOTgi1S_A)
  - [Building data pipelines with Airbyte and dbt - Webinar | WalkingTree Technologies - YouTube](https://www.youtube.com/watch?v=d-POqk_kKwU)
- [Spark](https://spark.apache.org/docs/latest/) TBD
  - [PySpark Tutorial for Beginners - YouTube](https://www.youtube.com/watch?v=EB8lfdxpirM)
  - [Валерия Дымбицкая - Автоматический тюнинг Spark-приложений - YouTube](https://www.youtube.com/watch?v=-VRQbCXmYOk)
- Trino (spark-like) TBD


&nbsp;
### Orchestration
- [Airflow](https://airflow.apache.org/docs/) TBD
- [Prefect](https://docs.prefect.io) (seems it fits better for Data Analysts, not gonna use it)
  - [Юлия Волкова - Любовь и ненависть к Prefect 2.0 после Apache Airflow - YouTube](https://www.youtube.com/watch?v=L16MkFWoRk4)


&nbsp;
### BI
- [DataLens](https://yandex.cloud/en/docs/datalens/) TBD
- [Getting Started w Metabase | Open Source Data Visualization Tool - YouTube](https://www.youtube.com/watch?v=yrrLxpz9J8c)


&nbsp;
### ML
- [ML‑сервисы: ключевые решения - Practicum](https://yandex.cloud/ru/training/ml-solutions)
- [Основы работы с Yandex SpeechSense - Practicum](https://yandex.cloud/ru/training/speechsense)
- [Yandexgpt](https://yandex.cloud/en/services/yandexgpt)
- [Математическая оптимизация для бизнеса в Yandex DataSphere - YouTube](https://www.youtube.com/watch?v=fOzDMNAGQXw)
- [MLOps в DataSphere на примере SpeechKit - YouTube](https://www.youtube.com/watch?v=Sd97ed_BBF8)


&nbsp;
### Documentation, Lineage, Observability, DQ
- [OpenLineage](https://openlineage.io/docs) TBD
- Great Expectations TBD
- Elementary (+dbt) TBD


&nbsp;
### Random Topics
- [What tools should you know as a Data Engineer? - YouTube](https://www.youtube.com/watch?v=UDmViyjdHuw)
- [What Tools Should Data Engineers Know In 2024 - 100 Days Of Data Engineering - YouTube](https://www.youtube.com/watch?v=nB7Lo9pGzVk)
- [DataFrame - настоящее и будущее - YouTube](https://www.youtube.com/watch?v=HAT2soEWex4)
- [How to Do Data Exploration (step-by-step tutorial on real-life dataset) - YouTube](https://www.youtube.com/watch?v=OY4eQrekQvs)
- [Introduction to data cleaning with OpenRefine & word clouds - YouTube](https://www.youtube.com/watch?v=KLuDe38muQI)


&nbsp;
### Open Data Sets
- https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research
- https://datasetsearch.research.google.com
- https://toloka.ai/datasets
- https://www.yelp.com/dataset/download
- https://github.com/owid/owid-datasets
- https://www.reddit.com/r/datasets/


&nbsp;
## Contact me
I do already have a permanent job, but if you believe I can help with your project, feel free to contact me on [Linkedin](https://www.linkedin.com/in/smirnovkirilll). At the very least, perhaps I could recommend another DWH specialist I have worked with and who might be able to help you.
