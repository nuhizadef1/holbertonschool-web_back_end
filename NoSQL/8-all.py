#!/usr/bin/env python3
"""List all documents in a Monge collection"""

def list_all(mongo_collection):
    """List all documents in collection"""
    documents = list(mongo_collection.find())
    return documents 
