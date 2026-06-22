from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ProgressEvent:
    node_name: str
    elapsed_ms: int
    fields_updated: list[str] = field(default_factory=list)
    status: str = "completed"
    message: str | None = None
