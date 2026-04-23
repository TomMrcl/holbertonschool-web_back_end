#!/usr/bin/env python3
"""Update topics of a school document"""


def update_topics(mongo_collection, name, topics):
    """Update all topics for a school matching the given name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
