# Fuzzing

## Crafted Sequences

These are constructed sequences used to probe for buffer overflows. They are generated with a pattern so that unique points in the sequence can be found.

### Metasploit Patterns: `msf-pattern_create`

The command `msf-pattern_create` is used to construct a sequence with a provided pattern and length.

```bash
$ msf-pattern_create -l 50 
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab
```

### Metasploit Patterns: `msf-pattern_offset`

Given that you have used an MSF pattern, and you now have a subsequence of interest, you can find that within the original pattern.

```bash
$ msf-pattern_offset -l 50 -q Aa4A  
[*] Exact match at offset 12
```

Note: For some reason the `-q` argument only accepts 4 characters.
