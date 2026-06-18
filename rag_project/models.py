from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Document:
    content: str
    source: str
    metadata: Dict = field(default_factory=dict)


@dataclass
class Chunk:
    content: str
    source: str
    chunk_id: int
    metadata: Dict = field(default_factory=dict)


@dataclass
class SearchResult:
    chunk: Chunk
    score: float

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Document:
    content: str
    source: str
    metadata: Dict = field(default_factory=dict)


@dataclass
class Chunk:
    content: str
    source: str
    chunk_id: int
    metadata: Dict = field(default_factory=dict)


@dataclass
class RetrievedChunk:
    content: str
    source: str
    chunk_id: int
    score: float