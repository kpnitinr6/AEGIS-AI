"""
AEGIS AI Domain

Decision Policies.
"""

from .majority_vote_policy import MajorityVotePolicy
from .weighted_decision_policy import (
    WeightedDecisionPolicy,
)

__all__ = [
    "MajorityVotePolicy",
    "WeightedDecisionPolicy",
]