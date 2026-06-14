# Security Policy

## Scope

This repository is an **open-core protocol + reference demo**. It contains:

- documentation and machine-readable schemas;
- a minimal reference runtime that uses **mock data only**.

It deliberately contains **no** secrets, API keys, tokens, server addresses,
production code, customer data, or business strategy. The live commercial
METAai organism is maintained privately and is out of scope here.

## No secrets, ever

- Never commit real credentials. Use `.env` (git-ignored) and keep
  `.env.example` as the only template.
- The reference runtime must run without any real provider keys (it ships with
  a mock LLM and in-memory stores).

## Reporting a vulnerability

If you find a security issue in the reference code or schemas, please open a
private report via GitHub Security Advisories (or contact the author listed in
`AUTHORS.md`) rather than a public issue. We aim to respond within a few days.
