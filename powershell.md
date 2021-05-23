# Powershell Commands

Useful cmdlets for PowerShell.

## Setting Up

- Allow scripts

```powershell
Set-ExecutionPolicy POLICY
```

Where:

- `POLICY` is one of:

  - `AllSigned`: all scripts must be signed
  - `Bypass`: don't block anything, allow all, no warnings
  - `RemoteSigned`: all remote scripts must be signed
  - `Restricted`: don't run any scripts
  - `Unrestricted`: run all scripts

## Running Scripts

- Dot-sourcing

```powershell
. .\script.ps1
```

Dot-sourcing loads a script into the current PowerShell session which makes any variables and functions visible to the current scope.
