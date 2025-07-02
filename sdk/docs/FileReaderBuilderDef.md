# FileReaderBuilderDef

Information on how to construct a file-read sql query
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_detect** | [**AutoDetectType**](AutoDetectType.md) |  | [optional] 
**columns** | [**List[ColumnInfo]**](ColumnInfo.md) | Column information for the results | [optional] 
**limit** | **int** | What limit be added to the load query?  Less than or equal to zero means none | [optional] 
**source** | [**Source**](Source.md) |  | [optional] 
**available_sources** | [**List[Source]**](Source.md) | The source locations the user has access to.  The provider in essence. | [optional] 
**variable_name** | **str** | The name of the variable for the &#x60;use&#x60; statement | [optional] 
**file_path** | **str** | The file (or folder) path | [optional] 
**folder_filter** | **str** | The filter to apply to a folder (all matching files then being read) a RegExp | [optional] 
**zip_filter** | **str** | The filter to apply to folder structures with zip archives (all matching files then being read) a RegExp | [optional] 
**add_file_name** | **bool** | Should a file name column be added to the output? | [optional] 
**csv** | [**OptionsCsv**](OptionsCsv.md) |  | [optional] 
**excel** | [**OptionsExcel**](OptionsExcel.md) |  | [optional] 
**sq_lite** | [**OptionsSqLite**](OptionsSqLite.md) |  | [optional] 
**xml** | [**OptionsXml**](OptionsXml.md) |  | [optional] 
**parquet** | [**OptionsParquet**](OptionsParquet.md) |  | [optional] 
## Example

```python
from luminesce.models.file_reader_builder_def import FileReaderBuilderDef
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt, conlist, constr

auto_detect: Optional[AutoDetectType] = # Replace with your value
columns: Optional[conlist(ColumnInfo)] = # Replace with your value
limit: Optional[StrictInt] = # Replace with your value
limit: Optional[StrictInt] = None
source: Optional[Source] = None
available_sources: Optional[conlist(Source)] = # Replace with your value
variable_name: Optional[StrictStr] = "example_variable_name"
file_path: Optional[StrictStr] = "example_file_path"
folder_filter: Optional[StrictStr] = "example_folder_filter"
zip_filter: Optional[StrictStr] = "example_zip_filter"
add_file_name: Optional[StrictBool] = # Replace with your value
add_file_name:Optional[StrictBool] = None
csv: Optional[OptionsCsv] = None
excel: Optional[OptionsExcel] = None
sq_lite: Optional[OptionsSqLite] = # Replace with your value
xml: Optional[OptionsXml] = None
parquet: Optional[OptionsParquet] = None
file_reader_builder_def_instance = FileReaderBuilderDef(auto_detect=auto_detect, columns=columns, limit=limit, source=source, available_sources=available_sources, variable_name=variable_name, file_path=file_path, folder_filter=folder_filter, zip_filter=zip_filter, add_file_name=add_file_name, csv=csv, excel=excel, sq_lite=sq_lite, xml=xml, parquet=parquet)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

