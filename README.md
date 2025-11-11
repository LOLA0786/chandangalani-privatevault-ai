<<<<<<< HEAD
# CloudShift — Multi-Cloud FinOps Autopilot (Demo Monorepo)

This repo contains a **local-first demo** for the CloudShift MVP:
- **apps/api** — Fastify + TypeScript API (sample collectors, rules, Razorpay mock, Actions DSL runner)
- **apps/web** — React + Vite dashboard (Supabase Auth stub, Recharts)
- **packages/core** — normalization, rules engine, Lock‑in Escape Index™ (LEI), YAML actions

> Works **offline** using sample spend exports. Flip to live mode by plugging real SDK creds in `.env` later.

## Quickstart

```bash
# 0) Install pnpm first if needed
npm i -g pnpm

# 1) Install deps in all workspaces
pnpm i

# 2) Start API + Web (two terminals)
pnpm dev:api
pnpm dev:web
```

- API ➜ http://127.0.0.1:8787/health  
- Web ➜ http://127.0.0.1:5173

> Demo uses **sample CSVs** under `data/sample/`. No cloud credentials required.
=======
# TechDebt - AI-Powered Technical Debt Analyzer

Comprehensive tool for detecting and managing technical debt in your codebase.

## Features
- 🔍 14 types of technical debt detection
- 🤖 AI-powered analysis
- 📊 Automated reports
- ⚙️ GitHub Actions integration

## Quick Start
```bash
# Analyze your code
python tools/tech_debt_analyzer.py src

# View report
cat tech-debt-report.json
```

## Categories Analyzed
- Legacy Code
- Security Vulnerabilities
- Performance Issues
- Code Duplication
- Missing Tests
- Poor Documentation
- And more...
>>>>>>> debt-origin/main
