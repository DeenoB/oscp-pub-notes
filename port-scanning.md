# Port Scanning

## `nmap`

### Port Scan Flags

Flag  | Type
----- | ---------------------------
`-sT` | TCP Connect
`-sS` | TCP SYN
`-sU` | UDP
`-sL` | List: Just list the targets
`-sV` | Service version detection

### Host Discovery Flags

Flag  | Type
----- | -----------------
`-sn` | Host Discovery
`-Pn` | No Host Discovery
`-O`  | OS Detection

### Composite Flags

Flag | Type
---- | ----------------------------------------------------
`-A` | OS Detection, Version Detection, Scripts, Traceroute

### Stealth Flags

Flag    | Type
------- | --------------------------------------------------------
`-T0-5` | 0 is very slow, 5 is very fast. Mnemonic: 0 = Zero Speed

### Scripts

Scripts for `nmap` can be found in `/usr/share/nmap/scripts`.
