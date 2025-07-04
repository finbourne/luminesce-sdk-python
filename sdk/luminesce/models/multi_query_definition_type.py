# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class MultiQueryDefinitionType(str, Enum):
    """
    MultiQueryDefinitionType
    """

    """
    allowed enum values
    """
    INSTRUMENT = 'Instrument'
    EXPIRY = 'Expiry'
    CORPORATEACTIONS = 'CorporateActions'
    EDIINSTRUMENT = 'EdiInstrument'
    EDIINSTRUMENTWRITER = 'EdiInstrumentWriter'
    TESTING = 'Testing'
    MARKETPLACECLIENTLOADHISTORY = 'MarketplaceClientLoadHistory'
    INSIGHTSMETRICSENTITLEMENT = 'InsightsMetricsEntitlement'
    INSTRUMENTDISCOVERY = 'InstrumentDiscovery'
    INSTRUMENTUPSERT = 'InstrumentUpsert'
    INSIGHTSAPPLICATIONREQUESTLOGS = 'InsightsApplicationRequestLogs'
    INSIGHTSVENDORLOGS = 'InsightsVendorLogs'

    @classmethod
    def from_json(cls, json_str: str) -> MultiQueryDefinitionType:
        """Create an instance of MultiQueryDefinitionType from a JSON string"""
        return MultiQueryDefinitionType(json.loads(json_str))
