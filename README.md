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
User: EMAIL_ADDRESS
Token: TOKEN 
saveed!! 🌮

> jiral create issue --project="OD" --summary="Separate issue board"
[OD-497] created!! 🌮


> jiral issue --project="OD" --limit=3
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ KEY      ┃ SUMMARY                                      ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ OD-462   │ deploy github actions                        │
│ OD-461   │ set env var                                  │
│ OD-459   │ bugfix wrong parameters                      │
└──────────┴──────────────────────────────────────────────┘
```
