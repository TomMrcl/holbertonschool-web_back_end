#!/usr/bin/env python3
"""List all documents in a collection"""


def list_all(mongo_collection):
    """Return list of all documents, or empty list if none."""
    return list(mongo_collection.find()) or []
