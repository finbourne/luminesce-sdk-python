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





class LuminesceBinaryType(str, Enum):
    """
    Binaries that can be downloaded
    """

    """
    allowed enum values
    """
    COMMANDLINETOOL = 'CommandLineTool'
    LOCAL_FILE_SYSTEM_PROVIDERS = 'LocalFileSystem_Providers'
    EMAIL_PROVIDERS = 'Email_Providers'
    PYTHON_PROVIDERS = 'Python_Providers'
    AWS_S3_PROVIDERS = 'AwsS3_Providers'
    SQL_DB_PROVIDERS_DB2_LINUX = 'SqlDb_Providers_Db2Linux'
    SQL_DB_PROVIDERS_MY_SQL = 'SqlDb_Providers_MySql'
    SQL_DB_PROVIDERS_ORACLE = 'SqlDb_Providers_Oracle'
    SQL_DB_PROVIDERS_ORACLE_SNOWFLAKE = 'SqlDb_Providers_Oracle_Snowflake'
    SQL_DB_PROVIDERS_POSTGRESQL = 'SqlDb_Providers_Postgresql'
    SQL_DB_PROVIDERS_SNOWFLAKE = 'SqlDb_Providers_Snowflake'
    SQL_DB_PROVIDERS_SQL_SERVER = 'SqlDb_Providers_SqlServer'
    SQL_DB_PROVIDERS_SYBASE_ASE = 'SqlDb_Providers_SybaseAse'
    JDBC_DRIVER = 'Jdbc_Driver'

    @classmethod
    def from_json(cls, json_str: str) -> LuminesceBinaryType:
        """Create an instance of LuminesceBinaryType from a JSON string"""
        return LuminesceBinaryType(json.loads(json_str))
