#!/usr/bin/env python3
# Copyright 2023 Michael Johnson
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import struct
import sys
import uuid


if not sys.argv[1:]:
    print("Usage: decode_duid.py <dhcp6v_duid filename>")
    print("DUID filename is missing. Please try again.")
    sys.exit(1)

duid_types = ['DUID-LLT - Link-layer address plus time',
              'DUID-EN - Vendor-assigned unique ID based on Enterprise Number',
              'DUID-LL - Link-layer address',
              'DUID-UUID - Universally Unique IDentifier']
hw_types = ['Ethernet']

data =  open(sys.argv[1:][0], 'rb')

data_length = struct.unpack('!H', data.read(2))[0]
print('Data length: {}'.format(data_length))

duid_type = struct.unpack('!H', data.read(2))[0]
try:
    duid_type_name = duid_types[duid_type-1]
except IndexError:
    duid_type_name = 'Unknown'
print('DUID Type: {} [{}]'.format(duid_type, duid_type_name))

if duid_type == 1:
    hw_type = struct.unpack('!H', data.read(2))[0]
    try:
        hw_type_name = hw_types[hw_type-1]
    except IndexError:
        hw_type_name = 'Unknown'
    print('Hardware Type: {} [{}]'.format(hw_type, hw_type_name))

    print('Seconds since midnight (UTC), January 1, 2000: {}'.format(
          struct.unpack('!I', data.read(4))[0]))

    address_len = data_length - 8
    lla = data.read(address_len).hex()
    if address_len == 6:   # ethernet address
        print('Link-layer Address: {}'.format(
            ':'.join(a+b for a,b in zip(lla[::2], lla[1::2]))))
    else:
        print('Link-layer Address: {}'.format(lla))
elif duid_type == 2:
    print('Enterprise Number: '.format(struct.unpack('!L', data.read(4))[0]))

    address_len = data_length - 6
    print('Identifier: 0x'.format(data.read(address_len).hex()))
elif duid_type == 3:
    hw_type = struct.unpack('!H', data.read(2))[0]
    try:
        hw_type_name = hw_types[hw_type-1]
    except IndexError:
        hw_type_name = 'Unknown'
    print('Hardware Type: {} [{}]'.format(hw_type, hw_type_name))

    address_len = data_length - 4
    lla = data.read(address_len).hex()
    if address_len == 6:   # ethernet address
        print('Link-layer Address: {}'.format(
            ':'.join(a+b for a,b in zip(lla[::2], lla[1::2]))))
    else:
        print('Link-layer Address: {}'.format(lla))
elif duid_type == 4:
    uuid_hex = data.read(16).hex()
    uuid = uuid.UUID(hex=uuid_hex)
    print('UUID: {}'.format(str(uuid)))
else:
    print('Unknown DUID Type. Unable to decode.')
