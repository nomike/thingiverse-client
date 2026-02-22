from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UrlSchema")


@_attrs_define
class UrlSchema:
    """
    Attributes:
        auth (str | Unset):
        hash_ (str | Unset):
        host (str | Unset):
        hostname (str | Unset):
        href (str | Unset):
        path (str | Unset):
        pathname (str | Unset):
        port (int | str | Unset):
        protocol (str | Unset):
        query (int | list[str] | str | Unset):
        search (str | Unset):
        slashes (bool | Unset):
    """

    auth: str | Unset = UNSET
    hash_: str | Unset = UNSET
    host: str | Unset = UNSET
    hostname: str | Unset = UNSET
    href: str | Unset = UNSET
    path: str | Unset = UNSET
    pathname: str | Unset = UNSET
    port: int | str | Unset = UNSET
    protocol: str | Unset = UNSET
    query: int | list[str] | str | Unset = UNSET
    search: str | Unset = UNSET
    slashes: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth = self.auth

        hash_ = self.hash_

        host = self.host

        hostname = self.hostname

        href = self.href

        path = self.path

        pathname = self.pathname

        port: int | str | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        protocol = self.protocol

        query: int | list[str] | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        elif isinstance(self.query, list):
            query = self.query

        else:
            query = self.query

        search = self.search

        slashes = self.slashes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth is not UNSET:
            field_dict["auth"] = auth
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if host is not UNSET:
            field_dict["host"] = host
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if href is not UNSET:
            field_dict["href"] = href
        if path is not UNSET:
            field_dict["path"] = path
        if pathname is not UNSET:
            field_dict["pathname"] = pathname
        if port is not UNSET:
            field_dict["port"] = port
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if query is not UNSET:
            field_dict["query"] = query
        if search is not UNSET:
            field_dict["search"] = search
        if slashes is not UNSET:
            field_dict["slashes"] = slashes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth = d.pop("auth", UNSET)

        hash_ = d.pop("hash", UNSET)

        host = d.pop("host", UNSET)

        hostname = d.pop("hostname", UNSET)

        href = d.pop("href", UNSET)

        path = d.pop("path", UNSET)

        pathname = d.pop("pathname", UNSET)

        def _parse_port(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        protocol = d.pop("protocol", UNSET)

        def _parse_query(data: object) -> int | list[str] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                query_type_2 = cast(list[str], data)

                return query_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(int | list[str] | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        search = d.pop("search", UNSET)

        slashes = d.pop("slashes", UNSET)

        url_schema = cls(
            auth=auth,
            hash_=hash_,
            host=host,
            hostname=hostname,
            href=href,
            path=path,
            pathname=pathname,
            port=port,
            protocol=protocol,
            query=query,
            search=search,
            slashes=slashes,
        )

        url_schema.additional_properties = d
        return url_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
