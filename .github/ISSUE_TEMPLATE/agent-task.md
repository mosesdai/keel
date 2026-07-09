---
name: Agent task
description: Standard autonomous agent work item (label agent)
title: "[agent]: "
labels:
  - agent
body:
  - type: markdown
    attributes:
      value: |
        标准 agent 任务。Agent 读 `AUTONOMOUS_DEV.md` + `PLAYBOOK.md` 当前阶段后开 PR。
        **勿在 issue 中粘贴 API key 或 `.env` 内容。**
  - type: dropdown
    id: stage
    attributes:
      label: 目标阶段
      options:
        - S0 云上底座
        - S1 Bridge Track (7/15)
        - S2 原生 Alpha
        - S3 TestFlight
        - S4 稳定化
    validations:
      required: true
  - type: textarea
    id: goal
    attributes:
      label: 目标（一句话）
      placeholder: 例：按 research/05 改进 demo 历史 tab 空状态
    validations:
      required: true
  - type: textarea
    id: value
    attributes:
      label: 用户价值（九叔 / Moses / agent）
    validations:
      required: true
  - type: textarea
    id: tasks
    attributes:
      label: 任务清单（checkbox 格式）
      value: |
        - [ ] 
        - [ ] 
    validations:
      required: true
  - type: textarea
    id: dod
    attributes:
      label: Definition of Done（引用 ACCEPTANCE.md 或具体验收）
    validations:
      required: true
  - type: checkboxes
    id: gate
    attributes:
      label: 是否触发 Moses 决策门禁
      options:
        - label: decision-gate（需要 Moses review 后再 merge）
  - type: textarea
    id: refs
    attributes:
      label: 参考文件（可选）
      placeholder: |
        - PLAYBOOK.md §S1
        - issues/002-S1-bridge-jiushu.md
