# Customer Complaint Management (`reclamation_client`)

Odoo 19 module to create, assign, track and close customer complaints with a full
workflow and a printable PDF report.

## Features

- **Auto-numbered complaints** in the `REC/YYYY/NNN` format (via an `ir.sequence`).
- **Full workflow**: `New` → `In Progress` → `Resolved` → `Closed`, with one-click
  buttons (`Start`, `Mark as Resolved`, `Close`, `Reset to New`).
- **Assignment & prioritization**: assign to a responsible user and set a priority
  (Low / Medium / High).
- **Computed resolution delay** (days between opening and closing dates).
- **Chatter** (messages, activities, field tracking) via `mail.thread` and
  `mail.activity.mixin`.
- **List view** with state-based color decorations, **form view** with statusbar,
  and a **search view** with filters and group-by.
- **QWeb PDF report** bound to the model with a Print action.

## Installation

1. Make sure the `addons/` folder is in your Odoo `addons_path` (already configured in
   `odoo.conf` / `docker-compose.yml`).
2. Start the stack:

```bash
docker compose up -d
```

3. In Odoo, enable developer mode, update the apps list, then search for
   **Customer Complaint Management** and install it.

## Technical details

| Item            | Value                                  |
| --------------- | -------------------------------------- |
| Model           | `reclamation.client`                   |
| Sequence code   | `reclamation.client`                   |
| Depends         | `base`, `mail`, `contacts`             |
| Version         | `19.0.1.0.0`                           |
| License         | `OPL-1`                                |

## Workflow buttons

| Button             | Method            | From state                | To state      |
| ------------------ | ----------------- | ------------------------- | ------------- |
| Start              | `action_start`    | `new`                     | `in_progress` |
| Mark as Resolved   | `action_resolve`  | `in_progress`             | `resolved`    |
| Close              | `action_close`    | `in_progress`, `resolved` | `closed`      |
| Reset to New       | `action_reset`    | any                       | `new`         |
