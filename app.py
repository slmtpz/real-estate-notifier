import runpy


def handler(event, context):
    """Lambda function entry point."""

    runpy.run_module("real_estate_notifier")
