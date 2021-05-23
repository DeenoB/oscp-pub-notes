# Simple Network Management Protocol (SNMP)

## Enumeration with `snmpwalk`

```bash
snmpwalk -c <COMMUNITY> -v<VERSION> <MIB>..
```

Where:

- `<COMMUNITY>`: community string (often "public")
- `<VERSION>`: SNMP version
- `<MIB>`: the Management Information Base (MIB) node(s) to search for

  - Can be omitted if the entire MIB tree is to be returned

## Management Information Base (MIB)

Here are some useful MIB values:

Value                  | Data
---------------------- | -------------------------
1.3.6.1.2.1.6.13.1.3   | Open TCP ports
1.3.6.1.2.1.25.4.2.1.2 | Windows running processes
1.3.6.1.2.1.25.6.3.1.2 | Installed software
1.3.6.1.4.1.77.1.2.25  | Windows users
