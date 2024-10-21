---
layout: Integration
status: published
name: Not Diamond
title: Dagster & Not Diamond
sidebar_label: Not Diamond
excerpt: Integrate Not Diamond calls into your Dagster pipelines to dynamically route your LLM prompts to the best model for your needs.
date: 2024-03-12
apireflink: https://docs.notdiamond.ai
docslink: https://docs.dagster.io/integrations/notdiamond
partnerlink:
logo: /integrations/notdiamond.svg
categories:
  - Other
enabledBy:
enables:
---

### About this integration

The `dagster-notdiamond` library allows you to easily interact with the Not Diamond REST API using the Not Diamond Python SDK to dynamically route LLM prompts to the best AI models within into your Dagster pipelines. You can also log Not Diamond API usage metadata in Dagster Insights, giving you detailed observability on routing usage.

When paired with Dagster assets, the resource automatically logs Not Diamond usage metadata in asset metadata.

### Installation

```bash
pip install dagster dagster-notdiamond
```

### Example

<CodeExample filePath="integrations/notdiamond.py" language="python" />

### About Not Diamond

Not Diamond is building an AI model router which dynamically recommends the best model for a LLM prompt in accordance with a user's goals and needs.