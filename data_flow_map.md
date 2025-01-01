## Data flow map (read/watch)
Chart representing my way of working with incoming information sources


```mermaid
---
title: 
 (TBD, not implemented fully yet)
---
flowchart LR;
S1((reddit)) --> |serverless func-1| DB[(postgresql)]
S2((some text source)) --> |save to pocket| S3((pocket)) --> |serverless func-2| DB[(postgresql)]
S4((youtube)) --> |save to playlist| S5((youtube playlist)) --> |serverless func-3| DB[(postgresql)]
DB[(postgresql)] --> |local actions*| DB[(postgresql)]
DB[(postgresql)] --> |serverless func-4| T1[reddit digest]
DB[(postgresql)] --> |local script-1*| T2[public readme list on DE]
DB[(postgresql)] --> |local script-2*| T3[private readme list]

click T1 "https://github.com/smirnovkirilll/lookmomimadataengineer/tree/main/reddit_digest" "reddit digest"
click T2 "https://github.com/smirnovkirilll/lookmomimadataengineer/blob/main/README.md" "readme on DE"
```


notes:
- local actions - all the kinds of actions useful to make tables more consistent, add the necessary tags, read marks, material quality marks, comments, deduplication, etc.
- local script-1/2 - as not all of my personal marks should be publicly available, there is some difference, but overall the scripts are quite similar: they both create an md view file on the same set of tables. the public readme is posted here in the repository. since both of views require some manual work, the scripts are applied locally, the cloud backend is not needed
- reddit digest - the project is not published yet (but some of its parts can be found in the same repository), does not involve any human control, should work completely autonomously, so the scripts are hosted in the cloud
