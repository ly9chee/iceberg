# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from pyiceberg.manifest import (
    DataFile,
    FieldSummary,
    FileFormat,
    ManifestEntry,
    ManifestFile,
    read_manifest_entry,
    read_manifest_list,
)
from tests.io.test_io_base import LocalInputFile


def test_read_manifest_entry(generated_manifest_entry_file: str):
    input_file = LocalInputFile(generated_manifest_entry_file)
    assert list(read_manifest_entry(input_file)) == [
        ManifestEntry(
            status=1,
            snapshot_id=8744736658442914487,
            data_file=DataFile(
                file_path="/home/iceberg/warehouse/nyc/taxis_partitioned/data/VendorID=null/00000-633-d8a4223e-dc97-45a1-86e1-adaba6e8abd7-00001.parquet",
                file_format=FileFormat.PARQUET,
                partition={"VendorID": None},
                record_count=19513,
                file_size_in_bytes=388872,
                block_size_in_bytes=67108864,
                column_sizes={
                    1: 53,
                    2: 98153,
                    3: 98693,
                    4: 53,
                    5: 53,
                    6: 53,
                    7: 17425,
                    8: 18528,
                    9: 53,
                    10: 44788,
                    11: 35571,
                    12: 53,
                    13: 1243,
                    14: 2355,
                    15: 12750,
                    16: 4029,
                    17: 110,
                    18: 47194,
                    19: 2948,
                },
                value_counts={
                    1: 19513,
                    2: 19513,
                    3: 19513,
                    4: 19513,
                    5: 19513,
                    6: 19513,
                    7: 19513,
                    8: 19513,
                    9: 19513,
                    10: 19513,
                    11: 19513,
                    12: 19513,
                    13: 19513,
                    14: 19513,
                    15: 19513,
                    16: 19513,
                    17: 19513,
                    18: 19513,
                    19: 19513,
                },
                null_value_counts={
                    1: 19513,
                    2: 0,
                    3: 0,
                    4: 19513,
                    5: 19513,
                    6: 19513,
                    7: 0,
                    8: 0,
                    9: 19513,
                    10: 0,
                    11: 0,
                    12: 19513,
                    13: 0,
                    14: 0,
                    15: 0,
                    16: 0,
                    17: 0,
                    18: 0,
                    19: 0,
                },
                nan_value_counts={16: 0, 17: 0, 18: 0, 19: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0},
                lower_bounds={
                    2: b"2020-04-01 00:00",
                    3: b"2020-04-01 00:12",
                    7: b"\x03\x00\x00\x00",
                    8: b"\x01\x00\x00\x00",
                    10: b"\xf6(\\\x8f\xc2\x05S\xc0",
                    11: b"\x00\x00\x00\x00\x00\x00\x00\x00",
                    13: b"\x00\x00\x00\x00\x00\x00\x00\x00",
                    14: b"\x00\x00\x00\x00\x00\x00\xe0\xbf",
                    15: b")\\\x8f\xc2\xf5(\x08\xc0",
                    16: b"\x00\x00\x00\x00\x00\x00\x00\x00",
                    17: b"\x00\x00\x00\x00\x00\x00\x00\x00",
                    18: b"\xf6(\\\x8f\xc2\xc5S\xc0",
                    19: b"\x00\x00\x00\x00\x00\x00\x04\xc0",
                },
                upper_bounds={
                    2: b"2020-04-30 23:5:",
                    3: b"2020-05-01 00:41",
                    7: b"\t\x01\x00\x00",
                    8: b"\t\x01\x00\x00",
                    10: b"\xcd\xcc\xcc\xcc\xcc,_@",
                    11: b"\x1f\x85\xebQ\\\xe2\xfe@",
                    13: b"\x00\x00\x00\x00\x00\x00\x12@",
                    14: b"\x00\x00\x00\x00\x00\x00\xe0?",
                    15: b"q=\n\xd7\xa3\xf01@",
                    16: b"\x00\x00\x00\x00\x00`B@",
                    17: b"333333\xd3?",
                    18: b"\x00\x00\x00\x00\x00\x18b@",
                    19: b"\x00\x00\x00\x00\x00\x00\x04@",
                },
                key_metadata=None,
                split_offsets=[4],
                sort_order_id=0,
            ),
        ),
        ManifestEntry(
            status=1,
            snapshot_id=8744736658442914487,
            data_file=DataFile(
                file_path="/home/iceberg/warehouse/nyc/taxis_partitioned/data/VendorID=1/00000-633-d8a4223e-dc97-45a1-86e1-adaba6e8abd7-00002.parquet",
                file_format=FileFormat.PARQUET,
                partition={"VendorID": 1},
                record_count=95050,
                file_size_in_bytes=1265950,
                block_size_in_bytes=67108864,
                column_sizes={
                    1: 318,
                    2: 329806,
                    3: 331632,
                    4: 15343,
                    5: 2351,
                    6: 3389,
                    7: 71269,
                    8: 76429,
                    9: 16383,
                    10: 86992,
                    11: 89608,
                    12: 265,
                    13: 19377,
                    14: 1692,
                    15: 76162,
                    16: 4354,
                    17: 759,
                    18: 120650,
                    19: 11804,
                },
                value_counts={
                    1: 95050,
                    2: 95050,
                    3: 95050,
                    4: 95050,
                    5: 95050,
                    6: 95050,
                    7: 95050,
                    8: 95050,
                    9: 95050,
                    10: 95050,
                    11: 95050,
                    12: 95050,
                    13: 95050,
                    14: 95050,
                    15: 95050,
                    16: 95050,
                    17: 95050,
                    18: 95050,
                    19: 95050,
                },
                null_value_counts={
                    1: 0,
                    2: 0,
                    3: 0,
                    4: 0,
                    5: 0,
                    6: 0,
                    7: 0,
                    8: 0,
                    9: 0,
                    10: 0,
                    11: 0,
                    12: 95050,
                    13: 0,
                    14: 0,
                    15: 0,
                    16: 0,
                    17: 0,
                    18: 0,
                    19: 0,
                },
                nan_value_counts={16: 0, 17: 0, 18: 0, 19: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0},
                lower_bounds={
                    1: b"\x01\x00\x00\x00",
                    2: b"2020-04-01 00:00",
                    3: b"2020-04-01 00:03",
                    4: b"\x00\x00\x00\x00",
                    5: b"\x01\x00\x00\x00",
                    6: b"N",
                    7: b"\x01\x00\x00\x00",
                    8: b"\x01\x00\x00\x00",
                    9: b"\x01\x00\x00\x00",
                    10: b"\x00\x00\x00\x00\x00\x00\x00\x00",
                    11: b"\x00\x00\x00\x00\x00\x00\x00\x00",
                    13: b"\x00\x00\x00\x00\x00\x00\x00\x00",
                    14: b"\x00\x00\x00\x00\x00\x00\x00\x00",
                    15: b"\x00\x00\x00\x00\x00\x00\x00\x00",
                    16: b"\x00\x00\x00\x00\x00\x00\x00\x00",
                    17: b"\x00\x00\x00\x00\x00\x00\x00\x00",
                    18: b"\x00\x00\x00\x00\x00\x00\x00\x00",
                    19: b"\x00\x00\x00\x00\x00\x00\x00\x00",
                },
                upper_bounds={
                    1: b"\x01\x00\x00\x00",
                    2: b"2020-04-30 23:5:",
                    3: b"2020-05-01 00:1:",
                    4: b"\x06\x00\x00\x00",
                    5: b"c\x00\x00\x00",
                    6: b"Y",
                    7: b"\t\x01\x00\x00",
                    8: b"\t\x01\x00\x00",
                    9: b"\x04\x00\x00\x00",
                    10: b"\\\x8f\xc2\xf5(8\x8c@",
                    11: b"\xcd\xcc\xcc\xcc\xcc,f@",
                    13: b"\x00\x00\x00\x00\x00\x00\x1c@",
                    14: b"\x9a\x99\x99\x99\x99\x99\xf1?",
                    15: b"\x00\x00\x00\x00\x00\x00Y@",
                    16: b"\x00\x00\x00\x00\x00\xb0X@",
                    17: b"333333\xd3?",
                    18: b"\xc3\xf5(\\\x8f:\x8c@",
                    19: b"\x00\x00\x00\x00\x00\x00\x04@",
                },
                key_metadata=None,
                split_offsets=[4],
                sort_order_id=0,
            ),
        ),
    ]


def test_read_manifest_list(generated_manifest_file_file: str):
    input_file = LocalInputFile(generated_manifest_file_file)
    assert list(read_manifest_list(input_file)) == [
        ManifestFile(
            manifest_path="/home/iceberg/warehouse/nyc/taxis_partitioned/metadata/0125c686-8aa6-4502-bdcc-b6d17ca41a3b-m0.avro",
            manifest_length=7989,
            partition_spec_id=0,
            added_snapshot_id=9182715666859759686,
            added_data_files_count=3,
            existing_data_files_count=0,
            deleted_data_files_count=0,
            partitions=[
                FieldSummary(
                    contains_null=True, contains_nan=False, lower_bound=b"\x01\x00\x00\x00", upper_bound=b"\x02\x00\x00\x00"
                )
            ],
            added_rows_count=237993,
            existing_rows_counts=None,
            deleted_rows_count=0,
        )
    ]