# File Searching

Commands for finding files on a system.

## Linux

### `locate`

- Search for a file by name

```shell
$ locate 'some-document'
```

- Search for a file by name (regular expressions)

```bash
$ locate --regex '^some-document.*txt$'
```

- Search for a file by the full name

```bash
$ locate -w 'some-document.txt'
```

### `find`

- Search for a file by name (use `-iname` to be case-insensitive)

```bash
$ find / -name 'some-document.txt'
```

- Search for any file owned by the given user and group

```bash
$ find / -user 'some-user' -group 'some-group'
```

- Search for any file modified in the past `n * 24hrs`

```bash
$ find / -mtime n
```

- Search for any file of the specified type

```bash
$ find / -type f
```

Notes:

- `-type c` where `c` is one of the following:

  - `b`: block (buffered) special
  - `c`: character (unbuffered) special
  - `d`: directory
  - `p`: named pipe (FIFO)
  - `f`: regular file
  - `l`: symbolic link
  - `s`: socket

- the first argument is the start directory (use `/` to search entire filesystem)

## Windows

TODO.
