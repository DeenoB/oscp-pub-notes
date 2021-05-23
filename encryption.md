# Encryption

## SSL/TLS Certificates

- Creating a self-signed certificate

```bash
$ openssl req -newkey rsa:2048 -nodes -keyout bind_shell.key -x509 -days 36
2 -out bind_shell.crt
```

Where:

- `req`: create a CSR
- `-newkey`: generate private key
- `rsa:2048`: encryption method and key size
- `-nodes`: store private key without protection
- `-keyout file`: save key to file
- `-x509`: self-signed certificate instead of CSR
- `-days N`: validity period in days
- `-out file`: save certificate to file
