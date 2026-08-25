# Network-Toolkit (NT)
Network_toolkit.html — a single-file, zero-dependency tool combining both scripts, opened in your browser.
# Objective
- Add IPv6 calculation support to the existing IPv4 subnet calculator script.
- Build an HTML tool that combines the functionality of IP Subnetting.py (IPv4/IPv6 subnetting) and ping_script_with range of IP address.py (ping scanning across an IP range) so network engineers can diagnose networks.
## About NT Toolkit
*Subnet Calculator (port of IP Subnetting.py)*
- Auto-detects IPv4/IPv6; accepts ip/prefix, ip mask, or 2001:db8::/32
- IPv4: network, broadcast, mask, wildcard, host range, usable count, class, RFC 1918/loopback/APIPA scope, binary views
- IPv6 (BigInt math): compressed + expanded forms, first/last address, total addresses, /64 count, type detection (multicast, link-local, ULA, documentation, Teredo, global unicast)

*Ping Sweep / Host Discovery (port of ping_script_with range of IP address.py)*
- Start–end IP range (v4 or v6), configurable port/timeout/concurrency
- Live progress bar, online/offline chips with latency, per-host PTR lookup via DNS-over-HTTPS, CSV export
# Limitation
One limitation documented in the tool's About tab: browsers can't send ICMP, so the sweep probes TCP/HTTP instead — hosts blocking that port show offline. For true ICMP + nmap OS/MAC fingerprinting, run your Python script locally.
