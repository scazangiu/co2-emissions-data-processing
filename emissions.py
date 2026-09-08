from __future__ import annotations
import sys
import csv
from typing import *
from dataclasses import dataclass
import unittest
import math

sys.setrecursionlimit(10_000)

@dataclass(frozen = True)
class Row:
    country: str
    year: int
    electricity_and_heat_co2_emissions: float | None
    electricity_and_heat_co2_emissions_per_capita: float | None
    energy_co2_emissions: float | None
    energy_co2_emissions_per_capita: float | None
    total_co2_emissions_excluding_lucf: float | None
    total_co2_emissions_excluding_lucf_per_capita: float | None


@dataclass(frozen = True)
class Node:
    value: Row
    next: Node | None


def convert_to_float(value: str) -> float | None:
    #Converts a CSV string value into a float, or None if the value is nonexistent
            if value == "":
                return None
            return float(value)
            
            
def parse_row(fields: list[str]) -> Row:
    #Converts one CSV row represented as strings into a Row object with proper data types
        return Row( country = fields[0], 
                    year = int(fields[1]),
                    electricity_and_heat_co2_emissions = convert_to_float(fields[2]),
                    electricity_and_heat_co2_emissions_per_capita = convert_to_float(fields[3]),
                    energy_co2_emissions = convert_to_float(fields[4]),
                    energy_co2_emissions_per_capita = convert_to_float(fields[5]),
                    total_co2_emissions_excluding_lucf = convert_to_float(fields[6]),
                    total_co2_emissions_excluding_lucf_per_capita = convert_to_float(fields[7])
                    )            
 
 
def build_linked_list(rows: list[list[str]]) -> Optional[Node]:
    #Recursively converts a list of CSV rows into a linked list of Row nodes
    if rows == []:
        return None
    return Node(parse_row(rows[0]), build_linked_list(rows[1:]))


def read_csv_lines(filename: str) -> Optional[Node]:
    #Reads the CSV file, checks its header, and returns its rows as a linked list
    expected_header = [
        "country",
        "year",
        "electricity_and_heat_co2_emissions",
        "electricity_and_heat_co2_emissions_per_capita",
        "energy_co2_emissions",
        "energy_co2_emissions_per_capita",
        "total_co2_emissions_excluding_lucf",
        "total_co2_emissions_excluding_lucf_per_capita"
    ]

    with open(filename, newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    header = rows[0]
    if header != expected_header:
        raise ValueError("unexpected first line: got: {}".format(header))

    data_rows = rows[1:]
    return build_linked_list(data_rows)


def listlen(data: Optional[Node]) -> int:
    #Recursively returns the number of nodes in a linked list
    if data is None:
        return 0
    return 1 + listlen(data.next)


def filter_rows(
    data: Optional[Node],
    field_name: str,
    comparison: str,
    value: Union[str, float, int]
    ) -> Optional[Node]:
        #Recursively returns a new linked list containing rows that match the given filter
        if data is None:
            return None
            
        filtered_list = filter_rows(data.next, field_name, comparison, value)
        field_value = getattr(data.value, field_name)
        
        if field_value is None:
            return filtered_list
            
        matches = False
        
        
        if field_name == "country":
            if comparison == "equal":
                matches = (field_value == value)
        else:
            if comparison == "less_than":
                matches = (field_value < value)
            elif comparison == "greater_than":
                matches = (field_value > value)
            elif comparison == "equal":
                matches = (field_value == value)

        if matches:
            return Node(data.value, filtered_list)
        else:
            return filtered_list
