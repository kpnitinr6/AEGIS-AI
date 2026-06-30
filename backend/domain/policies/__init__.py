"""
AEGIS AI Domain

Decision Policies.
"""

from .majority_vote_policy import MajorityVotePolicy

from backend.domain.policies.majority_vote_policy import (
    MajorityVotePolicy,
)

__all__ = [
    "MajorityVotePolicy",
]