def pytest_itemcollected(item):
    """
    Custom pytest hook to modify collected item's node ID.
    This hook combines parent and node information to form a more informative node ID.
    """
    parent_description = item.parent.obj.__doc__.strip() if item.parent.obj.__doc__ else item.parent.obj.__class__.__name__
    node_description = item.obj.__doc__.strip() if item.obj.__doc__ else item.obj.__name__
    if parent_description or node_description:
        item._nodeid = f"{parent_description} {node_description}"
