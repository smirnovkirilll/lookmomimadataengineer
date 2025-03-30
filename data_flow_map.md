## Data flow map (read/watch)
Chart representing my way of working with incoming information sources


```mermaid
---
title: 
 (TBD, not implemented fully yet)
---
flowchart LR;
S1((reddit)) --> |serverless func-1| DB[(postgresql)]
S2((online text<br>source)) --> |save to pocket| S3((pocket)) --> |serverless func-2| DB[(postgresql)]
S4((youtube)) --> |save to playlist| S5((youtube<br>playlist)) --> |serverless func-3| DB[(postgresql)]
S6((initial<br>read/watch<br>list in CSV)) --> |serverless func-4| DB[(postgresql)]
DB[(postgresql)] --> |local actions*| DB[(postgresql)]
DB[(postgresql)] --> |serverless func-5| T1[reddit digest on DE]
DB[(postgresql)] --> |serverless func-6| T2[curated list on DE]
DB[(postgresql)] --> |local actions*| T3[other read/watch lists]

click T1 "https://lookmomimadataengineer.website.yandexcloud.net" "reddit digest on DE"
click T2 "https://lookmomimadataengineer.website.yandexcloud.net" "curated list on DE"
```


notes:
- local actions - all the kinds of actions useful to make tables more consistent, add the necessary tags, read marks, material quality marks, comments, deduplication, etc.
- reddit digest - not published yet, does not involve any human control, should work completely autonomously, scripts are stored here in the same repo and hosted in the cloud
