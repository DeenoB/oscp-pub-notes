# Burp Suite

## Intruder

The **Intruder** tab will take a specific request and use it as a basis to send crafted payload(s).

### Attack Types

Different attack types can be used, and they differ in how they deal with the payloads.

#### Sniper

- Given multiple payload positions: A, B, C...
- And a single list of payloads: 1, 2, 3...
- Then apply the following: A1, B1, C1, A2, B2, C2, A3, B3, C3...

#### Battering Ram

- Given multiple payload positions: A, B, C...
- And a single list of payloads: 1, 2, 3...
- Then apply the following: A1-B1-C1, A2-B2-C2, A3-B3-C3...

#### Pitchfork

- Given multiple payload positions: A, B, C...
- And a set of payloads for position A: 1, 2, 3
- And a set of payloads for position B: 4, 5, 6
- And a set of payloads for position C: 7, 8, 9
- Then apply the following: A1-B4-C7, A2-B5-C8, A3-B6-C9...

Essentially each 'column'.

#### Cluster Bomb

- Given multiple payload positions: A, B, C...
- And a set of payloads for position A: 1, 2, 3
- And a set of payloads for position B: 4, 5, 6
- And a set of payloads for position C: 7, 8, 9
- Then apply the following: A1-B4-C7, A1-B4-C8, A1-B4-C9...

Essentially every single permutation.
