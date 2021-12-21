from enum import Enum

# NOTICE : CUSTOMIZE


class IssueStatus(str, Enum):
    TODO = "TODO"
    INPROGRESS = "INPROGRESS"
    INREVIEW = "INREVIEW"
    DONE = "DONE"
