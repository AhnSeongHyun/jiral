jiral
======

![CI](https://github.com/AhnSeongHyun/jiral/workflows/CI/badge.svg)


### Install 

```shell script
> pip3 install -r requirements.txt
> python3 setup.py install
```

### Usages

```shell script

> jiral config 
Server: https://YOUR-COMPANY.atlassian.net
User: EMIAL_ADDRESS
Token: TOKEN 

> jiral issue --project="OD" --limit=3
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ KEY      ┃ SUMMARY                                      ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ OD-462   │ deploy github actions                        │
│ OD-461   │ set env var                                  │
│ OD-459   │ bugfix wrong parameters                      │
└──────────┴──────────────────────────────────────────────┘
```
