jiral
======
> jira with cli

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
saved!! 🌮

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

> jiral update issue --issue-id="OD-461" --status="DONE"              
 
```
