# LUMINESCE<sup>®</sup> Python SDK
This is the Python SDK for [LUMINESCE by FINBOURNE](https://www.finbourne.com/luminesce/), a data virtualisation platform that lets you explore, query, fetch and combine data from multiple sources and systems, including LUSID, into an integrated view for interrogation. To use it you'll need a LUSID account. [Sign up for free at lusid.com](https://www.lusid.com/app/signup)

<a href="https://www.lusid.com/app/signup"><img src="https://content.finbourne.com/LUSID_repo.png" alt="LUSID_by_Finbourne"></a>

## Build Status

| branch | status |
| --- | --- |
| `main` |  ![PyPI](https://img.shields.io/pypi/v/luminesce-sdk?color=blue) ![build](https://github.com/finbourne/luminesce-sdk-python/workflows/luminesce-sdk-python-test/badge.svg) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=finbourne_luminesce-sdk-python&metric=alert_status)](https://sonarcloud.io/dashboard?id=finbourne_luminesce-sdk-python) |


## Installation

The PyPi package for the LUMINESCE SDK can installed using the following:

```
pip install luminesce-sdk
```

For more information on the LUMINESCE API, see [LUMINESCE API Documentation](https://www.lusid.com/honeycomb/swagger/index.html).


## Usage

```python
import luminesce
from luminesce import ApiClientFactory

factory = ApiClientFactory()
sql_exec_api = factory.build(luminesce.api.SqlExecutionApi)

await sql_exec_api.put_by_query_csv("""
    select * from lusid.portfolio limit 10
""")
```
