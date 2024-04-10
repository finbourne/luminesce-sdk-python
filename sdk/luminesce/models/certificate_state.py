# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist
from luminesce.models.certificate_status import CertificateStatus
from luminesce.models.certificate_type import CertificateType
from luminesce.models.link import Link

class CertificateState(BaseModel):
    """
    Information held about the minting / revoking of a certificate.  It does *not* contain the certificate itself  # noqa: E501
    """
    key: Optional[StrictStr] = Field(None, description="The \"key\" to which this belongs in the dictionary,  basically the CN without any version information")
    version: Optional[StrictInt] = Field(None, description="The version of this certificate")
    common_name: Optional[StrictStr] = Field(None, alias="commonName", description="The common Name of the Certificate")
    type: Optional[CertificateType] = None
    creation_status: Optional[CertificateStatus] = Field(None, alias="creationStatus")
    revocation_status: Optional[CertificateStatus] = Field(None, alias="revocationStatus")
    validity_start: Optional[datetime] = Field(None, alias="validityStart", description="The earliest point at which a certificate can be used")
    validity_end: Optional[datetime] = Field(None, alias="validityEnd", description="The latest point at which a certificate can be used")
    revoked_at: Optional[datetime] = Field(None, alias="revokedAt", description="The point at which this was revoked, if any")
    revoked_by: Optional[StrictStr] = Field(None, alias="revokedBy", description="The user which revoked this, if any")
    created_at: Optional[datetime] = Field(None, alias="createdAt", description="The point at which this was created")
    created_by: Optional[StrictStr] = Field(None, alias="createdBy", description="The user which created this")
    serial_number: Optional[StrictStr] = Field(None, alias="serialNumber", description="The Vault-issued serial number of the certificate, if any - used for revocation")
    links: Optional[conlist(Link)] = Field(None, description="The location within Configuration Store that this is saved to")
    __properties = ["key", "version", "commonName", "type", "creationStatus", "revocationStatus", "validityStart", "validityEnd", "revokedAt", "revokedBy", "createdAt", "createdBy", "serialNumber", "links"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CertificateState:
        """Create an instance of CertificateState from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if key (nullable) is None
        # and __fields_set__ contains the field
        if self.key is None and "key" in self.__fields_set__:
            _dict['key'] = None

        # set to None if common_name (nullable) is None
        # and __fields_set__ contains the field
        if self.common_name is None and "common_name" in self.__fields_set__:
            _dict['commonName'] = None

        # set to None if validity_start (nullable) is None
        # and __fields_set__ contains the field
        if self.validity_start is None and "validity_start" in self.__fields_set__:
            _dict['validityStart'] = None

        # set to None if validity_end (nullable) is None
        # and __fields_set__ contains the field
        if self.validity_end is None and "validity_end" in self.__fields_set__:
            _dict['validityEnd'] = None

        # set to None if revoked_at (nullable) is None
        # and __fields_set__ contains the field
        if self.revoked_at is None and "revoked_at" in self.__fields_set__:
            _dict['revokedAt'] = None

        # set to None if revoked_by (nullable) is None
        # and __fields_set__ contains the field
        if self.revoked_by is None and "revoked_by" in self.__fields_set__:
            _dict['revokedBy'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['createdAt'] = None

        # set to None if created_by (nullable) is None
        # and __fields_set__ contains the field
        if self.created_by is None and "created_by" in self.__fields_set__:
            _dict['createdBy'] = None

        # set to None if serial_number (nullable) is None
        # and __fields_set__ contains the field
        if self.serial_number is None and "serial_number" in self.__fields_set__:
            _dict['serialNumber'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CertificateState:
        """Create an instance of CertificateState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CertificateState.parse_obj(obj)

        _obj = CertificateState.parse_obj({
            "key": obj.get("key"),
            "version": obj.get("version"),
            "common_name": obj.get("commonName"),
            "type": obj.get("type"),
            "creation_status": obj.get("creationStatus"),
            "revocation_status": obj.get("revocationStatus"),
            "validity_start": obj.get("validityStart"),
            "validity_end": obj.get("validityEnd"),
            "revoked_at": obj.get("revokedAt"),
            "revoked_by": obj.get("revokedBy"),
            "created_at": obj.get("createdAt"),
            "created_by": obj.get("createdBy"),
            "serial_number": obj.get("serialNumber"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
