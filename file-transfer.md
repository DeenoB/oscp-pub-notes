# File Transfer

## wget

- Downloading a file with `wget`

```bash
$ wget -O output-file URL
```

## curl

- Downloading a file with `curl`

```bash
$ curl -o output-file URL
```

## axel

`axel` is used to maximise download speeds when transferring via FTP/HTTP; it does so by utilising multiple connections.

- Downloading a file with `axel`

```bash
$ axel -n connection-count -o output-file URL
```

## socat

- Transfer a file with `socat`

```bash
$ socat TCP4-LISTEN:PORT,fork file:in-file
```

- Accept a file with `socat`

```bash
$ socat TCP4:ADDRESS:PORT file:out-file,create
```

## PowerShell

- Transfer a file with PowerShell:

```powershell
powershell -c "(new-object System.Net.WebClient).DownloadFile('source','destination')"
powershell -c "(new-object System.Net.WebClient).DownloadFile('http://website/file.txt','C:\Users\SomeUser\Desktop\file.txt')"
```

## PowerCat

- Transfer a file with `powercat`:

```powershell
powercat -c ADDR -p PORT -i file
```
