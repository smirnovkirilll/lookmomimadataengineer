## Data flow map (read/watch)
Chart representing my way of working with incoming information sources


```mermaid
---
title: 
 (TBD, not implemented fully yet)
---
flowchart LR;
S1((initial<br>read/watch<br>list)) --> |serverless func-1| DB[(db)]
S2((online text<br>source)) --> |save to pocket| S3((pocket)) --> |serverless func-2| DB[(db)]
S4((youtube)) --> |save to playlist| S5((youtube<br>playlist)) --> |serverless func-3| DB[(db)]
S6((reddit)) --> |serverless func-4| DB[(db)]
DB[(db)] --> |local actions*| DB[(db)]
DB[(db)] --> |serverless func-5| T1[pw]
DB[(db)] --> |serverless func-6| T1[public website:<br>- curated list on DE<br>- reddit digest on DE]
DB[(database)] --> |local actions*| T3[private read/watch lists]

click T1 "https://lookmomimadataengineer.website.yandexcloud.net" "public website"
```


notes:
- local actions - all the kinds of actions useful to make tables more consistent, add the necessary tags, read marks, material quality marks, comments, deduplication, etc.
- reddit digest - not published yet, does not involve any human control, should work completely autonomously, scripts are stored here in the same repo and hosted in the cloud
