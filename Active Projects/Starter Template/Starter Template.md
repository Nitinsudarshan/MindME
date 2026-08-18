---
title: Starter Template
aliases: [Next.js Shadcn Boilerplate, boilerplate]
tags: [active-projects, web, template]
type: resource
status: evergreen
created: 2026-08-18
updated: 2026-08-18
related: ["[[Active Projects]]", "[[Web Application & Full-Stack Exposure]]", "[[Git, GitHub & Vercel]]"]
source: https://github.com/Nitinsudarshan/boilerplate.git
---

# Starter Template

## What it is

A personal Next.js + Shadcn UI boilerplate — the default starting point for a new web project, so each one doesn't re-derive the same App Router/Tailwind/component setup from scratch.

**Repo**: [github.com/Nitinsudarshan/boilerplate](https://github.com/Nitinsudarshan/boilerplate.git) · MIT licensed

## Stack

- **Next.js 16** (App Router)
- **Tailwind CSS v4**
- **Shadcn UI**, pre-configured
- **React 19**, fully type-safe (TypeScript)
- Dark mode out of the box (`next-themes`)

## What's included

- `AppSidebar` — a generic application sidebar
- `SiteHeader` — top navigation with a user menu and theme toggle
- `LoginForm` — a generic placeholder login form
- A `rules/` folder of its own — code standards, component architecture, project structure, design system, UI components, accessibility, responsive design, and documentation conventions. This is a smaller subset of the same rule categories now copied into [[Active Projects]]'s `Rules/` folder from NGConnect, which extends this same rule set with the domain-specific rules (data access, security, RBAC, etc.) a real production app needs on top of a boilerplate.

## Structure

```
src/app/         Next.js App Router pages and layouts
src/components/  Shadcn UI components and shared UI elements
src/contexts/    React context providers (e.g. user-context)
src/lib/         Utility functions
```

## My Take

This is the layer below [[Active Projects]]'s `.agents` and `Rules` folders — where those two are about *how an AI agent should work* on a Next.js/Supabase project (conventions, precedence, RBAC patterns), this is the actual runnable skeleton those conventions apply to. Starting a new project from this repo plus the copied `.agents`/`Rules` folders reconstitutes most of NGConnect's working setup without carrying NGConnect's actual application code.

## Related

- [[Active Projects]]
- [[Web Application & Full-Stack Exposure]]
- [[Git, GitHub & Vercel]]
