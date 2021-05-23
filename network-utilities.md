# Network Utilities

This section covers utilities used to create network connections and connect remote streams.

## netcat

## socat

Very similar in principle to `netcat`, however slightly complicated in terms of arguments.

- Basic operation of `socat`:

```bash
$ socat [options] <address> <address>
```

### Address Keywords

These keywords specify the actual protocols and addresses to use for connection:

For TCP:

- `TCP4:ADDR:PORT`: connect to the address and port with TCP and IPv4
- `TCP6:ADDR:PORT`: connect to the address and port with TCP and IPv6
- `TCP4-LISTEN:PORT`: listen on the given port using TCP and IPv4
- `TCP6-LISTEN:PORT`: listen on the given port using TCP and IPv6

For UDP:

- `UDP4:ADDR:PORT`: connect to the address and port with UDP and IPv4
- `UDP6:ADDR:PORT`: connect to the address and port with UDP and IPv6
- `UDP4-LISTEN:PORT`: listen on the given port using UDP and IPv4
- `UDP6-LISTEN:PORT`: listen on the given port using UDP and IPv6

Non-network keywords:

- `file:some_file.txt`: use a file
- `-`: use the `STDIO`
- `STDOUT`/`STDIN`/`STDERR`: standard out, in, err

### Address Options

These options are added with commas, after the address part.

- `fork`: Creates a child process to handle the connection, useful if you are using `socat` as a listener/server - i.e. to handle multiple connections

## rdp

Remote desktop protocol, typically for Windows.

- Open up a regular RDP session with a user and pass

```bash
$ xfreerdp /u:USER /p:PASS /v:ADDRESS
```

- RDP with `rdesktop`

```bash
$ rdesktop ADDR -u username -p password -g 1920x1080
```
