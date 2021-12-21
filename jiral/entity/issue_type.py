from enum import Enum


class IssueType(str, Enum):
    TASK = "Task"
    BUG = "Bug"
