# Remote Procedure Call (RPC) and Portmapper

RPC and Portmapper run on TCP-111 and their purpose is to:

- Allow RPC-based applications to register to them
- Map TCP-111 to the specific application's real port
- Allow clients to provide an RPC application number
- Return the RPC mapping to the client

NFS is an example of an RPC-based application.

## `nmap` Scripts

Use `--script=rpcinfo` to extract information about the RPC mappings.

```bash
nmap -sV -p111 --script=rpcinfo <HOST>
```
