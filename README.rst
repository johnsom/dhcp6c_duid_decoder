.. meta::
   :description: A simple tool to decode dhcp6c_duid device ID files into human readable form.
   :keywords: DHCPv6 dhcp6c_duid DUID
   :locale: en_US
   :author: Michael Johnson
   :robots: index

========================
Decode DHCP6c DUID Files
========================

This is a simple python script that will decode dhcp6c Device UUID (DUID) files
into a human readable form. This is handy when you are replacing your edge
network equipment, such as a firewall, with a different brand that requires
the decoded field information.

*Usage:*

.. code-block:: bash

    $decode_duid.py dhcp6c_duid
    Data length: 14
    DUID Type: 1 [DUID-LLT - Link-layer address plus time]
    Hardware Type: 1 [Ethernet]
    Seconds since midnight (UTC), January 1, 2000: 1000
    Link-layer Address: 00:00:5E:00:53:00

.. note::

   This has been tested with wide-dhcpv6-client, which only supports DUID type
   1, the other decoders are based on
   `RFC 3315 <https://www.rfc-editor.org/rfc/rfc3315.html>`_ and
   `RFC 6355 <https://www.rfc-editor.org/rfc/rfc6355.html>`_.
   There may be bugs.

Disclaimers
***********

* This document comes without any warranty of any kind.
* Not intended for safety of life applications.
* The code provided in this repository is licensed under the Apache License,
  Version 2.0. See the included LICENSE for terms.
* This document is Copyright 2023 Michael Johnson
* This document is licensed under the Creative Commons Attribution-ShareAlike
  4.0 International Public License

.. raw:: html

   <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">Decode DHCP6c DUID Files</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/johnsom" property="cc:attributionName" rel="cc:attributionURL">Michael Johnson</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
