# Network File System (NFS)

NFS allows the sharing and mounting of remote file systems.

## `nmap` Scripts

Various scripts are available for NFS.

## Mounting Shares

Network shares can be mounted:

```bash
sudo mount -o <OPTIONS> <HOST>:/<SHARE> /mnt
```

Where:

- `<OPTIONS>`: options to set for the mount
- `<HOST>`: hostname or IP address which is sharing the share
- `<SHARE>`: name of the share being shared

Specific options of interest:

- `nolock`: Do not lock files, useful for legacy NFS servers
