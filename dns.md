# Domain Name Server (DNS)

## Lookup with `host`

```bash
host <HOST or IP>
```

Where:

- `<HOST OR IP>`: a hostname or IP address

Tips:

- The `host` command works for forward and reverse lookups
- Use wordlists to help this lookup process (e.g., `seclists`)

## Query with `host`

```bash
host -t <TYPE> <HOST or IP>
```

Where:

- `<TYPE>`: the type of record being queried
- `<HOST OR IP>`: a hostname or IP address

## Zone Transfer with `host`

```bash
host -l <HOST> <DNS IP>
```

Where:

- `<HOST>`: a hostname or IP address
- `<DNS IP>`: IP address of the authoritative DNS server

## Other DNS Tools

### `dnsrecon`

```bash
dnsrecon -d <HOST> -t axfr
```

Where:

- `<HOST>`: a hostname or IP address

### `dnsenum`

```bash
dnsenum <HOST>
```

Where:

- `<HOST>`: a hostname or IP address
