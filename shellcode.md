# Shellcode

## Illegal Characters

The following characters should not be used in shellcode.

Character (Hex) | Ascii Mapping    | Reasoning
--------------- | ---------------- | ------------------------------------------------------------------------
00              | Null Byte        | Terminates a string therefore ending string-based operations (e.g, copy)
0a              | Line Feed        | Creates a newline in the HTTP GET parameter string, messing it up
0d              | Carriage Return  | Similar to Line Feed, but returns to the start of the current line
25              | Percent Sign (%) | Place marker for a HTML encoded entity (e.g. '%20' for space)
26              | And Sign (&)     | Separates different parameters in HTTP requests
2b              | Plus Sign (+)    | Represents a single whitespace in HTTP requests
3d              | Equals Sign (=)  | Represents assignment of a value to a parameter
