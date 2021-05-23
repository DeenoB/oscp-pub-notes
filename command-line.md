# Command Line

Notes regarding the commandline and shell specifics.

## Bash

### Environment Variables

Useful envars to know:

Environment Variable | Purpose
-------------------- | -----------------------------
`$PATH`              | binary search path
`$USER`              | current user's name
`$PWD`               | working directory
`$HOME`              | current user's home directory
`$$`                 | the PUID of the current shell

- Storing a variable (not exported to spawned shells)

```bash
$ ENVAR=30; echo $ENVAR
$ sh
$ echo $ENVAR
<Nothing, since ENVAR is not exported to sub-shell>
```

- Storing an environment variable (so its value is persistent)

```bash
$ export ENVAR=30
$ sh
$ echo $ENVAR
30
```

- Viewing all environment variables

```bash
$ env
```

### History

The shell history can be controlled by environment variables:

- `HISTSIZE` : in-memory limit to command history
- `HISTFILESIZE` :command limit of the history file (`.bash_history`)
- `HISTIGNORE`: colon-separated list of commands to not save in history
- `HISTCONTROL` : colon-separated list containing some of:

  - `ignorespace`: lines begining with a space are not saved
  - `ignoredups`: duplicates of existing history commands are not saved
  - `ignoreboth`: entails both `ignorespace` and `ignoredups`
  - `erasedups`: save the latest command, delete dupes from history

- Viewing the command history

```bash
$ history
```

- Re-run command using ID from `history` command

```bash
$ !3
```

- Re-run last command

```bash
$ !!
```

### Alias

- Create an alias

```bash
$ alias blah='some command'
```

- Remove an alias

```bash
$ unalias blah
```

### Evaluation

- Evaluate a Base-N number

```bash
$ echo "$((N#1234))"
```

### Special Variables

Variable Name | Description
------------- | ------------------------------------------------
$0            | The name of the Bash script
\$1 - \$9     | The first 9 arguments to the Bash script
$#            | Number of arguments passed to the Bash script
$@            | All arguments passed to the Bash script
$?            | The exit status of the most recently run process
$$            | The process ID of the current script
$USER         | The username of the user running the script
$HOSTNAME     | The hostname of the machine
$RANDOM       | A random number
$LINENO       | The current line number in the script
