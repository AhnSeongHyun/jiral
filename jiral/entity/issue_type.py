from enum import Enum


class IssueType(str, Enum):
    TASK = "Task"
    Bug = "Bug"
